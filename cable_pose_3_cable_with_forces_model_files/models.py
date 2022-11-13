"""Models to make pose predictions"""


import shutil
import time
import os
import pandas as pd
import numpy as np
import math
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
from enum import Enum
import warnings
from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings(action='ignore', category=ConvergenceWarning)
pd.set_option("display.max_rows", None, "display.max_columns", None)


class ModelType(Enum):
    MLPRegressor = 1
    KNeighborsRegressor = 2
    LinearRegression = 3
    LinearAnalytical = 4

class DataOptions(Enum):
    """The numbers are the number of input features for the data option."""
    ALL = 39
    Z_ONLY = 10
    CONTACT_ONLY = 9



class LinearAnalytical:
    """Produces linear regression prediction from the contact/no contact points. The most simple baseline to compare
    other models."""
    def __init__(self):
        self.pil_point_map = {0:[1,1], 1:[1,0], 2:[1,-1], 3:[0,1], 4:[0,0], 5:[0,-1], 6:[-1,1], 7:[-1,0], 8:[-1,-1]}
        self.pos_scale = 7  # Each pillar is 7 mm apart.

    def predict(self, samples):
        """Takes a (n,9) numpy array of samples, and returns predicted position and angle. Sample must be only
        contact/no contact binary 1's or 0's."""
        predictions = []
        for sample in samples:
            x_points, y_points = [], []
            for pil_num in range(len(sample)):
                if sample[pil_num]:
                    point = self.pil_point_map[pil_num]
                    x_points.append(point[0])
                    y_points.append(point[1])
            # If not enough points to make a prediction.
            if len(x_points) < 2:
                predictions.append([0,0])
                continue
            elif len(x_points) == 2:
                pos,ang = self.__find_2pt_pose(x_points,y_points)
            else:
                # Do linear regression on contact points.
                z = np.polyfit(x_points, y_points, 1)
                p = np.poly1d(z)
                if len(p.c) == 1:  # Slope is zero.
                    slope = 0
                    intercept = p.c[0]
                else:
                    slope = p.c[0]
                    intercept = p.c[1]
                ang = math.degrees(math.atan(slope))
                pos = intercept * self.pos_scale
            predictions.append([pos,-ang])
        return np.array(predictions)

    def __find_2pt_pose(self,x_points,y_points):
        if x_points[0]==x_points[1]: # Vertical slope...
            ang = 90
            pos = np.average(y_points)
        else:
            m = (y_points[1]-y_points[0]) / (x_points[1]-x_points[0])
            if m == 0:
                b = y_points[0]
            elif x_points[0] == 0:
                b = y_points[0]
            elif x_points[1] == 0:
                b = y_points[1]
            else:
                b = y_points[0] / (m*x_points[0])
            ang = np.rad2deg(np.arctan(m))
            pos = b * self.pos_scale
        return pos,ang


