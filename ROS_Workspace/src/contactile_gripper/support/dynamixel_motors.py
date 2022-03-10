#!/usr/bin/env python
"""
This module contains a class and super class for the XM430_W210 Dyanmixel motor.
"""

import sys
import os
# If running the script without ROS, rospy logging will not work. Use rospy_shadow instead.
try:
    import rospy
    from dynamixel_sdk import *
except:
    import rospy_shadow as rospy
    dynamixel_sdk_path = os.getcwd().replace('contactile_gripper','dynamixel_sdk')
    sys.path.append(dynamixel_sdk_path) # Path to dynamixel sdk package.
    from dynamixel_sdk import *
import os
import inspect
import time
import atexit
import serial
import serial.tools.list_ports


class Dynamixel(object):
    """Base class for Dynamixel motors."""
    def __init__(self):
        pass

    def write_goal_pos(self,value):
        if value < self.MIN_POS_FULLY_OPEN: value = self.MIN_POS_FULLY_OPEN
        elif value > self.MAX_POS_FULLY_CLOSED: value = self.MAX_POS_FULLY_CLOSED
        rospy.logdebug('[write_goal_pos] {}'.format(value))
        try: assert self.mode == 'pos_control' or self.mode == 'ext_pos_control' or self.mode == 'cur_based_pos_control' and self.torque == 'on'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req mode: pos_control ({}), '
                                             'req torque: on ''({})'.format(self.mode, self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, self.id,self.addr_goal_pos, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_goal_vel(self,value):
        rospy.logdebug('[write_goal_vel] {}'.format(value))
        try: assert self.mode == 'vel_control' and self.torque == 'on'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req mode: vel_control ({}), '
                                             'req torque: on ''({})'.format(self.mode, self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, self.id,self.addr_goal_vel, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_goal_cur(self,value):
        """Positive/negative = closing/opening"""
        if value > self.MAX_CURRENT_ABS: value = self.MAX_CURRENT_ABS
        elif value < -self.MAX_CURRENT_ABS: value = -self.MAX_CURRENT_ABS
        rospy.logdebug('[write_goal_cur] {}'.format(value))
        try: assert self.mode == 'cur_control' and self.torque == 'on'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req mode: cur_control ({}), '
                                             'req torque: on ''({})'.format(self.mode, self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id, self.addr_goal_cur, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_moving_threshold(self,value):
        rospy.loginfo('[write_moving_threshold] {}'.format(value))
        try: assert self.torque == 'off'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req torque: off ''({})'.format(self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, self.id, self.addr_moving_threshold, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_homing_offset(self,value):
        rospy.logdebug('[write_homing_offset] {}'.format(value))
        try: assert self.torque == 'off'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req torque: off ''({})'.format(self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write4ByteTxRx(self.portHandler, self.id, self.addr_homing_offset, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_pos_p_gain(self,value):
        rospy.logdebug('[write_pos_p_gain] {}'.format(value))
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id, self.addr_pos_p_gain, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_pos_i_gain(self,value):
        rospy.logdebug('[write_pos_i_gain] {}'.format(value))
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id, self.addr_pos_i_gain, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_pos_d_gain(self,value):
        rospy.logdebug('[write_pos_d_gain] {}'.format(value))
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id, self.addr_pos_d_gain, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_led(self,value):
        rospy.logdebug('[write_led] {}'.format(value))
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, self.id, self.addr_led, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)

    def write_torque_mode(self,mode):
        """Arguments: 'on','off' """
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, self.id,self.addr_torque_mode,self.torque_modes[mode])
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        if not error:
            self.torque = mode
            rospy.logdebug('[motor torque mode] {}'.format(mode))
        return error

    def write_operating_mode(self,mode):
        """Arguments: 'cur_control', 'vel_control', 'pos_control', 'ext_pos_control', 'cur_based_pos_control', 'PWM_control' """
        rospy.logdebug('[write_operating_mode] {}'.format(mode))
        try: assert self.torque == 'off'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req torque: off ''({})'.format(self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write1ByteTxRx(self.portHandler, self.id,self.addr_operating_mode,self.operating_modes[mode])
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        if not error:
            self.mode = mode
            rospy.logdebug('[operating_mode] {}'.format(mode))
        return error

    def write_current_limit(self,value):
        rospy.logdebug('[write_current_limit] {}'.format(value))
        try: assert self.torque == 'off'
        except AssertionError: rospy.logwarn('Write failed. Motor is not in the correct state. req torque: off ''({})'.format(self.torque))
        dxl_comm_result, dxl_error = self.packetHandler.write2ByteTxRx(self.portHandler, self.id, self.addr_current_limit, value)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        self.MAX_CURRENT_ABS = value

    def switch_modes(self,mode):
        """Arguments: 'cur_control', 'vel_control', 'pos_control', 'ext_pos_control', 'cur_based_pos_control', 'PWM_control'
        Leaves the motor torque on."""
        rospy.loginfo('[switch_modes] {}'.format(mode))
        if self.torque != 'off': self.write_torque_mode('off')
        if self.mode != mode: self.write_operating_mode(mode)
        self.write_torque_mode('on')

    def read_pos(self):
        try:
            result, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, self.id,self.addr_present_pos)
            error = self.log_com_if_error(dxl_comm_result, dxl_error)
        except:
            result=0
            error = True
        rospy.logdebug('[read_pos] {}'.format(result))
        return result, error

    def read_vel(self):
        result, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, self.id, self.addr_present_vel)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        rospy.logdebug('[read_vel] {}'.format(result))
        return result, error

    def read_cur(self):
        result, dxl_comm_result, dxl_error = self.packetHandler.read2ByteTxRx(self.portHandler, self.id, self.addr_present_cur)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        rospy.logdebug('[read_cur] {}'.format(result))
        return result, error

    def read_moving(self):
        """Returns True/False for whether or not the motor is moving (withing the moving threshold value)"""
        result, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, self.id, self.addr_moving)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        moving = True if result == 1 else False
        rospy.logdebug('[read_moving] {}'.format(moving))
        return moving, error

    def read_mode(self):
        result, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, self.id, self.addr_operating_mode)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        inv_operating_modes_dict = {v: k for k, v in self.operating_modes.copy().items()}
        self.mode = inv_operating_modes_dict[result]
        mode = self.mode
        rospy.loginfo('[motor operating mode] {}'.format(self.mode))
        return mode, error

    def read_homing_offset(self):
        result, dxl_comm_result, dxl_error = self.packetHandler.read4ByteTxRx(self.portHandler, self.id, self.addr_homing_offset)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        rospy.logdebug('[read_vel] {}'.format(result))
        return result, error


    def log_com_if_error(self,dxl_comm_result,dxl_error):
        """Logs and returns True/False if there was a com error."""
        error = False
        if dxl_comm_result != COMM_SUCCESS:
            rospy.logwarn("DYNAMIXEL COM FAILURE in function: {}".format(inspect.stack()[1][3]))
            rospy.logwarn("%s" % self.packetHandler.getTxRxResult(dxl_comm_result))
            error = True
        if dxl_error != 0:
            rospy.logwarn("DYNAMIXEL COM FAILURE")
            rospy.logwarn("%s" % self.packetHandler.getRxPacketError(dxl_error))
            error = True
        return error

    def initialize(self):
        rospy.loginfo('[INITIALIZE MOTOR]')
        # Dynamixel porthandler and packethandler instances.
        self.portHandler = PortHandler(self.port_name)
        self.packetHandler = PacketHandler(self.protocol_version)
        # Open port
        if not self.portHandler.openPort(): rospy.logfatal("Failed to open the port. Port name path: {}".format(self.port_name))
        # Set port baudrate
        if not self.portHandler.setBaudRate(self.baud_rate): rospy.logfatal("Failed to change the baudrate")
        # Test coms
        result, dxl_comm_result, dxl_error = self.packetHandler.read1ByteTxRx(self.portHandler, self.id, self.addr_operating_mode)
        error = self.log_com_if_error(dxl_comm_result, dxl_error)
        if error:
            rospy.logfatal('Result: {}'.format(result))
            rospy.logfatal('Test communication failed. Check baud rate, connection, and power.')
            raise Exception
        else: rospy.loginfo('Established motor coms.')
        # Find and set the current operating mode, and set current.
        self.read_mode()
        self.write_torque_mode('off')
        self.status = 'initialized'
        rospy.loginfo('[motor status] {}'.format(self.status))

    def shutdown(self):
        rospy.loginfo('[SHUTDOWN MOTOR]')
        if self.status == 'initialized': # If it failed during initialization the torque can't be written to zero.
            while True: # Make sure the motor torque gets turned off.
                error = self.write_torque_mode('off')
                if not error: break
        self.portHandler.closePort()
        self.status = 'shutdown'
        rospy.loginfo('[motor status] {}'.format(self.status))

    def find_port_name(self):
        """Finds and returns the device port name path as string. Ex: '/dev/ttyUSB0'"""
        comports = serial.tools.list_ports.comports()
        for comport in comports:
            try:
                if self.serial_number in comport.serial_number and 'linux' in os.sys.platform:
                    return comport.device
                if self.serial_number in comport.serial_number and 'linux' not in os.sys.platform:
                    return comport.name
            except: pass
        rospy.logfatal('Motor not found.')
        raise Exception('Serial number for motor not found in connected devices.\n')


