#!/usr/bin/env python
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
            'step_up':'k',
            'step_down':'j',
            'step_increment_inc':'u',
            'step_increment_dec':'i',
            'set_upper_lim': 'w',
            'set_lower_lim': 'q',
            'complete': 'c',
            'clear_limits': 'a',
            'prompt': 'p',
            'EMO': 'SPACE OR ENTER',
            'EMO_bindings': set({' ','\r','\x1b','\x7f'})
             }

class UiNode(object):

    def __init__(self):
        # Publishers
        self.gripper_cmd_pub = rospy.Publisher('Gripper_Cmd',String, queue_size=5)
        self.stepper_cmd_pub = rospy.Publisher('Stepper_Cmd',String, queue_size=5)

        # Subscribers
        self.routine_running_sub = rospy.Subscriber('Routine_Running', Bool, self.routine_running_callback, queue_size=100)
        self.routine_running = False
        self.gripper_pos_sub = rospy.Subscriber('Gripper_Pos', Int64, self.gripper_pos_callback, queue_size=1, buff_size=1)
        self.gripper_pos = 0
        self.gripper_goal_pos = None
        self.stepper_pos_sub = rospy.Subscriber('Stepper_Pos', Int64, self.stepper_pos_callback, queue_size=1, buff_size=1)
        self.stepper_pos = 0
        self.stepper_goal_pos = None

        #Setup
        self.routine_menu_funcs = (self.menu_routines_grasp_and_release,
                                   self.menu_routines_grasp_forever,
                                   self.menu_routines_cable_pull_experiment)
        self.gripper_pos_increment = 30
        self.stepper_pos_increment = 50
        self.stepper_upper_lim = None
        self.stepper_lower_lim = None

        self.current_menu = None
        self.new_menu_update(self.menu_step_cal)

        self.main_loop()


    ######################## Subscriber and service callbacks ########################
    def gripper_pos_callback(self,msg):
        self.gripper_pos = msg.data
    def stepper_pos_callback(self,msg):
        self.stepper_pos = msg.data
    def routine_running_callback(self, msg):
        rospy.logdebug('[routine_running_callback]')
        rospy.loginfo('Routine running: {}'.format(msg.data))
        self.routine_running = msg.data


    ######################## Main loop ########################
    def main_loop(self):
        """Continuously get the key inputs from the user and pass the key to the current menu method."""
        while not rospy.is_shutdown():
            key = getKey()
            if key == '': pass # No entry.
            else:
                self.current_menu(key)
                rospy.logdebug('current_menu: {} key: {}'.format(self.current_menu.__name__,key))


    ######################## Menus ########################
    def menu_main(self,key):
        rospy.logdebug('[menu_main] key: {}'.format(key))
        if key == '1':
            self.new_menu_update(self.menu_sys_direct_control)
        elif key == '2':
            self.new_menu_update(self.menu_routines)
        elif key == '3':
            self.new_menu_update(self.menu_step_cal)
        elif key == '4':
            self.shutdown_entire_system()

    menu_main.prompt = """  
    \n\nMAIN MENU\n
    1: Direct control
    2: Routines
    3: Calibrate
    4: Shutdown System
    """

    def menu_sys_direct_control(self,key):
        rospy.logdebug('[menu_sys_direct_control] key: {}'.format(key))
        if key in key_map['EMO_bindings']: # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive(self.menu_main)
        elif key in key_map.values():
            self.dir_control_handle(key)
    menu_sys_direct_control.prompt= """
        \n\nDIRECT CONTROL MODE\n
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper up/down
        {}/{}: Stepper increase/decrease increment
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_up'], key_map['step_down'],
                   key_map['step_increment_inc'],key_map['step_increment_dec'],key_map['prompt'],key_map['EMO'])

    def menu_step_cal(self,key):
        rospy.logdebug('[menu_step_cal] key: {}'.format(key))
        if key in key_map['EMO_bindings']:  # EMERGENCY OFF. Space, enter, backspace, or esc.
            self.change_to_passive(self.menu_main)
        elif key==key_map['set_lower_lim'] or key==key_map['set_upper_lim'] or key==key_map['clear_limits'] or key==key_map['complete']:
            self.set_limit_handle(key)
        elif key in key_map.values():
            self.dir_control_handle(key)
    menu_step_cal.prompt = """
        \n\nSET STEPPER LIMITS
        {}/{}: Gripper open/close
        {}/{}: Gripper increase/decrease increment
        {}/{}: Stepper down/up
        {}/{}: Stepper increase/decrease increment
        {}/{}: Set lower/upper stepper limit (AWAY/TOWARDS the motor) 
        {}: Complete
        {}: Clear limits
        {}: Show prompt again
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['grip_open'], key_map['grip_close'],key_map['grip_increment_inc'],
                   key_map['grip_increment_dec'], key_map['step_up'], key_map['step_down'],
                   key_map['step_increment_inc'],key_map['step_increment_dec'],key_map['set_upper_lim'],
                   key_map['set_lower_lim'],key_map['complete'],key_map['clear_limits'],key_map['prompt'],key_map['EMO'])


    ######################## Routine Menus ########################
    routine_running_prompt = """
        \n\nGrasp & Release Routine\n
        {}: EMERGENCY OFF/PASSIVE MODE/BACK\n
        """.format(key_map['EMO'])

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
    def new_menu_update(self,new_menu_func):
        rospy.logdebug('[new_menu_update]')
        if new_menu_func in self.routine_menu_funcs:
            self.routine_running = True
        self.current_menu = new_menu_func
        srv_clients.ui_menu_srv_client(self.current_menu.__name__)
        rospy.loginfo(self.current_menu.prompt)

    def change_to_passive(self, new_menu_func):
        rospy.logdebug('[change_to_passive]')
        self.new_menu_update(new_menu_func)
        _ = srv_clients.gripper_change_mode_srv_client('off')
        _ = srv_clients.stepper_off_srv_client('off')

    def dir_control_handle(self,key):
        rospy.logdebug('[dir_control_handle] key: {}'.format(key))
        self.gripper_dir_control_handle(key)
        self.stepper_dir_control_handle(key)
        if key == key_map['prompt']:
            rospy.loginfo(self.current_menu.prompt)

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


    def stepper_dir_control_handle(self, key):
        if key == key_map['step_down']:
            rospy.loginfo('Stepper down - increment: {}'.format(self.stepper_pos_increment))
            self.stepper_goal_pos = self.stepper_pos - self.stepper_pos_increment
            self.stepper_cmd_pub.publish('position_' + str(self.stepper_goal_pos))
        elif key == key_map['step_up']:
            rospy.loginfo('Stepper up - increment: {}'.format(self.stepper_pos_increment))
            self.stepper_goal_pos = self.stepper_pos + self.stepper_pos_increment
            self.stepper_cmd_pub.publish('position_' + str(self.stepper_goal_pos))
        elif key == key_map['step_increment_inc']:
            self.stepper_pos_increment += 10
            rospy.loginfo('Stepper increment: {}'.format(self.stepper_pos_increment))
        elif key == key_map['step_increment_dec']:
            self.stepper_pos_increment -= 10
            rospy.loginfo('Stepper increment: {}'.format(self.stepper_pos_increment))


    def set_limit_handle(self,key):
        rospy.logdebug('[set_limit_handle] key: {}'.format(key))
        if key == key_map['complete']:
            rospy.loginfo("\nUpper limit: {}, Lower limit: {}".format(self.stepper_upper_lim,self.stepper_lower_lim))
            self.change_to_passive(self.menu_main)
        elif key == key_map['set_lower_lim']:
            self.stepper_lower_lim = srv_clients.stepper_set_limit_srv_client('lower','set')
            rospy.loginfo("Lower limit set to: {}".format(self.stepper_lower_lim))
        elif key == key_map['set_upper_lim']:
            self.stepper_upper_lim = srv_clients.stepper_set_limit_srv_client('upper','set')
            rospy.loginfo("Upper limit set to: {}".format(self.stepper_upper_lim))
        elif key == key_map['clear_limits']:
            self.stepper_upper_lim = srv_clients.stepper_set_limit_srv_client('none', 'clear')
            self.stepper_upper_lim = None
            self.stepper_lower_lim = None
            rospy.loginfo("\nUpper limit: {}, Lower limit: {}\n".format(self.stepper_upper_lim,self.stepper_lower_lim))

    def routine_handle(self,key):
        """All specific routines are handled the same. Unique menus are needed to communicate to the control node
        which routine to run."""
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
    rospy.init_node('ui_node', anonymous=False, log_level=rospy.INFO)
    _ = UiNode()

if __name__ == '__main__':
    main()
