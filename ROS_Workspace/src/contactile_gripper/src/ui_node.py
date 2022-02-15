#!/usr/bin/env python
"""
User interface node to control the system.
"""

import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Int32
from contactile_gripper.srv import *
import sys, select, termios, tty
settings = termios.tcgetattr(sys.stdin)

#TODO: Need to implement services for changing stepper motor limit values directly with the stepper motor.
#TODO: Need to implement services for changing the stepper motor to passive as well.

key_map = {'grip_open':'d',
            'grip_close':'f',
            'grip_increment_inc':'e',
            'grip_increment_dec':'r',
            'step_up':'j',
            'step_down':'k',
            'step_increment_inc':'u',
            'step_increment_dec':'i',
            'set_upper_lim': 'q',
            'set_lower_lim': 'w',
            'complete': 'c',
            'clear_limits': 'a',
            'prompt': 'p',
            'EMO': 'SPACE OR ENTER',
            'EMO_bindings': set({' ','\r','\x1b','\x7f'})
             }

class UiNode(object):
    def __init__(self):
        # Publishers
        self.menu_pub = rospy.Publisher('UI_Menu', String, queue_size=100, latch=True)
        self.ui_gripper_cmd_pub = rospy.Publisher('UI_Gripper_Cmd',String, queue_size=5)
        self.ui_stepper_cmd_pub = rospy.Publisher('UI_Stepper_Cmd',String, queue_size=5)

        # Subscribers
        self.routine_running_sub = rospy.Subscriber('Routine_Running', String, self.routine_running_callback, queue_size=100)
        self.routine_running = 'No'
        
        #Setup
        self.gripper_pos_increment = 5
        self.stepper_pos_increment = 100
        self.stepper_upper_lim = None
        self.stepper_lower_lim = None

        self.current_menu = self.menu_step_cal
        self.new_menu_update()

        self.main_loop()

    def main_loop(self):
        """Continuously get the key inputs from the user and pass the key to the current menu method."""
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry.
            else: self.current_menu(key)


    ############ Menus ############
    def menu_main(self,key):
        if key == '1':
            self.current_menu = self.menu_sys_direct_control
        elif key == '2':
            self.current_menu = self.menu_routines
        elif key == '3':
            self.current_menu = self.menu_step_cal
            
        if key == '1' or key == '2' or key == '3': self.new_menu_update()
    menu_main.prompt = """  
    \n\nMAIN MENU\n
    1: Direct control
    2: Routines
    3: Calibrate
    """

    def menu_sys_direct_control(self,key):
        if key in key_map['EMO_bindings']: # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive()
            self.current_menu = self.menu_main
            self.new_menu_update()
        elif key in key_map.values():
            self.dir_control_handle(key)
    menu_sys_direct_control.prompt= """
        \n\nPOSITION CONTROL MODE\n
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper up/down
        {}/{}: Stepper increase/decrease increment
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_up'], key_map['step_down'],
                   key_map['step_increment_inc'],key_map['step_increment_dec'],key_map['prompt'],key_map['EMO'])

    def menu_routines(self,key):
        #TODO: Make routines menu.
        pass
    menu_routines.prompt = None

    def menu_step_cal(self,key):
        if key in key_map['EMO_bindings']:  # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive()
        elif key==key_map['set_lower_lim'] or key==key_map['set_upper_lim'] or key==key_map['clear_limits'] or key==key_map['complete']:
            self.set_limit_handle(key)
        elif key in key_map.values():
            self.dir_control_handle(key)
    menu_step_cal.prompt = """
        \n\nSET STEPPER LIMITS
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper up/down
        {}/{}: Stepper increase/decrease increment
        {}/{}: Set upper/lower stepper limit (AWAY/TOWARDS the motor) 
        {}: Complete
        {}: Clear limits
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_up'], key_map['step_down'],
                   key_map['step_increment_inc'],key_map['step_increment_dec'],key_map['set_upper_lim'],
                   key_map['set_lower_lim'],key_map['complete'],key_map['clear_limits'],key_map['prompt'],key_map['EMO'])


    ############ Supporting methods ############
    def new_menu_update(self):
        rospy.loginfo(self.current_menu.prompt)
        self.menu_pub.publish(self.current_menu.__name__)

    def change_to_passive(self):
        pass  # TODO: Change both stepper and gripper to passive.
        # _ = self.change_mode_srv_client('passive')

    def routine_running_callback(self, msg):
        self.routine_running = msg.data

    def dir_control_handle(self,key):
        if key == key_map['grip_open']:
            rospy.loginfo('Gripper open - increment: {}'.format(self.gripper_pos_increment))
            self.ui_gripper_cmd_pub.publish(str(-self.gripper_pos_increment))
        elif key == key_map['grip_close']:
            rospy.loginfo('Gripper close - increment: {}'.format(self.gripper_pos_increment))
            self.ui_gripper_cmd_pub.publish(str(self.gripper_pos_increment))
        elif key == key_map['grip_increment_inc']:
            self.gripper_pos_increment += 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['grip_increment_dec']:
            self.gripper_pos_increment -= 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['step_up']:
            rospy.loginfo('Stepper open - increment: {}'.format(self.stepper_pos_increment))
            self.ui_stepper_cmd_pub.publish(str(-self.stepper_pos_increment))
        elif key == key_map['step_down']:
            rospy.loginfo('Stepper close - increment: {}'.format(self.stepper_pos_increment))
            self.ui_stepper_cmd_pub.publish(str(self.stepper_pos_increment))
        elif key == key_map['step_increment_inc']:
            self.stepper_pos_increment += 1
            rospy.loginfo('Stepper increment: {}'.format(self.stepper_pos_increment))
        elif key == key_map['step_increment_dec']:
            self.stepper_pos_increment -= 1
            rospy.loginfo('Stepper increment: {}'.format(self.stepper_pos_increment))
        elif key == key_map['prompt']:
            rospy.loginfo(self.current_menu.prompt)

    def set_limit_handle(self,key):
        if key == key_map['complete'] and self.stepper_lower_lim is not None and self.stepper_upper_lim is not None:
            rospy.loginfo("\nUpper limit: {}, Lower limit: {}".format(self.stepper_upper_lim,self.stepper_lower_lim))
            self.current_menu = self.menu_main
            self.new_menu_update()
        elif key == key_map['complete']:
            rospy.loginfo("Limits not set. Lower: {}, Upper: {}".format(self.stepper_lower_lim,self.stepper_upper_lim))
        elif key == key_map['set_lower_lim']:
            self.stepper_lower_lim = 80
            rospy.loginfo("Lower limit set to: {}".format(self.stepper_lower_lim))
            # TODO: Make service calls to the stepper node.
        elif key == key_map['set_upper_lim']:
            self.stepper_upper_lim = 90
            rospy.loginfo("Upper limit set to: {}".format(self.stepper_upper_lim))
            # TODO: Make service calls to the stepper node.
        elif key == key_map['clear_limits']:
            self.stepper_upper_lim = None
            self.stepper_lower_lim = None
            rospy.loginfo("\nUpper limit: {}, Lower limit: {}".format(self.stepper_upper_lim,self.stepper_lower_lim))
            # TODO: Make service calls to the stepper node.

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
    rospy.init_node('ui_node', anonymous=False, log_level=rospy.DEBUG)
    _ = UiNode()

if __name__ == '__main__':
    main()