class PoseModel:
    def __init__(self,model_type, data_type = DataOptions.ALL, X_train=None, y_train=None, X_test=None, y_test=None, model_fn = None):
        self.model_options = {'MLPRegressor','KNeighborsRegressor','LinearRegression','LinearAnalytical'}
        self.model_type = model_type
        self.data_type = data_type
        self.model = None if model_fn is None else self.load_model(model_fn)
        self.X_train, self.y_train,self.X_test, self.y_test = self.__prep_data(X_train,y_train,X_test,y_test)

    def train(self,epochs = [100,500,2000], lr_range = [0.005,0.001,0.0005],hidden_range = [25,500],random_inits = 5,
              neighbors = 5, save = False, save_fn = "model.sav", show_progress = False):
        assert self.X_train is not None and self.y_train is not None
        if self.model_type == ModelType.MLPRegressor:
            self.model = self.__find_best_model(random_inits,show_progress)
            # self.model = self.__find_best_model2(random_inits, epochs, lr_range, hidden_range, show_progress)
        elif self.model_type == ModelType.LinearRegression:
            self.model = LinearRegression().fit(self.X_train, self.y_train)
        elif self.model_type == ModelType.KNeighborsRegressor:
            self.model = KNeighborsRegressor(neighbors, weights='uniform').fit(self.X_train, self.y_train)
        elif self.model_type == ModelType.LinearAnalytical:
            self.model = LinearAnalytical()
        else: raise KeyError
        if save: self.save_model(save_fn)

    def report(self,save=False,report_fn = "report.txt",extra_header = " "):
        y_pred = self.model.predict(self.X_test)
        rmse, mse, r2, ave_err, standard_dev, max_err, scaled= self.__get_perf_data(y_pred, scaled=False)
        header = "\n\nModel Type: {}\nData Used: {}\n{}".format(self.model_type.name, self.data_type.name, extra_header)
        perf_info = '\nRMSE: {}\nAve err: {}\nStd err: {}\nMax err: {}\nR²: {}\nData scaled: {}'.format(rmse,ave_err,standard_dev,max_err,r2,scaled)
        print(header,perf_info)
        if save:
            with open(report_fn, 'w') as f:
                f.write(header)
                f.write(perf_info)
        return header+perf_info

    def load_model(self, filepath):
        if self.model_type == ModelType.LinearAnalytical: return
        self.saved_model_filepath = filepath
        model = joblib.load(filepath)
        assert self.model_type.name in str(type(model))
        assert model.n_features_in_ == self.data_type.value
        return joblib.load(filepath)

    def save_model(self, filename):
        assert self.model is not None
        if self.model_type == ModelType.LinearAnalytical: return
        joblib.dump(self.model, filename)

    def __prep_data(self,X_tr,y_tr,X_te,y_te):
        if self.model_type == ModelType.LinearAnalytical: assert self.data_type == DataOptions.CONTACT_ONLY
        if self.data_type == DataOptions.CONTACT_ONLY and X_tr is not None:
            X_train, y_train = self.__drop_data(X_tr),y_tr.to_numpy()
            if X_te is not None:
                X_test, y_test = self.__drop_data(X_te),y_te.to_numpy()
            else: X_test, y_test = None, None
        elif self.data_type == DataOptions.Z_ONLY and X_tr is not None:
            X_train, y_train = self.__drop_data(X_tr), y_tr.to_numpy()
            if X_te is not None:
                X_test, y_test = self.__drop_data(X_te), y_te.to_numpy()
            else: X_test, y_test = None, None
            input_scaler = StandardScaler()
            X_train = input_scaler.fit_transform(X_train)
            if X_te is not None:
                X_test = input_scaler.transform(X_test)
        elif self.data_type == DataOptions.ALL and X_tr is not None:
            input_scaler = StandardScaler()
            X_train, y_train = input_scaler.fit_transform(X_tr), y_tr.to_numpy()
            if X_te is not None:
                X_test, y_test = input_scaler.transform(X_te), y_te.to_numpy()
            else: X_test, y_test = None, None
        else: X_train, y_train, X_test, y_test = None,None,None,None
        if y_train is not None:
            self.output_scaler = StandardScaler()
            self.output_scaler.fit(y_train)
        return X_train, y_train, X_test, y_test

    def __drop_data(self,data):
        if data is None: return None
        drop_indexes = self.__find_drop_indexes(data)
        data = data.drop(data.columns[drop_indexes], axis=1)
        return data.to_numpy()

    def __find_drop_indexes(self,data):
        col_headers = list(data)
        indexes = []
        for i, header in enumerate(col_headers):
            if "contact" not in header and self.data_type == DataOptions.CONTACT_ONLY: indexes.append(i)
            if "z" not in header and self.data_type == DataOptions.Z_ONLY: indexes.append(i)
        return indexes

    def __find_best_model(self,num_rands,show_progress):
        """The default parameters are good enough to get something good."""
        rand_ints = np.random.randint(0,9999,num_rands)
        best_rmse, best_lr, best_epoch, best_hidden = None, None, None, None
        best_model = None
        seed_intervals = []
        for i, seed in enumerate(rand_ints):
            seed_start_time = time.time()
            m = MLPRegressor(random_state=seed).fit(self.X_train, self.y_train)
            y_pred = m.predict(self.X_test)
            rmse, mse, r2, ave_err, standard_dev, max_err, scaled = self.__get_perf_data(y_pred, scaled=False)
            if best_rmse is None or rmse < best_rmse:
                best_rmse,best_model = rmse,m
                if show_progress:
                    print('RMSE: {}\nStd: {}\nMax err: {}\nR²: {}\n'.format(rmse, standard_dev, max_err, r2))
            seed_intervals.append(time.time()-seed_start_time)
            ave_seed_time = np.average(seed_intervals)
            rounds_left = num_rands-1-i
            print("MLP training - Estimated remaining time: {} min".format(ave_seed_time*rounds_left/60))
        return best_model

    def __find_best_model2(self,num_rands,epochs,lrs,hidden_range,show_progress):
        rand_ints = np.random.randint(0,9999,num_rands)
        best_rmse, best_lr, best_epoch, best_hidden = None, None, None, None
        best_model = None
        seed_intervals = []
        for i, seed in enumerate(rand_ints):
            seed_start_time = time.time()
            for lr in lrs:
                for epoch in epochs:
                    for num_hiddens in hidden_range:
                        m = MLPRegressor(hidden_layer_sizes=[num_hiddens], max_iter=epoch, learning_rate_init=lr, \
                                             random_state=seed).fit(self.X_train, self.y_train)
                        y_pred = m.predict(self.X_test)
                        rmse, mse, r2, ave_err, standard_dev, max_err = self.__get_perf_data(y_pred, scaled=False)
                        if best_rmse is None or rmse < best_rmse:
                            best_rmse,best_lr,best_epoch,best_hidden,best_model = rmse,lr,epoch,num_hiddens,m
                            if show_progress:
                                print("\n\nNew best: \nRMSE: {}\nLR: {}\nEpoch: {}\nHiddens: {}\n\n".format(rmse,lr,epoch,num_hiddens))
                                print('RMSE: {}\nStd: {}\nMax err: {}\nR²: {}\n'.format(rmse, standard_dev, max_err, r2))
            seed_intervals.append(time.time()-seed_start_time)
            ave_seed_time = np.average(seed_intervals)
            rounds_left = num_rands-1-i
            print("MLP training - Estimated remaining time: {} min".format(ave_seed_time*rounds_left/60))
        return best_model

    def __get_perf_data(self,y_pred,scaled=True):
        error = np.abs(y_pred - self.y_test)
        error.sum(axis=1)
        ave_err, standard_dev, max_err = np.average(error), np.std(error), np.max(error)
        if scaled: y_pred, y_test = self.output_scaler.transform(y_pred), self.output_scaler.transform(self.y_test)
        else: y_test = self.y_test
        mse = mean_squared_error(y_pred, y_test)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_pred, y_test)
        return rmse, mse, r2, ave_err, standard_dev, max_err,scaled

