
import rospy
from contactile_gripper.srv import *
from papillarray_ros_v2.srv import *

def gripper_change_mode_srv_client(mode):
    rospy.logdebug('[gripper_change_mode_srv_client] {}'.format(mode))
    rospy.wait_for_service('gripper_change_mode_srv')
    gripper_change_mode_srv = rospy.ServiceProxy('gripper_change_mode_srv', GripperChangeMode)
    msg = gripper_change_mode_srv(mode)
    return msg.response

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

def data_recorder_srv_client(topic_list,file_prefix='contactile',stop=False):
    rospy.wait_for_service('data_recorder_srv')
    try:
        stepper_off_srv = rospy.ServiceProxy('data_recorder_srv',DataRecorder)
        _ = stepper_off_srv(file_prefix,topic_list,stop)
    except:
        rospy.logerr('data_recorder_srv failed.')

def ui_menu_srv_client(menu):
    rospy.wait_for_service('ui_menu_srv')
    stepper_off_srv = rospy.ServiceProxy('ui_menu_srv', UIMenu)
    _ = stepper_off_srv(menu)

def bias_request_srv_client():
    rospy.wait_for_service('/hub_0/send_bias_request')
    bias_request_srv = rospy.ServiceProxy('/hub_0/send_bias_request', BiasRequest)
    success = bias_request_srv()
    return success
