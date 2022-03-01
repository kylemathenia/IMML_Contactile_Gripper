import bagpy
from bagpy import bagreader
import pandas as pd
b = bagreader('test.bag')
# replace the topic name as per your need
MSG = b.message_by_topic('Stepper_Cmd')
MSG
data = pd.read_csv(MSG)
data # prints laser data in the form of pandas dataframe