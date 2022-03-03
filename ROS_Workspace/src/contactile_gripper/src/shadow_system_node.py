#!/usr/bin/env python
"""
This module is a shadow system for testing.
"""

import rospy
import roslib; roslib.load_manifest('contactile_gripper')
from contactile_gripper.srv import GripperChangeMode,StepperOff,StepperSetLimit,DataRecorder,UIMenu
from std_msgs.msg import String,Int64,Int32
from contactile_gripper.msg import Float32List,Int32List
from contactile_gripper.srv import GripperChangeMode,ChangeMode,DataRecorder,StepperOff,StepperSetLimit,UIMenu
import srv_clients

#TODO: Refactor to work with goal position.
#TODO: Refactor to not have differt sets of modes.

class GripperNode(object):
    """ROS node for the gripper. Max com speed is ~62hz for read or write operation. This is both reading
    and writing, so rate is 30hz. """
    def __init__(self):
        rospy.init_node('shadow_system_node', anonymous=False, log_level=rospy.DEBUG)

        # Publishers
        self.gripper_pos_pub = rospy.Publisher('Gripper_Pos',Int64, queue_size=1)
        self.gripper_mode_pub = rospy.Publisher('Gripper_Mode',String, queue_size=1)
        self.IMU_pub = rospy.Publisher('IMU_Acc', Float32List, queue_size=1)
        self.stepper_pos_pub = rospy.Publisher('Stepper_Pos',Int64, queue_size=1)
        self.limit_switch_pub = rospy.Publisher('Limit_Switch_Status', Int32List, queue_size=1)

        # Services
        self.gripper_change_mode_srv = rospy.Service('gripper_change_mode_srv', GripperChangeMode, self.srv_handle_change_mode)
        self.stepper_off_srv = rospy.Service('stepper_off_srv', StepperOff, self.srv_handle_stepper_off)
        self.stepper_set_limit_srv = rospy.Service('stepper_set_limit_srv', StepperSetLimit, self.srv_handle_stepper_set_limit)


        self.pub_loop_rate = 1  # Hz
        self.pub_loop_rate_obj = rospy.Rate(self.pub_loop_rate)
        self.pub_loop()

    def pub_loop(self):
        """This is the main loop for the node which executes at self.pub_loop_rate."""
        while not rospy.is_shutdown():
            self.IMU_pub.publish([3, 4, 5])
            self.gripper_pos_pub.publish(60)
            self.gripper_mode_pub.publish('off')
            self.stepper_pos_pub.publish(50)
            self.limit_switch_pub.publish([1,0])

            self.pub_loop_rate_obj.sleep()

    def srv_handle_change_mode(self, req):
        print(req)
        return GripperChangeModeResponse('Mode changed')

    def srv_handle_stepper_off(self, req):
        return StepperOffResponse('Stepper off')

    def srv_handle_stepper_set_limit(self, req):
        return StepperSetLimitResponse(50)

    def gripper_cmd_callback(self, msg):
        cmd = msg.data.split('_')
        msg_cmd_mode = cmd[0]
        self.cmd_val = int(cmd[1])
        if self.cmd_mode != msg_cmd_mode:
            self.update_cmd_mode(msg_cmd_mode)

    def srv_handle_change_mode(self, req):
        rospy.logwarn('[srv_handle_change_mode] {}'.format(req.mode))
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

    def get_pos(self):
        pos, com_err = self.gripper.motor.read_pos()
        if not com_err:
            self.gripper_pos_pub.publish(pos)
            self.gripper_pos = pos

    def send_command(self):
        if self.cmd_mode == 'position':
            self.gripper.motor.write_goal_pos(self.gripper_pos + self.cmd_val)
        elif self.cmd_mode == 'current':
            self.gripper.motor.write_goal_cur(self.cmd_val)

    def shutdown_function(self):
        #TODO: remove
        srv_clients.data_recorder_client(['/Gripper_Pos','/Gripper_Mode'], file_prefix='experiment1', stop=True)
        # pass

def main():
    _ = GripperNode()

if __name__ == '__main__':
    main()
