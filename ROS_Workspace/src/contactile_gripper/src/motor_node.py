#!/usr/bin/env python
"""
This module contains the gripper node.
"""

import roslib; roslib.load_manifest('contactile_gripper')
from contactile_gripper.srv import *
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int32
import gripper

class MotorNode(object):
    """ROS node for the Dynamixel motor. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        rospy.init_node('motor_node', anonymous=False, log_level=rospy.INFO)
        self.goal_pos_subscriber = rospy.Subscriber('Goal_Position', Int32, self.goal_pos_callback, queue_size=1, buff_size = 100)
        self.motor_publisher = rospy.Publisher('Motor_Position',Int32, queue_size=1)
        self.change_mode_srv = rospy.Service('change_mode_srv', ChangeMode, self.handle_change_mode)

        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop_rate = 5 # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)

        self.gripper = gripper.Gripper()
        self.data = None
        self.gripper.motor.switch_modes('cur_control')

        self.pub_loop()

    def handle_change_mode(self,req):
        if req.mode == 'passive':
            com_error = True
            while com_error:  # While loop to make sure it turns torque off.
                com_error = self.gripper.motor.write_torque_mode('off')
        elif req.mode == 'position_control':
            self.gripper.motor.switch_modes('ext_pos_control')
        return ChangeModeResponse('Mode changed')

    def goal_pos_callback(self,msg):
        self.gripper.motor.write_goal_pos(msg.data)

    def pub_loop(self):
        """This is the main loop for the node which executes at self.pub_loop_rate."""
        while not rospy.is_shutdown():
            pos,err = self.gripper.motor.read_pos()
            if not err: self.motor_publisher.publish(pos)
            self.pub_loop_rate_obj.sleep()

    def shutdown_function(self):
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    gripper_node = MotorNode()

if __name__ == '__main__':
    main()
