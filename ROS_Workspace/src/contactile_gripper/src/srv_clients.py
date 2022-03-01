
import rospy
from contactile_gripper.srv import GripperChangeMode
from contactile_gripper.srv import StepperOff
from contactile_gripper.srv import StepperSetLimit
from contactile_gripper.srv import DataRecorder

def gripper_change_mode_srv_client(mode):
    rospy.logdebug('[gripper_change_mode_srv_client] {}'.format(mode))
    print('[gripper_change_mode_srv_client] {}'.format(mode))
    rospy.wait_for_service('gripper_change_mode_srv')
    try:
        gripper_change_mode_srv = rospy.ServiceProxy('gripper_change_mode_srv',GripperChangeMode)
        msg = gripper_change_mode_srv(mode)
        return msg.response
    except:
        rospy.logerr('Change mode service failed.')

def stepper_off_srv_client(mode):
    rospy.wait_for_service('stepper_off_srv')
    try:
        stepper_off_srv = rospy.ServiceProxy('stepper_off_srv',StepperOff)
        msg = stepper_off_srv(mode)
        return msg.response
    except:
        rospy.logerr('Change mode service failed.')

def stepper_set_limit_srv_client(switch,action):
    rospy.wait_for_service('stepper_set_limit_srv')
    try:
        stepper_off_srv = rospy.ServiceProxy('stepper_set_limit_srv',StepperSetLimit)
        msg = stepper_off_srv(switch,action)
        return msg.response
    except:
        rospy.logerr('Change mode service failed.')

def data_recorder_client(topic_list,file_prefix='contactile',stop=False):
    rospy.wait_for_service('data_recorder_srv')
    stepper_off_srv = rospy.ServiceProxy('data_recorder_srv',DataRecorder)
    msg = stepper_off_srv(file_prefix,topic_list,stop)
    print(msg)