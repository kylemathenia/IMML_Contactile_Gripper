#!/usr/bin/env python
"""
Prints info about the currently connected comport devices and paths.
"""

import serial
import serial.tools.list_ports

def print_com_info():
    comports = serial.tools.list_ports.comports()
    for comport in comports:
        info = comport.__dict__
        print("\n\n#####################################################")
        for key in info.keys():
            print("{}: {}".format(key,info[key]))

def get_com_info():
    comport_info = []
    comports = serial.tools.list_ports.comports()
    for comport in comports:
        comport_info.append(comport.__dict__)
    return comport_info

def main():
    print_com_info()

if __name__ == '__main__':
    main()
