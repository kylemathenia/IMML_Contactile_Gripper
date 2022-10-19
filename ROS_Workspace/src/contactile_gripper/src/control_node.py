#!/usr/bin/env python2


import time
import rospy
from std_msgs.msg import String,Float32,Int64,Int32,Bool
from papillarray_ros_v2.msg import SensorState
from contactile_gripper.msg import Float32List,Int32List
from contactile_gripper.srv import *
import srv_clients



class ControlNode(object):
    def __init__(self):
        # Publishers
        self.gripper_cmd_pub = rospy.Publisher('Gripper_Cmd', String, queue_size=1)
        self.routine_running_pub = rospy.Publisher('Routine_Running', Bool, queue_size=100)

        # Subscribers
        self.gripper_pos_sub = rospy.Subscriber('Gripper_Pos', Int64, self.gripper_pos_callback, queue_size=1)
        self.gripper_pos = None
        # self.imu_sub = rospy.Subscriber('IMU_Acc', Float32, self.imu_callback, queue_size=1)
        # self.imu_data = {"acc_x":None,"acc_y":None,"acc_z":None}
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_1', SensorState, self.tact_1_callback, queue_size=1)
        self.tact_sensor1 = None
        # Access data in this form: self.tact_sensor0.pillars[0].fX

        # Services
        self.change_mode_srv = rospy.Service('ui_menu_srv', UIMenu, self.menu_srv)
        self.control_function = self.no_routine

        # Setup
        self.routine_bindings = {'menu_routines_grasp_and_release': self.grasp_and_release_routine,
                                 'menu_routines_grasp_forever': self.grasp_forever_routine,
                                 'menu_routines_cable_pull_experiment': self.cable_pull_experiment_routine}
        self.routine_menus = set(self.routine_bindings.keys())
        self.routine_running = False
        self.routine_stage = 0
        self.grasping = False
        self.stage_start_time = None
        self.recording_data = False
        self.gripper_goal_pos = None
        self.stage_complete = False
        self.goal_grasp_force = 5 # Newtons
        self.p_gain = 2
        self.d_gain = .2
        self.i_gain = .1
        self.total_error = 0
        self.previous_error = 0

        self.wait_for_sensors()
        self.gripper_goal_pos = self.gripper_pos
        self.gripper_goal_cur = 18

        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 30  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()


    ######################## Subscriber and service callbacks ########################
    def menu_srv(self,req):
        """Callback for when the user inputs a command in the ui node. req.menu is a string of the ui menu function."""

        #TODO put a control in place to make sure the contactile sensor is publishing non-zero data. Maybe never let it enter a routine
        # mode if that is the case
        rospy.logdebug('[menu_srv] req: {}'.format(req))
        self.check_if_leave_or_enter_routine(req.menu)
        if req.menu in self.routine_menus:
            self.control_function = self.routine_bindings[req.menu]
        else:
            self.control_function = self.no_routine
        return UIMenuResponse()
    def tact_0_callback(self,msg):
        self.tact_sensor0 = msg
        # rospy.loginfo("Global Z force: {} (N)".format(self.tact_sensor0.gfZ))
    def tact_1_callback(self,msg):
        self.tact_sensor1 = msg
    def gripper_pos_callback(self,msg):
        self.gripper_pos = msg.data
    def imu_callback(self,msg):
        pass

    ######################## Main loop ########################
    def main_loop(self):
        """Publishes motor commands to the motor depending on the current operating mode parameters."""
        while not rospy.is_shutdown():
            self.control_function()
            self.main_loop_rate_obj.sleep()

    ######################## Control/Routine Functions ########################
    def no_routine(self):
        """Don't publish commands if the UI is not in a menu for running a routine."""
        pass

    def grasp_forever_routine(self):
        self.check_stage()
        if self.routine_stage == 0:  # Grasp
            srv_success = srv_clients.bias_request_srv_client()
            self.stage_complete = True
        if self.routine_stage == 1:  # Grasp
            self.grasp()


    def grasp_and_release_routine(self):
        """Grasps and maintains grasp for an amount of time, then releases."""
        self.check_stage()
        if self.routine_stage == 0:  # Setup
            srv_success = srv_clients.bias_request_srv_client()
            file_prefix_ans = raw_input("Enter the filename for data:\n")
            topic_list = ['/hub_0/sensor_0', '/hub_0/sensor_1']
            self.record_data(topic_list, file_prefix=file_prefix_ans, record=True)
            self.stage_complete = True

        elif self.routine_stage == 1:  # Go to starting position.
            self.open()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_start_pos = self.gripper_pos + 1300
                self.gripper_goal_cur = 4

        elif self.routine_stage == 2:  # Go to starting position.
            self.go_to_start()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_goal_cur = 4

        elif self.routine_stage == 3:  # Wait for data to start recording.
            if self.stage_timeout(timeout=0.25):
                self.stage_complete = True

        elif self.routine_stage == 4:  # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=2):
                self.stage_complete = True

        elif self.routine_stage == 5:  # Go to starting position.
            self.go_to_start()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_goal_cur = 12

        elif self.routine_stage == 6:  # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=2):
                self.stage_complete = True

        elif self.routine_stage == 7:  # Go to starting position.
            self.go_to_start()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_goal_cur = 24

        elif self.routine_stage == 8:  # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=2):
                self.stage_complete = True

        elif self.routine_stage == 9:  # Go to starting position.
            self.go_to_start()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_goal_cur = 36

        elif self.routine_stage == 10:  # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=2):
                self.stage_complete = True

        elif self.routine_stage == 11:  # Release grasp.
            self.open()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True

        elif self.routine_stage == 12:  # Finish
            """Need to let the UI node that the routine is complete. """
            self.record_data(record=False)
            self.routine_running_pub.publish(False)
            self.stage_complete = True




    def grasp_and_release_routine2(self):
        """Grasps and maintains grasp for an amount of time, then releases."""
        self.check_stage()
        if self.routine_stage==0: # Setup
            srv_success = srv_clients.bias_request_srv_client()
            # topic_list = ['/Gripper_Pos', '/hub_0/sensor_0', '/hub_0/sensor_1']
            file_prefix_ans = raw_input("Enter the filename for data:\n")
            topic_list = ['/hub_0/sensor_0', '/hub_0/sensor_1']
            self.record_data(topic_list, file_prefix=file_prefix_ans, record=True)
            self.stage_complete = True

        elif self.routine_stage==1: # Wait for data to start recording.
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.gripper_goal_cur = 4

        elif self.routine_stage==2: # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=3):
                self.stage_complete = True
                self.gripper_goal_cur = 20

        elif self.routine_stage==3: # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=3):
                self.stage_complete = True
                self.gripper_goal_cur = 30

        elif self.routine_stage==4: # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=3):
                self.stage_complete = True
                self.gripper_goal_cur = 45

        elif self.routine_stage==5: # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=3):
                self.stage_complete = True
                self.gripper_goal_cur = 65

        elif self.routine_stage==6: # Maintain grasp for some time.
            self.grasp()
            if self.stage_timeout(timeout=3):
                self.stage_complete = True

        elif self.routine_stage==7: # Release grasp.
            self.open()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True

        elif self.routine_stage==8: # Finish
            """Need to let the UI node that the routine is complete. """
            self.record_data(record=False)
            self.routine_running_pub.publish(False)
            self.stage_complete = True



    def cable_pull_experiment_routine(self):
        pass


    ######################## Routine Support ########################
    def grasp(self):
        """Close the gripper until the global z force is at a certain level."""
        global_z_force = (self.tact_sensor0.gfZ + self.tact_sensor1.gfZ) / 2
        rospy.loginfo("z force: {}".format(global_z_force))
        self.check_if_grasping()
        if not self.grasping: # Not in contact.
            self.no_contact_close()
        elif self.over_z_force_limit(): # Overshooting.
            self.over_z_force_limit_control()
        else: # Apply a constant torque
            self.gripper_cmd_pub.publish('current_' + str(self.gripper_goal_cur))

    def check_if_grasping(self):
        # If changing a lot in the positive direction.
        if self.tact_sensor0.gfZ > 1:
            self.grasping = True
        else:
            self.grasping = False

    def no_contact_close(self):
        self.gripper_cmd_pub.publish('current_' + str(10))

    def over_z_force_limit(self):
        """Returns T/F for if the z force is over a max threshold."""
        if self.tact_sensor0.gfZ > 30:
            return True
        else:
            return False

    def over_z_force_limit_control(self):
        self.gripper_cmd_pub.publish('current_' + str(0))


    def grasp_feedback(self):
        """Close the gripper unitl the global z force is at a certain level."""
        global_z_force = (self.tact_sensor0.gfZ + self.tact_sensor1.gfZ)/2
        rospy.loginfo("z force: {}".format(global_z_force))
        if global_z_force > 1:
            self.grasping = True
        else:
            self.grasping = False
        if not self.grasping: # Not in contact. Move faster than PID control.
            pos_change = 10
        else: # PID control
            error = self.goal_grasp_force - global_z_force
            change_in_error = error - self.previous_error
            self.total_error += error
            pos_change = (error*self.p_gain) + (change_in_error*self.d_gain) + (self.total_error*self.i_gain)
        self.gripper_goal_pos = self.gripper_pos + int(pos_change)
        self.gripper_cmd_pub.publish('position_' + str(self.gripper_goal_pos))

    def open(self):
        self.gripper_goal_pos = 10 # Set to a really small position to open all the way.
        self.gripper_cmd_pub.publish('position_' + str(self.gripper_goal_pos))

    def go_to_start(self):
        self.gripper_cmd_pub.publish('position_' + str(self.gripper_start_pos))


    ######################## State Change Support #########################
    def check_if_leave_or_enter_routine(self,next_menu):
        """Special action taken if entering or leaving a routine."""
        routine_control_functions = self.routine_bindings.values()
        if self.control_function not in routine_control_functions and next_menu not in self.routine_menus: # No routine involved.
            return
        elif self.control_function not in routine_control_functions and next_menu in self.routine_menus: # Entering a routine.
            self.entering_routine(next_menu)
        elif self.control_function in routine_control_functions and next_menu not in self.routine_menus: # Leaving a routine.
            self.exiting_routine()
        else:
            rospy.logerr("Error with ui menu structure.")
            raise Exception

    def entering_routine(self,next_menu):
        self.routine_running_pub.publish(True)
        self.control_function = self.routine_bindings[next_menu]
        self.routine_running = True
        self.stage_start_time = time.time()

    def exiting_routine(self):
        self.routine_running_pub.publish(False)
        self.control_function = self.no_routine
        self.routine_running = False
        self.routine_stage = 0
        self.grasping = False
        self.record_data(record=False)

    def check_stage(self):
        if self.stage_complete:
            self.routine_stage += 1
            self.stage_start_time = time.time()
            self.stage_complete = False

    def stage_timeout(self,timeout=1):
        """Returns True/False for whether or not the current stage has exceeded the timeout value (sec)"""
        elapsed_time = time.time() - self.stage_start_time
        if elapsed_time > timeout: return True
        else: return False

    ######################## Other ########################
    def record_data(self,topic_list=None,file_prefix="experiment1",record=True):
        if record:
            srv_clients.data_recorder_srv_client(topic_list, file_prefix=file_prefix, stop=False)
            self.recording_data = True
        elif not record:
            srv_clients.data_recorder_srv_client([], file_prefix=" ", stop=True)
            self.recording_data = False
        else: rospy.logerr("record_data method argument is not boolean. ({})".format(record))

    def wait_for_sensors(self):
        """Wait for all sensors to start publishing data before entering the main control loop."""
        # while self.stepper_pos is None:
        #     rospy.loginfo("Waiting for: stepper_node")
        # while self.imu_acc_x is None:
        #     rospy.loginfo("Waiting for: imu_node")
        while self.gripper_pos is None:
            rospy.loginfo("Waiting for: gripper_node")
        while self.tact_sensor0 is None:
            rospy.loginfo("Waiting for: papillarray node")

    def shutdown_function(self):
        self.record_data(record=False)

def main():
    rospy.init_node('control_node',anonymous=False,log_level=rospy.INFO)
    _ = ControlNode()

if __name__ == '__main__':
    main()
