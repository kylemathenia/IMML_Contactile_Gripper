#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from contactile_gripper.srv import *
import sys, select, termios, tty
settings = termios.tcgetattr(sys.stdin)

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist: key = sys.stdin.read(1)
    else: key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

class UiNode(object):
    def __init__(self):
        rospy.init_node('ui_node', anonymous=False, log_level=rospy.DEBUG)
        self.UI_input_pub = rospy.Publisher('UI_Input',String, queue_size=1)
        self.UI_mode_pub = rospy.Publisher('UI_Mode',String, queue_size=100)

        self.mode_options = set({'passive', 'cur_based_pos_control', 'sinusoidal_motion_routine'})
        self.mode = 'passive'
        self.position_increment = 5
        rospy.loginfo(self.get_prompt())
        self.main_loop()

    def main_loop(self):
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry. This is happening often very fast when nothing is pressed.
            elif self.mode == 'passive': self.passive_func(key)
            elif self.mode == 'cur_based_pos_control': self.cur_based_pos_control_func(key)
            elif self.mode == 'sinusoidal_motion_routine': self.sinusoidal_func(key)

    def change_mode_srv_client(self,mode):
        rospy.wait_for_service('change_mode_srv')
        try:
            change_mode_srv = rospy.ServiceProxy('change_mode_srv',ChangeMode)
            msg = change_mode_srv(mode)
            return msg.response
        except:
            rospy.logerr('Change mode service failed.')

    def passive_func(self,key):
        if key == '1':
            for _ in range(3): self.UI_mode_pub.publish('cur_based_pos_control')
            self.mode = 'cur_based_pos_control'
            rospy.loginfo(self.get_prompt())
        elif key == '2':
            self.mode = 'sinusoidal_motion_routine'
            for _ in range(3): self.UI_mode_pub.publish('sinusoidal_motion_routine')
            rospy.loginfo(self.get_prompt())

    def cur_based_pos_control_func(self,key):
        """f/d : open/close, r/e : increase/decrease increment, backspace: back, space/enter:
        EMERGENCY OFF/PASSIVE MODE"""
        if key == ' ' or key == '\r' or key == '\x1b' or key == '\x7f': # EMERGENCY OFF/PASSIVE or backspace.
            self.change_to_passive()
        elif key == 'f':
            rospy.loginfo('Open - increment {}'.format(self.position_increment))
            self.UI_input_pub.publish(str(-self.position_increment))
        elif key == 'd':
            rospy.loginfo('Close - increment {}'.format(self.position_increment))
            self.UI_input_pub.publish(str(self.position_increment))
        elif key == 'r':
            self.position_increment +=1
            rospy.loginfo('Increment {}'.format(self.position_increment))
        elif key == 'e':
            self.position_increment -= 1
            rospy.loginfo('Increment {}'.format(self.position_increment))
        elif key == 'i':
            rospy.loginfo(self.get_prompt())

    def sinusoidal_func(self,key):
        """SINUSOIDAL MOTION ROUTINE START, s: start, space/enter: EMERGENCY OFF/PASSIVE MODE"""
        if key == ' ' or key == '\r' or key == '\x1b' or key == '\x7f':  # EMERGENCY OFF/PASSIVE or backspace.
            self.change_to_passive()
        elif key == 's':
            rospy.loginfo('START ROUTINE\n')
            self.UI_input_pub.publish('start')

    def change_to_passive(self):
        _ = self.change_mode_srv_client('passive')
        self.UI_mode_pub.publish('passive')
        self.mode = 'passive'
        rospy.loginfo(self.get_prompt())

    def get_prompt(self):
        """Returns the prompt for the current UI screen as a string."""
        if self.mode == 'passive':
            return '\n\nPASSIVE MODE\n1: position control\n2: sinusoidal routine'
        elif self.mode == 'cur_based_pos_control':
            return """
            \n\nPOSITION CONTROL MODE\n
            d/f : open/close
            e/r : increase/decrease increment (Now: {})
            i: show prompt again
            space/enter: EMERGENCY OFF/PASSIVE MODE/BACK\n
            """.format(self.position_increment)
        elif self.mode == 'sinusoidal_motion_routine':
            return """
            \n\nSINUSOIDAL MOTION ROUTINE START\n
            s: start
            space/enter: EMERGENCY OFF/PASSIVE MODE/BACK\n
            """
        else: rospy.log('Error in get_prompt. {} is not a valid mode'.format(self.mode))

def main():
    _ = UiNode()

if __name__ == '__main__':
    main()
