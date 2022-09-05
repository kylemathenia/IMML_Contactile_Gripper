#!/usr/bin/env python2
"""Launches the gripper. Generates a ROS launch file based on com port findings and config options, and call roslaunch
with that newly generated file.

The reason that this file is used to launch instead of a typical ROS launch file is because the comport info for the
contactile sensors is not found dynamically on startup. Instead, the comport path is a parameter in the launch file.
This is a problem because the host computer will not reliably give the contactile sensor the same comport. Instead
of finding the comport info every time and editing the launch file, this launch file finds the correct comport and
generates a launch file."""

import serial
import serial.tools.list_ports
import subprocess, shlex, os
import time
import logging

logging.basicConfig(level = logging.INFO)

# Config options
stepper = False
IMU = False
camera = False

# File info
launch_dir =  "./ROS_Workspace/src/contactile_gripper/launch/"
gen_file_name = "autogen.launch"
gen_file_path = launch_dir + gen_file_name
contactile_node_txt = "contactile.txt"
gripper_node_txt = "gripper.txt"
stepper_node_txt = "stepper.txt"
imu_node_txt = "imu.txt"
control_node_txt = "control.txt"
UI_node_txt = "UI.txt"
data_recorder_path = "./ROS_Workspace/src/contactile_gripper/src/data_recorder_node.py"

def generate_file():
    """The order matters. Some nodes need to be started before others."""
    with open(gen_file_path, 'w') as genFile:
        genFile.write("\n<launch>")
        write_contactile(genFile)
        write_gripper(genFile)
        if stepper:
            write_stepper(genFile)
        if IMU:
            write_imu(genFile)
        write_control(genFile)
        write_UI(genFile)
        genFile.write("\n\n</launch>")
        logging.info("Launch file generated.")

def launch():
    command = "roslaunch contactile_gripper {} ".format(gen_file_name)
    args = shlex.split(command)
    process = subprocess.Popen(args, stderr=subprocess.PIPE, shell=False)

def launch_data_recorder():
    """For some reason, the data recorder node must be started outside of the launch file."""
    time.sleep(10)
    os.system("gnome-terminal -- " + data_recorder_path)

def write_contactile(write_file):
    read_file_path = launch_dir + contactile_node_txt
    port_path = find_contactile_port()
    with open(read_file_path,'r') as read_file:
        lines = read_file.readlines()
        write_file.write("\n\n")
        for line in lines:
            if "com_port" in line:
                line = line.replace("TBD",'"'+port_path+'"')
            write_file.write(line)

def find_contactile_port():
    """Returns the comport path for the contactile sensor hub."""
    comport_info = get_com_info()
    for port in comport_info:
        if port['serial_number'] == '10129740':
            return port['device']
    print("\nContactile sensor hub port info not found.\n")
    raise LookupError

def write_gripper(write_file):
    read_file_path = launch_dir + gripper_node_txt
    write_all_lines(read_file_path,write_file)

def write_imu(write_file):
    read_file_path = launch_dir + imu_node_txt
    write_all_lines(read_file_path,write_file)

def write_stepper(write_file):
    read_file_path = launch_dir + stepper_node_txt
    write_all_lines(read_file_path,write_file)

def write_control(write_file):
    read_file_path = launch_dir + control_node_txt
    write_all_lines(read_file_path,write_file)

def write_UI(write_file):
    read_file_path = launch_dir + UI_node_txt
    write_all_lines(read_file_path,write_file)

def write_all_lines(read_file_path,write_file):
    with open(read_file_path, 'r') as read_file:
        lines = read_file.readlines()
        write_file.write("\n\n")
        for line in lines:
            write_file.write(line)

def get_com_info():
    comport_info = []
    comports = serial.tools.list_ports.comports()
    for comport in comports:
        comport_info.append(comport.__dict__)
    return comport_info

def main():
    generate_file()
    launch()
    # For some reason, the data recorder node must be started outside of the launch file.
    launch_data_recorder()
    logging.info("Launch complete.")
    # Call the file.
    # Launch the data recorder node seperate, after.

if __name__ == "__main__":
    main()