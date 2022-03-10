

# from bagpy import bagreader
import pandas as pd
import numpy as np
# b = bagreader('grasp_and_release_2022-03-09-21-39-10.bag')
# # replace the topic name as per your need
# name_of_csv_file_written = b.message_by_topic(['/hub_0/sensor_0'])
# print(name_of_csv_file_written)
name_of_csv_file_written = 'hub_0-sensor_0.csv'
data = pd.read_csv(name_of_csv_file_written)
my_data = np.genfromtxt(name_of_csv_file_written, delimiter=',')
data # prints laser data in the form of pandas dataframe