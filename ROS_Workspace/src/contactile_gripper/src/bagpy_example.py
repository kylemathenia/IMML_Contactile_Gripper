import bagpy
from bagpy import bagreader
import pandas as pd
b = bagreader('experiment1_2022-03-01_01:51:41.249169.bag')
# replace the topic name as per your need
MSG = b.message_by_topic('/Gripper_Pos')
MSG
data = pd.read_csv(MSG)
data # prints laser data in the form of pandas dataframe