#!/usr/bin/env python
"""
This is an example of the structure of a node that has multiple publishers publishing at different rates and a
subscriber. This examples does not function.
"""

import time
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Int32
from std_msgs.msg import Int64
from papillarray_ros_v2.msg import SensorState
import srv_clients


#TODO: Need to set the self.stepper_home value.

class ControlNode(object):
    def __init__(self):
        # Publishers
        self.gripper_cmd_pub = rospy.Publisher('Gripper_Cmd', String, queue_size=1)
        self.stepper_cmd_pub = rospy.Publisher('Stepper_Cmd', String, queue_size=1)
        self.routine_running_pub = rospy.Publisher('Routine_Running', String, queue_size=100)

        # Subscribers
        self.menu_sub = rospy.Subscriber('UI_Menu', String, self.menu_callback, queue_size=100)
        self.menu = None
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

        # Setup
        self.stepper_home = None
        self.routine_menus = set({'experiment1','experiment2'}) # TODO: Add actual routine method names here.
        self.routine_running = False
        self.routine_stage = 0
        self.grasping = False
        self.stage_start_time = None
        self.recording_data = False

        rospy.on_shutdown(self.shutdown_function)
        self.main_loop_rate = 0.5  # Hz
        self.main_loop_rate_obj = rospy.Rate(self.main_loop_rate)

        self.wait_for_sensors()
        self.gripper_goal_pos = self.gripper_pos
        self.gripper_goal_cur = 0

        self.main_loop()


    ######################## Subscriber callbacks ########################
    def menu_callback(self,msg):
        """Callback for when the user inputs a command in the ui node."""
        self.check_if_routine(msg.data)
        self.menu = msg.data
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

    ######################## Main control loop ########################
    def main_loop(self):
        """Publishes motor commands to the motor depending on the current operating mode parameters."""
        while not rospy.is_shutdown():
            # Execute control function for this cycle.
            self.grasp_and_pull_routine()
            # How will the function know that it is finished? Need to signal to gripper that it is finished when done.
            # A series of flags to mark different stages of the routine.

            # rospy.loginfo("Tactile Sensor 0 P0 fX: {}".format(self.tact_sensor0.pillars[0].fX))
            # rospy.loginfo("UI Menu: {}".format(self.menu))
            # rospy.loginfo("Gripper Pos: {}".format(self.gripper_pos))
            # rospy.loginfo("Stepper Pos: {}".format(self.stepper_pos))

            self.main_loop_rate_obj.sleep()


    ######################## Routine Main Functions ########################
    def grasp_and_pull_routine(self):
        self.check_stage()
        if self.routine_stage==0: # Start recording
            self.record_data(record=True)
            self.stage_complete = True

        elif self.routine_stage==1: # Grasp
            self.grasp()
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.grasping: self.stage_complete = True

        elif self.routine_stage==2: # Maintain grasp for some time. No pull.
            self.grasp()
            self.stepper_cmd_pub.publish("some command for zero speed.")
            if self.stage_timeout(timeout=1): self.stage_complete = True

        elif self.routine_stage==3: # Maintain grasp and pull
            self.grasp()
            if self.cable_check_pull(): self.stage_complete = True

        elif self.routine_stage==4: # Maintain grasp for some time. No pull.
            self.grasp()
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
        if self.ending_condition:
            #TODO: Set the stepper to passive/not moving.
            return True
        else:
            return False

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
            # self.stepper_home
            # TODO
            self.stepper_cmd_pub.publish("Command to return to home position")
            return False

    ######################## State Change Support ########################
    def check_if_routine(self,next_menu):
        """Special action taken if entering or leaving a routine."""
        if self.menu not in self.routine_menus and next_menu not in self.routine_menus: # No routine involved.
            return
        elif self.menu not in self.routine_menus and next_menu in self.routine_menus: # Entering a routine.
            self.entering_routine()
        elif self.menu in self.routine_menus and next_menu not in self.routine_menus: # Leaving a routine.
            self.exiting_routine()
        else:
            rospy.logerr("Error with ui menu structure.")
            raise Exception

    def entering_routine(self):
        self.routine_running = True
        self.stage_start_time = time.time()

    def exiting_routine(self):
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
    def record_data(self,record=True):
        #TODO: If already recording and trying to start a new recording, end, start a new one, and log warning.
        # If already not recording, handle that too.
        if record:
            # TODO: Start recording the data
            self.recording_data = False
        elif not record:
            # TODO: Stop recording the data
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
        """This function runs when the ROS node is shutdown for some reason.
        It might be useful to publish messages to other nodes. Perhaps if this node crashes it should trigger and EMO."""
        pass

def main():
    rospy.init_node('control_node',anonymous=False,log_level=rospy.INFO)
    _ = ControlNode()

if __name__ == '__main__':
    main()
