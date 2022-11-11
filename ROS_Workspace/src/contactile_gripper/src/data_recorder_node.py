#!/usr/bin/env python2

import rospy
from contactile_gripper.srv import *
import subprocess, shlex
import datetime as dt
import os

class DataRecorderNode(object):

    def __init__(self):
        rospy.init_node('data_recorder_node')
        self.active_process = None
        rospy.Service('data_recorder_srv', DataRecorder, self.callback)
        rospy.on_shutdown(self.shutdown_function)
        rospy.loginfo("\nData recorder node initialized.\n")
        rospy.spin()

    def callback(self, req):
        if req.stop:
            self.stop()
        elif not req.stop:
            self.start(req.file_prefix,req.topic_list)
        else:
            rospy.logerr("DataRecorderNode -> callback: req.stop must be a bool (received: {})".format(req.stop))
        return []

    def stop(self):
        rospy.loginfo("\nStop record\n")
        if self.active_process is not None:
            self.active_process.terminate()
            self.active_process = None

    def start(self,file_prefix,topic_list):
        rospy.loginfo("\nStart recording: {}\n{}".format(file_prefix,topic_list))
        # self.stop() # Stop if already recording.
        msg = "rosbag record -o {} ".format(file_prefix) + ' '.join(topic_list)
        args = shlex.split(msg)
        self.active_process = subprocess.Popen(args, stderr=subprocess.PIPE, shell=False)

    def shutdown_function(self):
        self.stop()

if __name__ == '__main__':
    _ = DataRecorderNode()