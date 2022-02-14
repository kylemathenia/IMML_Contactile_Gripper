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

key_map = {'grip_open':'d',
            'grip_close':'f',
            'grip_increment_inc':'e',
            'grip_increment_dec':'r',
            'step_open':'j',
            'step_close':'k',
            'step_increment_inc':'u',
            'step_increment_dec':'i',
            'set_upper_lim': 'q',
            'set_lower_lim': 'w',
            'complete': 'c',
            'prompt': 'p',
            'EMO': 'SPACE OR ENTER',
            'EMO_bindings': set({' ','\r','\x1b','\x7f'})
             }

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
        self.stepper_upper_lim = None
        self.stepper_lower_lim = None

        self.current_menu = self.stepper_cal_main_menu
        rospy.loginfo(self.current_menu.prompt)
        self.main_loop()

    def main_loop(self):
        """Continuously get the key inputs from the user and do something."""
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry.
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

    main_menu.prompt = """  
    \n\nSTEPPER CALIBRATION MAIN MENU
    LINEAR ACTUATOR RANGE LIMITS MUST BE SET. INCORRECT SETUP COULD BREAK THE GRIPPER OR LINEAR ACTUATOR.\n
    1: Auto calibrate (CAUTION: FULL RANGE OF LINEAR ACTUATOR MUST BE CLEAR OF OBSTRUCTION)
    2: Manual calibrate
    """

    def sys_direct_control_menu(self,key):
        if key in key_map['EMO_bindings']: # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive()
        elif key in key_map:
            self.dir_control_handle(key)

    sys_direct_control_menu.prompt= """
        \n\nPOSITION CONTROL MODE\n
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper open/close
        {}/{}: Stepper increase/decrease increment
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_open'], key_map['step_close'],
                   key_map['grip_increment_inc'],key_map['grip_increment_dec'],key_map['prompt'],key_map['EMO'])

    def step_cal_main_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        pass

    step_cal_main_menu.prompt = """
        \n\nSTEPPER CALIBRATION MAIN MENU
        LINEAR ACTUATOR RANGE LIMITS MUST BE SET. INCORRECT SETUP COULD BREAK THE GRIPPER OR LINEAR ACTUATOR.\n
        1: Auto calibrate (CAUTION: FULL RANGE OF LINEAR ACTUATOR MUST BE CLEAR OF OBSTRUCTION)
        2: Manual calibrate
        """

    def step_cal_auto_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        pass

    step_cal_auto_menu.prompt = """
        \n\nCalibration will begin soon.\n
        {}: EMERGENCY OFF/PASSIVE.
        """.format(key_map['EMO'])

    def step_cal_manual_menu(self,key):
        """Begin stepper calibration. Choose automatic or manual."""
        if key in key_map['EMO_bindings']:  # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive()
        elif key == key_map['set_lower_lim'] or key_map['set_upper_lim'] or key_map['set_upper_lim']:
            self.set_limit_handle(key)
        elif key in key_map:
            self.dir_control_handle(key)

    step_cal_manual_menu.prompt = """
        \n\nSET STEPPER LIMITS
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper open/close
        {}/{}: Stepper increase/decrease increment
        {}/{}: Set upper/lower stepper limit (AWAY/TOWARDS the motor)
        {}: Complete
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_open'], key_map['step_close'],
                   key_map['grip_increment_inc'],key_map['grip_increment_dec'],key_map['set_upper_lim'],
                   key_map['set_lower_lim'],key_map['complete'],key_map['prompt'],key_map['EMO'])


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

    def dir_control_handle(self,key):
        if key == key_map['grip_open']:
            rospy.loginfo('Gripper open - increment: {}'.format(self.gripper_pos_increment))
            self.gripper_cmd_pub.publish(str(-self.gripper_pos_increment))
        elif key == key_map['grip_close']:
            rospy.loginfo('Gripper close - increment: {}'.format(self.gripper_pos_increment))
            self.gripper_cmd_pub.publish(str(self.gripper_pos_increment))
        elif key == key_map['grip_increment_inc']:
            self.gripper_pos_increment += 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['grip_increment_dec']:
            self.gripper_pos_increment -= 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['step_open']:
            rospy.loginfo('Stepper open - increment: {}'.format(self.stepper_pos_increment))
            self.gripper_cmd_pub.publish(str(-self.stepper_pos_increment))
        elif key == key_map['step_close']:
            rospy.loginfo('Stepper close - increment: {}'.format(self.stepper_pos_increment))
            self.gripper_cmd_pub.publish(str(self.stepper_pos_increment))
        elif key == key_map['step_increment_inc']:
            self.gripper_pos_increment += 1
            rospy.loginfo('Stepper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['step_increment_dec']:
            self.gripper_pos_increment -= 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['prompt']:
            rospy.loginfo(self.current_menu.prompt)

    def set_limit_handle(self,key):
        #TODO: Not complete. log instead of print etc.
        # pos = get pos()
        if not self._lim_valid(key,pos):
            print('invailid')
        elif key == key_map['set_lower_lim']:
            self.stepper_lower_lim = pos
            print('Lower limit set to ....')
        elif key_map['set_upper_lim']:
            self.stepper_upper_lim = pos
            print('Upper limit set to ....')
        # if both limits are set, change menu to the next.

    def _lim_valid(self,key,pos):
        if key == key_map['set_lower_lim']:
            pass
        elif key == key_map['set_upper_lim']:
            pass


    def get_prompt(self):
        """Returns the prompt for the current UI screen as a string."""
        if self.current_menu == self.main_menu:
            return '\n\nPASSIVE MODE\n1: position control\n2: sinusoidal routine'
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


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist: key = sys.stdin.read(1)
    else: key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key


def test():
    # Check to make sure no duplicate/conflicting key values.
    set(key_map.values())

def main():
    _ = UiNode()

if __name__ == '__main__':
    main()