def evaluate_all():
    data_dir_name = "cable_pose_3_cable_with_forces"
    dataset_path = os.getcwd() + '\\' + 'processed_data' + '\\' + data_dir_name + '\\'
    X_train = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_X_train_30-70.csv')
    y_train = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_y_train_30-70.csv')
    X_test = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_X_test_30-70.csv')
    y_test = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_y_test_30-70.csv')

    full_report = ""
    data_options = [DataOptions.Z_ONLY, DataOptions.ALL]

    full_report += "\n\n\n################ LinearAnalytical ################"
    model = PoseModel(ModelType.LinearAnalytical, DataOptions.CONTACT_ONLY, X_train=X_train, y_train=y_train,
                      X_test=X_test,
                      y_test=y_test)
    model.train(save=False, save_fn="{}_{}.sav".format(model.model_type.name, model.data_type.name))
    report = model.report(save=False, report_fn="{}_{}_report.txt".format(model.model_type.name, model.data_type.name))
    full_report += report

    full_report += "\n\n\n################ LinearRegression ################"
    for data_option in data_options:
        model = PoseModel(ModelType.LinearRegression, data_option, X_train=X_train, y_train=y_train, X_test=X_test,
                          y_test=y_test)
        model.train(save=False, save_fn="{}_{}.sav".format(model.model_type.name, model.data_type.name))
        report = model.report(save=False,
                              report_fn="{}_{}_report.txt".format(model.model_type.name, model.data_type.name))
        full_report += report

    neighbors = [3, 4, 5, 6, 8, 12, 20, 35]
    full_report += "\n\n\n################ KNeighborsRegressor ################"
    for data_option in data_options:
        for n in neighbors:
            model = PoseModel(ModelType.KNeighborsRegressor, data_option, X_train=X_train, y_train=y_train,
                              X_test=X_test, y_test=y_test)
            model.train(neighbors=n, save=False,
                        save_fn="{}_{}_{}neighbors.sav".format(model.model_type.name, model.data_type.name, n))
            report_fn = "{}_{}_{}neighbors_report.txt".format(model.model_type.name, model.data_type.name, n)
            extra_header = "Neighbors: {}".format(n)
            report = model.report(save=False, report_fn=report_fn, extra_header=extra_header)
            full_report += report

    num_models = 5
    rand_inits = 5
    full_report += "\n\n\n################ MLPRegressor ################"
    for data_option in data_options:
        for n in range(num_models):
            model = PoseModel(ModelType.MLPRegressor, data_option, X_train=X_train, y_train=y_train, X_test=X_test,
                              y_test=y_test)
            model.train(random_inits=rand_inits, save=False,
                        save_fn="{}_{}_{}.sav".format(model.model_type.name, model.data_type.name, n))
            report_fn = "{}_{}_{}_report.txt".format(model.model_type.name, model.data_type.name, n)
            extra_header = "Default Sklearn MLPRegressor params. \nModel num: {}\nRandom initializations: {}\nCriteria: RMSE".format(
                n, rand_inits)
            report = model.report(save=False, report_fn=report_fn, extra_header=extra_header)
            full_report += report

    with open("full_report.txt", 'w') as f:
        f.write(full_report)


