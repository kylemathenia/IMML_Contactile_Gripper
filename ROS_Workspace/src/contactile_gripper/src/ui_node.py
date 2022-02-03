#!/usr/bin/env python
"""
User interface node to control the system.
"""

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from contactile_gripper.srv import *
import sys, select, termios, tty
settings = termios.tcgetattr(sys.stdin)

class UiNode(object):
    def __init__(self):
        rospy.init_node('ui_node', anonymous=False, log_level=rospy.DEBUG)
        self.gripper_cmd_pub = rospy.Publisher('UI_Gripper_Cmd',String, queue_size=1)
        self.gripper_mode_pub = rospy.Publisher('UI_Gripper_Mode',String, queue_size=100)
        self.stepper_cmd_pub = rospy.Publisher('UI_Stepper_Cmd', String, queue_size=1)
        self.stepper_mode_pub = rospy.Publisher('UI_Stepper_Mode', String, queue_size=100)
        
        self.gripper_mode_options = set({'passive', 'cur_based_pos_control', 'sinusoidal_motion_routine'})
        self.gripper_mode = 'passive'
        self.gripper_pos_increment = 5
        self.stepper_mode_options = set({'passive', 'position_control', 'speed_control'})
        self.stepper_mode = 'passive'
        self.stepper_pos_increment = 100

        #TODO: Figure how to do elegant key bindings. Dictionary? Space and enter cannot be printed and used for equality.
        self.key_gripper_open = 'd'
        self.key_gripper_close = 'f'
        self.key_gripper_increment_inc = 'e'
        self.key_gripper_increment_dec = 'r'
        self.key_gripper_open = 'd'
        self.key_gripper_close = 'f'
        self.key_gripper_increment_inc = 'e'
        self.key_gripper_increment_dec = 'r'

        self.current_menu = self.stepper_cal_main_menu
        rospy.loginfo(self.get_prompt())
        self.main_loop()

    def main_loop(self):
        """Continuously get the key inputs from the user and do something."""
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry. This is happening often very fast when nothing is pressed.
            else: self.current_menu(key)

    def main_menu(self,key):
        if key == '1':
            for _ in range(3): self.gripper_mode_pub.publish('cur_based_pos_control')
            self.gripper_mode = 'cur_based_pos_control'
            rospy.loginfo(self.get_prompt())
        elif key == '2':
            self.gripper_mode = 'sinusoidal_motion_routine'
            for _ in range(3): self.gripper_mode_pub.publish('sinusoidal_motion_routine')
            rospy.loginfo(self.get_prompt())

        #TODO: Perhaps there is a slick way to set the prompts so you can always just call self.current_menu.prompt. Perhaps there is a special method.
        main_menu.prompt = """  
        \n\nSTEPPER CALIBRATION MAIN MENU
        LINEAR ACTUATOR RANGE LIMITS MUST BE SET. INCORRECT SETUP COULD BREAK THE GRIPPER OR LINEAR ACTUATOR.\n
        1: Auto calibrate (CAUTION: FULL RANGE OF LINEAR ACTUATOR MUST BE CLEAR OF OBSTRUCTION)
        2: Manual calibrate
        """

    def sys_direct_control_menu(self,key):
        #TODO: Change to include stepper.
        """f/d : open/close, r/e : increase/decrease increment, backspace: back, space/enter:
        EMERGENCY OFF/PASSIVE MODE"""
        if key == ' ' or key == '\r' or key == '\x1b' or key == '\x7f': # EMERGENCY OFF/PASSIVE or backspace.
            self.change_to_passive()
        elif key == 'f':
            rospy.loginfo('Open - increment {}'.format(self.gripper_pos_increment))
            self.gripper_cmd_pub.publish(str(-self.gripper_pos_increment))
        elif key == 'd':
            rospy.loginfo('Close - increment {}'.format(self.gripper_pos_increment))
            self.gripper_cmd_pub.publish(str(self.gripper_pos_increment))
        elif key == 'r':
            self.gripper_pos_increment +=1
            rospy.loginfo('Increment {}'.format(self.gripper_pos_increment))
        elif key == 'e':
            self.gripper_pos_increment -= 1
            rospy.loginfo('Increment {}'.format(self.gripper_pos_increment))
        elif key == 'i':
            rospy.loginfo(self.get_prompt())

    def stepper_cal_main_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        pass

    def stepper_cal_auto_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        pass

    def stepper_cal_manual_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        pass


    def sinusoidal_func(self,key):
        if key == ' ' or key == '\r' or key == '\x1b' or key == '\x7f':  # EMERGENCY OFF/PASSIVE or backspace.
            self.change_to_passive()
        elif key == 's':
            rospy.loginfo('START ROUTINE\n')
            self.gripper_cmd_pub.publish('start')

    def change_to_passive(self):
        _ = self.change_mode_srv_client('passive')
        self.gripper_mode_pub.publish('passive')
        self.gripper_mode = 'passive'
        rospy.loginfo(self.get_prompt())

    def get_prompt(self):
        #TODO: Find a way to store prompts as attributes to the methods so it can get called like self.menu.prompt
        """Returns the prompt for the current UI screen as a string."""
        if self.current_menu == self.main_menu:
            return '\n\nPASSIVE MODE\n1: position control\n2: sinusoidal routine'
        elif self.current_menu == self.stepper_cal_main_menu:
            return """
            \n\nSTEPPER CALIBRATION MAIN MENU
            LINEAR ACTUATOR RANGE LIMITS MUST BE SET. INCORRECT SETUP COULD BREAK THE GRIPPER OR LINEAR ACTUATOR.\n
            1: Auto calibrate (CAUTION: FULL RANGE OF LINEAR ACTUATOR MUST BE CLEAR OF OBSTRUCTION)
            2: Manual calibrate
            """
        elif self.current_menu == self.stepper_cal_auto_menu:
            return """
            \n\nCalibration will begin soon.\n
            space/enter: EMERGENCY OFF/PASSIVE
            """
        elif self.current_menu == self.stepper_cal_manual_lower_menu:
            return """
            \n\nSet lower limit (limit TOWARDS the motor)
            a: Auto - automatically go to lower limit switch (CAUTION: PATH MUST BE CLEAR)
            j/k) Stepper motor - towards/away from  motor
            u/i) Stepper motor - increase/decrease movement increment (Now: {})
            d/f) Gripper - open/close
            e/r) Gripper - increase/decrease increment (Now: {})
            s) Set lower limit
            i) Show info again
            SPACE OR ENTER: EMERGENCY OFF/PASSIVE
            """
        elif self.current_menu == self.sys_direct_control_menu:
            return """
            \n\nPOSITION CONTROL MODE\n
            d/f : open/close
            e/r : increase/decrease increment (Now: {})
            i: show prompt again
            space/enter: EMERGENCY OFF/PASSIVE MODE/BACK\n
            """.format(self.gripper_pos_increment)
        elif self.current_menu == self.main_menu:
            return """
            \n\nSINUSOIDAL MOTION ROUTINE START\n
            s: start
            space/enter: EMERGENCY OFF/PASSIVE MODE/BACK\n
            """
        else: rospy.log('Error in get_prompt. {} is not a valid mode'.format(self.gripper_mode))


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist: key = sys.stdin.read(1)
    else: key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def main():
    _ = UiNode()

if __name__ == '__main__':
    main()
