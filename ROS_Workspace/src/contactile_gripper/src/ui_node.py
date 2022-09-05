#!/usr/bin/env python2
"""
User interface node to control the system.
"""


import time
import rospy
from std_msgs.msg import String,Float32,Int64,Int32,Bool
import srv_clients
import subprocess, shlex
import sys, select, termios, tty
settings = termios.tcgetattr(sys.stdin)

key_map = {'grip_open':'d',
            'grip_close':'f',
            'grip_increment_inc':'e',
            'grip_increment_dec':'r',
            'complete': 'c',
            'clear_limits': 'a',
            'prompt': 'p',
            'EMO': 'SPACE OR ENTER',
            'EMO_bindings': set({' ','\r','\x1b','\x7f'})
             }

class UiNode(object):

    def __init__(self):
        rospy.init_node('ui_node', anonymous=False, log_level=rospy.INFO)

        # Publishers
        self.gripper_cmd_pub = rospy.Publisher('Gripper_Cmd',String, queue_size=5)

        # Subscribers
        self.routine_running_sub = rospy.Subscriber('Routine_Running', Bool, self.routine_running_callback, queue_size=100)
        self.routine_running = False
        self.gripper_pos_sub = rospy.Subscriber('Gripper_Pos', Int64, self.gripper_pos_callback, queue_size=1, buff_size=1)
        self.gripper_pos = 0
        self.gripper_goal_pos = None

        #Setup
        self.routine_menu_funcs = (self.menu_routines_grasp_and_release,
                                   self.menu_routines_grasp_forever,
                                   self.menu_routines_cable_pull_experiment)
        self.gripper_pos_increment = 30

        self.current_menu = self.menu_main
        self.new_menu_update(self.menu_main)

        self.main_loop_rate = 50  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()


    ######################## Subscriber and service callbacks ########################
    def gripper_pos_callback(self,msg):
        self.gripper_pos = msg.data
    def routine_running_callback(self, msg):
        rospy.logdebug('[routine_running_callback]')
        rospy.loginfo('Routine running: {}'.format(msg.data))
        self.routine_running = msg.data


    ######################## Main loop ########################
    def main_loop(self):
        """Continuously get the key inputs from the user and pass the key to the current menu function."""
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry.
            else:
                self.current_menu(key)
                rospy.logdebug('current_menu: {} key: {}'.format(self.current_menu.__name__,key))
            self.main_loop_rate_obj.sleep()


    ######################## Menus ########################
    """All menu functions accept a key as an argument. When a key is pressed, the key is passed to whatever function
    is set as self.current_menu."""
    def new_menu_update(self,new_menu_func):
        """Changes the current menu function. The new menu function is passed as an argument."""
        rospy.logdebug('[new_menu_update]')
        if new_menu_func in self.routine_menu_funcs:
            self.routine_running = True
        self.current_menu = new_menu_func
        srv_clients.ui_menu_srv_client(self.current_menu.__name__)
        rospy.loginfo(self.current_menu.prompt)

    def menu_main(self,key):
        rospy.logdebug('[menu_main] key: {}'.format(key))
        if key == '1':
            self.new_menu_update(self.menu_sys_direct_control)
        elif key == '2':
            self.new_menu_update(self.menu_routines)
        elif key == '3':
            self.shutdown_entire_system()
    menu_main.prompt = """  
    \n\nMAIN MENU\n
    1: Direct control
    2: Routines
    3: Shutdown System
    """

    def menu_sys_direct_control(self,key):
        rospy.logdebug('[menu_sys_direct_control] key: {}'.format(key))
        if key in key_map['EMO_bindings']: # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive(self.menu_main)
        elif key == key_map['prompt']:
            rospy.loginfo(self.current_menu.prompt)
        elif key in key_map.values():
            self.gripper_dir_control_handle(key)
    menu_sys_direct_control.prompt= """
        \n\nDIRECT CONTROL MODE\n
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'],key_map['prompt'],key_map['EMO'])

    def menu_routines(self,key):
        rospy.logdebug('[menu_routines] key: {}'.format(key))
        if key == '1':
            self.new_menu_update(self.menu_routines_grasp_and_release)
        elif key == '2':
            self.new_menu_update(self.menu_routines_grasp_forever)
        elif key == '3':
            self.new_menu_update(self.menu_routines_cable_pull_experiment)
        elif key in key_map['EMO_bindings']:
            self.new_menu_update(self.menu_main)
    menu_routines.prompt = """  
        \n\nROUTINES MENU\n
        1: Grasp & Release
        2: Grasp Forever
        3: Cable Pull Experiment
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['EMO'])

    routine_running_prompt = """
        \n\nROUTINE RUNNING\n
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['EMO'])
    def menu_routines_grasp_and_release(self,key):
        self.routine_handle(key)
    menu_routines_grasp_and_release.prompt = routine_running_prompt
    def menu_routines_grasp_forever(self, key):
        self.routine_handle(key)
    menu_routines_grasp_forever.prompt = routine_running_prompt
    def menu_routines_cable_pull_experiment(self, key):
        self.routine_handle(key)
    menu_routines_cable_pull_experiment.prompt = routine_running_prompt


    ######################## Supporting methods ########################
    def change_to_passive(self, new_menu_func):
        rospy.logdebug('[change_to_passive]')
        self.new_menu_update(new_menu_func)
        _ = srv_clients.gripper_change_mode_srv_client('off')

    def gripper_dir_control_handle(self,key):
        if key == key_map['grip_open']:
            rospy.loginfo('Gripper open - increment: {}'.format(self.gripper_pos_increment))
            self.gripper_goal_pos = self.gripper_pos - self.gripper_pos_increment
            self.gripper_cmd_pub.publish('position_' + str(self.gripper_goal_pos))
        elif key == key_map['grip_close']:
            rospy.loginfo('Gripper close - increment: {}'.format(self.gripper_pos_increment))
            self.gripper_goal_pos = self.gripper_pos + self.gripper_pos_increment
            self.gripper_cmd_pub.publish('position_' + str(self.gripper_goal_pos))
        elif key == key_map['grip_increment_inc']:
            self.gripper_pos_increment += 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))
        elif key == key_map['grip_increment_dec']:
            self.gripper_pos_increment -= 1
            rospy.loginfo('Gripper increment: {}'.format(self.gripper_pos_increment))

    def routine_handle(self,key):
        """All routines are handled the same. If self.routine_running was set back to false because the routine
        completed or EMO was pressed, go back to the routines menu."""
        try:
            assert self.current_menu in self.routine_menu_funcs
        except:
            rospy.logerr("The current routine menu ({}) needs to be added to self.routine_menu_funcs"
                         "Failure to include may cause the routine to never run because routine_running flag"
                         "never gets set to True.")
        if key in key_map['EMO_bindings'] or not self.routine_running:  # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive(self.menu_routines)

    def shutdown_entire_system(self):
        msg = "rosnode kill -a"
        args = shlex.split(msg)
        _ = subprocess.Popen(args, stderr=subprocess.PIPE, shell=False)

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
