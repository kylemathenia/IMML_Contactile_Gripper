import bagpy
from bagpy import bagreader
import pandas as pd
b = bagreader('grasp_and_release_2022-03-09-21-39-10.bag')
# replace the topic name as per your need
MSG = b.message_by_topic(['/hub_0/sensor_0'])
MSG
data = pd.read_csv(MSG)
data # prints laser data in the form of pandas dataframe