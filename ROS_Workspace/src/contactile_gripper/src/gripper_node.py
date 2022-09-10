#!/usr/bin/env python2
"""
This module contains the gripper node.
"""
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'support'))
import roslib; roslib.load_manifest('contactile_gripper')
import rospy
from contactile_gripper.srv import *
from std_msgs.msg import String,Float32,Int64,Int32
import gripper
import srv_clients

#TODO: Refactor to work with goal position.
#TODO: Refactor to not have differt sets of modes.

class GripperNode(object):
    """ROS node for the gripper. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        rospy.init_node('gripper_node', anonymous=False, log_level=rospy.INFO)

        # Initialize and calibrate gripper.
        self.gripper = gripper.Gripper(fast_start=True)

        # Publishers
        self.gripper_pos_pub = rospy.Publisher('Gripper_Pos',Int64, queue_size=1)
        self.gripper_pos = None
        self.gripper_mode_pub = rospy.Publisher('Gripper_Mode',String, queue_size=1)

        # self.pub_loop_rate = 31  # Hz
        self.pub_loop_rate = 60  # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)

        # Subscribers
        self.gripper_cmd_sub = rospy.Subscriber('Gripper_Cmd', String, self.gripper_cmd_callback, queue_size=1, buff_size = 100)

        # Services
        self.gripper_change_mode_srv = rospy.Service('gripper_change_mode_srv', GripperChangeMode, self.srv_handle_change_mode)

        # Setup and start
        self.cmd_mode = None
        self.cmd_val = None
        self.change_mode_flag = False
        self.msg_mode_gripper_mode_conversion = {'off':'passive'}
        rospy.on_shutdown(self.shutdown_function)
        self.pub_loop()

    def pub_loop(self):
        """This is the main loop for the node which executes at self.pub_loop_rate."""
        while not rospy.is_shutdown():
            self.check_if_change_mode()
            self.read_and_publish()
            self.send_command()
            self.pub_loop_rate_obj.sleep()

    def gripper_cmd_callback(self, msg):
        cmd = msg.data.split('_')
        msg_cmd_mode = cmd[0]
        self.cmd_val = int(cmd[1])
        if self.cmd_mode != msg_cmd_mode:
            self.update_cmd_mode(msg_cmd_mode)

    def srv_handle_change_mode(self, req):
        rospy.logdebug('[srv_handle_change_mode] {}'.format(req.mode))
        try:
            assert req.mode in self.gripper.mode_options
            if req.mode == 'off':
                self.update_cmd_mode('off')
            elif req.mode == 'cur_based_pos_control':
                self.update_cmd_mode('position')
            elif req.mode == 'cur_control':
                self.update_cmd_mode('current')
        except:
            rospy.logerr('Change mode service failed.')
        return GripperChangeModeResponse('Mode changed')

    def update_cmd_mode(self,msg_cmd_mode):
        assert msg_cmd_mode == 'position' or msg_cmd_mode == 'current' or msg_cmd_mode == 'off'
        self.change_mode_flag = True
        self.cmd_mode = msg_cmd_mode

    def check_if_change_mode(self):
        if self.change_mode_flag:
            if self.cmd_mode == 'position':
                self.gripper.switch_modes('cur_based_pos_control')
            elif self.cmd_mode == 'current':
                self.gripper.switch_modes('cur_control')
            elif self.cmd_mode == 'off':
                self.gripper.switch_modes('off')
            self.change_mode_flag = False
            self.gripper_mode_pub.publish(self.gripper.mode)

    def read_and_publish(self):
        if self.gripper.mode != 'off':
            pos, com_err = self.gripper.motor.read_pos()
            if not com_err and pos != 0:
                self.gripper_pos_pub.publish(pos)
                self.gripper_pos = pos

    def send_command(self):
        if self.cmd_mode == 'position':
            self.gripper.motor.write_goal_pos(self.cmd_val)
        elif self.cmd_mode == 'current':
            self.gripper.motor.write_goal_cur(self.cmd_val)

    def shutdown_function(self):
        self.gripper.shutdown_function()

def main():
    _ = GripperNode()

if __name__ == '__main__':
    main()