def train_with_all_data():
    data_dir_name = "cable_pose_3_cable_with_forces"
    dataset_path = os.getcwd() + '\\' + 'processed_data' + '\\' + data_dir_name + '\\'
    X_train = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_X_train_10-90.csv')
    y_train = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_y_train_10-90.csv')
    X_test = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_X_test_10-90.csv')
    y_test = pd.read_csv(dataset_path + 'cable_pose_3_cable_with_forces_y_test_10-90.csv')

    data_options = [DataOptions.Z_ONLY, DataOptions.ALL]

    for data_option in data_options:
        model = PoseModel(ModelType.LinearRegression, data_option, X_train=X_train, y_train=y_train, X_test=X_test,
                              y_test=y_test)
        model.train(save=True, save_fn="{}_{}.sav".format(model.model_type.name, model.data_type.name))

    neighbors = [3, 4, 5, 6, 8, 12, 20, 35]
    for data_option in data_options:
        for n in neighbors:
            model = PoseModel(ModelType.KNeighborsRegressor, data_option, X_train=X_train, y_train=y_train, X_test=X_test,
                              y_test=y_test)
            model.train(neighbors=n, save=True,
                        save_fn="{}_{}_{}neighbors.sav".format(model.model_type.name, model.data_type.name, n))

    num_models = 5
    rand_inits = 5
    for data_option in data_options:
        for n in range(num_models):
            model = PoseModel(ModelType.MLPRegressor, data_option, X_train=X_train, y_train=y_train, X_test=X_test,
                              y_test=y_test)
            model.train(random_inits=rand_inits, save=True,
                        save_fn="{}_{}_{}.sav".format(model.model_type.name, model.data_type.name, n))



def main():
    # evaluate_all()
    train_with_all_data()

if __name__ == '__main__':
    main()