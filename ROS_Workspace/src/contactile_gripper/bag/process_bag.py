import bagpy
from bagpy import bagreader
import pandas as pd
b = bagreader('grasp_and_release_2022-03-07-23-44-12.bag')
# replace the topic name as per your need
MSG = b.message_by_topic(['/Gripper_Pos', '/hub_0/sensor_0', '/hub_0/sensor_1'])
MSG
data = pd.read_csv(MSG)
data # prints laser data in the form of pandas dataframe