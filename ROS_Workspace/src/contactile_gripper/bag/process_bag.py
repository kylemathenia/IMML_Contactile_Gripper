from bagpy import bagreader
import pandas as pd
b = bagreader('grasp_and_release_2022-03-10-12-14-33.bag')
# replace the topic name as per your need
name_of_csv_file = b.message_by_topic(['/hub_0/sensor_0'])
print(name_of_csv_file)
dataframe = pd.read_csv(name_of_csv_file)
dataframe # prints laser data in the form of pandas dataframe