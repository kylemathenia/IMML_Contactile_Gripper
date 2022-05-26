"""Models to make pose predictions"""


import shutil
import os
import pandas as pd
import numpy as np
import math

pd.set_option("display.max_rows", None, "display.max_columns", None)


class LinearAnalytical:
    """Produces linear regression from the contact/no contact points."""
    def __init__(self,data):
        self.data = data
        self.pos_err,self.ang_err = [],[]
        self.pil_point_map = {0:[1,1], 1:[1,0], 2:[1,-1], 3:[0,1], 4:[0,0], 5:[0,-1], 6:[-1,1], 7:[-1,0], 8:[-1,-1]}
        self.drop_cont_indexes = [0,1,2,3,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,32,33,34,36,37,38,40,41]

    def evaluate(self):
        """Evaluates the model. Prints results. Since this is an analytical model, all of the data can be used
        to evaluate"""
        self.pos_err,self.ang_err = [],[]
        # For every sample in the data, predict, and add errors.
        for sample_num in range(len(self.data)):
            sample = self.data.iloc[[sample_num]]
            pos,ang = self.predict(sample)
            if pos is not None:
                self.pos_err.append(abs((pos - float(sample.position))))
                self.ang_err.append(abs((ang - float(sample.angle))))
        self.show_eval_results()

    def show_eval_results(self):
        """Prints mean error and std deviation for each."""
        mean_pos_err = np.mean(self.pos_err)
        std_pos_err = np.std(self.pos_err)
        mean_ang_err = np.mean(self.ang_err)
        std_ang_err = np.std(self.ang_err)
        print("\nPosition Error:\nMean: {}\tStandard Deviation: {}".format(mean_pos_err,std_pos_err))
        print("\nAngle Error:\nMean: {}\tStandard Deviation: {}".format(mean_ang_err, std_ang_err))


    def predict(self,sample):
        """Returns predicted position and angle."""
        x_points,y_points = [],[]
        contacts = sample.drop(sample.columns[self.drop_cont_indexes], axis=1)
        contacts = contacts.reset_index()
        contact_list = contacts.loc[0, :].values.tolist()
        del contact_list[0]
        for pil_num in range(len(contact_list)):
            if contact_list[pil_num]:
                point=self.pil_point_map[pil_num]
                x_points.append(point[0])
                y_points.append(point[1])
        # If not enough points to make a prediction.
        if len(x_points) <= 2:
            return None,None
        # Do linear regression on contact points.
        z = np.polyfit(x_points, y_points, 1)
        p = np.poly1d(z)
        if len(p.c) == 1: # Slope is zero.
            slope = 0
            intercept = p.c[0]
        else:
            slope = p.c[0]
            intercept = p.c[1]
        ang = math.degrees(math.atan(slope))
        pos = intercept
        return pos,ang



def main(data_dir_name):
    data_path = os.getcwd() + '\\' + 'processed_data' + '\\' + data_dir_name + '\\' + 'labeled_data.csv'
    data = pd.read_csv(data_path)
    model = LinearAnalytical(data)
    model.evaluate()

if __name__ == '__main__':
    main("cable_pose_data")
