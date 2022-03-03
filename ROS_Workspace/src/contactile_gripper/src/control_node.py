#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import time
import rospy
from std_msgs.msg import String,Float32,Int64,Int32
from papillarray_ros_v2.msg import SensorState
from contactile_gripper.msg import Float32List,Int32List
from contactile_gripper.srv import DataRecorder,UIMenu
import srv_clients


#TODO: Need to set the self.stepper_home value.
#TODO: Add logging functionality as shown in gripper node. Get the bag files to save to a different directory. The bag directory.

class ControlNode(object):
    def __init__(self):
        # Publishers
        self.gripper_cmd_pub = rospy.Publisher('Gripper_Cmd', String, queue_size=1)
        self.stepper_cmd_pub = rospy.Publisher('Stepper_Cmd', String, queue_size=1)
        self.routine_running_pub = rospy.Publisher('Routine_Running', String, queue_size=100)

        # Subscribers
        self.gripper_pos_sub = rospy.Subscriber('Gripper_Pos', Int64, self.gripper_pos_callback, queue_size=1, buff_size=1)
        self.gripper_pos = None
        self.stepper_pos_sub = rospy.Subscriber('Stepper_Pos', Int64, self.stepper_pos_callback, queue_size=1, buff_size=1)
        self.stepper_pos = None
        # self.imu_sub = rospy.Subscriber('IMU_Acc', Float32, self.imu_callback, queue_size=1)
        # self.imu_data = {"acc_x":None,"acc_y":None,"acc_z":None}
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_0', SensorState, self.tact_0_callback, queue_size=1)
        self.tact_sensor0 = None
        self.tact_pillar_sub = rospy.Subscriber('/hub_0/sensor_1', SensorState, self.tact_1_callback, queue_size=1)
        self.tact_sensor1 = None
        # Access data in this form: self.tact_sensor0.pillars[0].fX

        # Services
        self.change_mode_srv = rospy.Service('ui_menu_srv', UIMenu, self.menu_srv)
        self.menu = None

        # Setup
        self.routine_bindings = {'menu_routines_grasp_and_release': self.grasp_and_release_routine,
                                 'menu_routines_grasp_forever': self.grasp_forever_routine,
                                 'menu_routines_cable_pull_experiment': self.cable_pull_experiment_routine}
        self.routine_menus = set(self.routine_bindings.keys())
        self.control_function = self.no_routine
        self.stepper_home = None
        self.routine_running = False
        self.routine_stage = 0
        self.grasping = False
        self.stage_start_time = None
        self.recording_data = False

        self.wait_for_sensors()
        self.gripper_goal_pos = self.gripper_pos
        self.gripper_goal_cur = 0

        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 0.5  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)
        self.main_loop()


    ######################## Subscriber and service callbacks ########################
    def menu_srv(self,req):
        """Callback for when the user inputs a command in the ui node."""
        self.check_if_leave_or_enter_routine(req.menu)
        self.menu = req.menu
    def tact_0_callback(self,msg):
        self.tact_sensor0 = msg
    def tact_1_callback(self,msg):
        self.tact_sensor1 = msg
    def gripper_pos_callback(self,msg):
        self.gripper_pos = msg.data
    def stepper_pos_callback(self,msg):
        self.stepper_pos = msg.data
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
            self.grasp()
            #TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")

    def grasp_and_release_routine(self):
        """Grasps and maintains grasp for an amount of time, then releases."""
        self.check_stage()
        if self.routine_stage==0: # Grasp
            self.grasp()
            # TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.grasping: self.stage_complete = True

        elif self.routine_stage==1: # Maintain grasp for some time. No pull.
            self.grasp()
            # TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.stage_timeout(timeout=2): self.stage_complete = True

        elif self.routine_stage==2: # Release grasp.
            self.open()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True

        elif self.routine_stage==3: # Publish flag to let UI node know routine is complete.
            """Need to let the UI node that the routine is complete. """
            #TODO: Publish routine finish flag.


    def cable_pull_experiment_routine(self):
        self.check_stage()
        if self.routine_stage==0: # Start recording
            topic_list = ['/Gripper_Pos','/Gripper_Mode']
            self.record_data(topic_list,file_prefix="cable_pull",record=True)
            self.stepper_home = self.stepper_pos
            self.stage_complete = True

        elif self.routine_stage==1: # Grasp
            self.grasp()
            # TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.grasping: self.stage_complete = True

        elif self.routine_stage==2: # Maintain grasp for some time. No pull.
            self.grasp()
            # TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.stage_timeout(timeout=1): self.stage_complete = True

        elif self.routine_stage==3: # Maintain grasp and pull
            self.grasp()
            if self.cable_check_pull(): self.stage_complete = True

        elif self.routine_stage==4: # Maintain grasp for some time. No pull.
            self.grasp()
            # TODO:
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.stage_timeout(timeout=1): self.stage_complete = True

        elif self.routine_stage==5: # Release grasp.
            self.open()
            if self.stage_timeout(timeout=0.5):
                self.stage_complete = True
                self.record_data(record=False)

        elif self.routine_stage==6: # Return to start position.
            if self.home(): self.stage_complete = True

        elif self.routine_stage==7: # Publish flag to let UI node know routine is complete.
            """Need to let the UI node that the routine is complete. """
            #TODO: Publish routine finish flag.



    ######################## Routine Support ########################
    def grasp(self):
        # TODO:
        if self.grasping_condition:
            self.grasping = True
        else:
            self.grasping = False

    def cable_check_pull(self):
        """Returns True/False for whether or not the check is complete."""
        if self.ending_condition:
            #TODO: Set the stepper to passive/not moving.
            return True
        else:
            return False

    def home(self):
        """Returns True/False for whether or not back at home position."""
        if self.stepper_pos == self.stepper_home:
            return True
        else:
            # TODO
            self.stepper_cmd_pub.publish("Command to return to home position")
            return False


    ######################## State Change Support ########################
    def check_if_leave_or_enter_routine(self,next_menu):
        """Special action taken if entering or leaving a routine."""
        if self.menu not in self.routine_menus and next_menu not in self.routine_menus: # No routine involved.
            return
        elif self.menu not in self.routine_menus and next_menu in self.routine_menus: # Entering a routine.
            self.entering_routine(next_menu)
        elif self.menu in self.routine_menus and next_menu not in self.routine_menus: # Leaving a routine.
            self.exiting_routine()
        else:
            rospy.logerr("Error with ui menu structure.")
            raise Exception

    def entering_routine(self,next_menu):
        self.control_function = self.routine_bindings[next_menu]
        self.routine_running = True
        self.stage_start_time = time.time()

    def exiting_routine(self):
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
    def record_data(self,topic_list=None,file_prefix=" ",record=True):
        #TODO: If already recording and trying to start a new recording, end, start a new one, and log warning.
        # If already not recording, handle that too.
        if record:
            srv_clients.data_recorder_srv_client(topic_list, file_prefix="experiment1", stop=False)
            self.recording_data = True
        elif not record:
            srv_clients.data_recorder_srv_client([], file_prefix=" ", stop=True)
            self.recording_data = False
        else: rospy.logerr("record_data method argument is not boolean. ({})".format(record))

    def wait_for_sensors(self):
        """Wait for all sensors to start publishing data before entering the main control loop."""
        while self.menu is None:
            rospy.loginfo("Waiting for: ui_node")
        while self.stepper_pos is None:
            rospy.loginfo("Waiting for: stepper_node")
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
