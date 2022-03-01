#!/usr/bin/env python

import rospy
from contactile_gripper.srv import DataRecorder
import subprocess, shlex
import datetime as dt
import os

class DataRecorderNode(object):

    def __init__(self):
        rospy.init_node('data_recorder_node')
        self.active_process = None
        rospy.Service('data_recorder_srv', DataRecorder, self.callback)

    def callback(self, req):
        if req.stop:
            self.stop()
        elif not req.stop:
            self.start(req.file_prefix,req.topic_list)
        else:
            rospy.logerr("DataRecorderNode -> callback: req.stop must be a bool (received: {})".format(req.stop))
        return []

    def stop(self):
        if self.active_process is not None:
            self.active_process.terminate()
            self.active_process = None

    def start(self,file_prefix,topic_list):
        self.stop() # Stop if already recording.
        path = '/home/ted/Documents/GitHub/IMML_Contactile_Gripper/bag/'
        timestamp = str(dt.datetime.now())
        timestamp = timestamp.replace(' ','_')
        filename = path + file_prefix + '_' + timestamp
        msg = "rosbag record -O {} ".format(filename) + ' '.join(topic_list)
        args = shlex.split(msg)
        self.active_process = subprocess.Popen(args, stderr=subprocess.PIPE, shell=False)


if __name__ == '__main__':
    _ = DataRecorderNode()
    rospy.spin()