class XM430_W210(Dynamixel):
    """Class for the XM430_W210 motor.
    Find the serial number with 'comports = serial.tools.list_ports.comports()' & 'comport.serial_number"""

    def __init__(self, id, serial_number, protocol_version, baud_rate, current_limit = 50):
        super(Dynamixel,self).__init__()
        self.id = id
        self.baud_rate = baud_rate
        self.protocol_version = protocol_version
        self.serial_number = serial_number
        self.port_name = self.find_port_name()
        self.mode = None
        self.torque = 'off'
        self.status = None
        # Device addresses and values specific to XM430_W210 Dynamixel motor
        self.addr_id = 7
        self.addr_baud_rate = 8
        self.addr_drive_mode = 10
        self.addr_operating_mode = 11
        self.addr_protocol_type = 13
        self.addr_homing_offset = 20
        self.addr_moving_threshold = 24
        self.addr_current_limit = 38
        self.addr_shutdown = 63
        self.addr_torque_mode = 64
        self.addr_led = 65
        self.addr_pos_d_gain = 80
        self.addr_pos_i_gain = 82
        self.addr_pos_p_gain = 84
        self.addr_goal_PWM = 100
        self.addr_goal_cur = 102
        self.addr_goal_vel = 104
        self.addr_goal_pos = 116
        self.addr_moving = 122
        self.addr_moving_status = 123
        self.addr_present_PWM = 124
        self.addr_present_cur = 126
        self.addr_present_vel = 128
        self.addr_present_pos = 132
        self.operating_modes = {'cur_control': 0, 'vel_control': 1, 'pos_control': 3, 'ext_pos_control': 4,
                                'cur_based_pos_control': 5, 'PWM_control': 16}
        self.torque_modes = {'on': 1, 'off': 0}
        self.MAX_CURRENT_ABS = current_limit
        self.MIN_POS_FULLY_OPEN = -10000000  # lower value
        self.MAX_POS_FULLY_CLOSED = 10000000 # higher value
        atexit.register(self.shutdown)
        self.initialize()

    def __repr__(self):
        pass

def test():
    try:
        m = XM430_W210(1, 'FT5NSNJ0', 2.0, 4000000)
        rospy.logdebug('Mode: {}'.format(m.mode))
        rospy.logdebug('Torque: {}'.format(m.torque))
        rospy.logdebug('Status: {}'.format(m.status))
        m.write_goal_cur(0)
        m.write_torque_mode('on')
        m.switch_modes('cur_control')

        duration = 1
        start = time.time()
        counter = 0
        while time.time() - start < duration:
            m.read_pos()
            counter += 1
        rospy.loginfo('Reading position at a rate of: {}'.format(counter/duration))

        start = time.time()
        counter = 0
        while time.time() - start < duration:
            m.write_goal_cur(0)
            counter += 1
        rospy.loginfo('Writing current at a rate of: {}'.format(counter/duration))

        rospy.loginfo('Test passed.')

    except: rospy.loginfo('Test failed.')

def main():
    test()

if __name__ == '__main__':
    main()