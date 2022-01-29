#!/usr/bin/env python
"""
This is a shadow version of the rospy module to be used for debugging or executing scripts outside of ROS.
"""

def logdebug(msg, *args, **kwargs):
    print(msg)

def loginfo(msg, *args, **kwargs):
    print(msg)

def logwarn(msg, *args, **kwargs):
    print(msg)

def logerr(msg, *args, **kwargs):
    print(msg)

def logfatal(msg, *args, **kwargs):
    print(msg)
