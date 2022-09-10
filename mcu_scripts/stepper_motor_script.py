import serial
import serial.tools.list_ports
import atexit
import time
import re

""""
/* Write communication protocol:
 * Format: [mode][value]
 * p = position mode
 * s = speed mode
 * x = off/passive mode
 * Example: "p500" -> position mode, move 500 positive
 * Example: "x1" -> off mode, 1 is unused, but 
 */

/* Read communication protocol:
 * Format: <[lim switch 1 status]_[lim switch 2 status]_[current position]>
 * lim switch status: 1 if engaged, 0 if not.
 * Example: "<1_0_543>" -> lim switch 1 engaged, lim switch 2 not engaged, current position is 543.
 */
 """

class Stepper(object):
    def __init__(self):
        self.dev_board_name = 'Arduino Uno'
        self.baudrate = 2_500_000
        self.com_path = self.find_com_path()
        self.serial = serial.Serial(self.com_path, baudrate=self.baudrate, timeout=1)
        atexit.register(self.shutdown)

    def clean_before_read_start(self):
        """Sets the read protocol pattern to align with the Arduino write protocol.
        This must be run once before starting to continuously read."""
        self.serial.reset_input_buffer()
        self.serial.read_until() # Reads until \n by default.

    def read(self):
        line = self.serial.read_until().decode('ascii')
        data = line.strip('<>\n\r').split('_')
        self.serial.reset_input_buffer()
        if '<' in line and '>' in line:
            return int(data[0]),int(data[1]),int(data[2]),True
        else:
            return None,None,None,False

    def write(self,cmd):
        if self.serial.out_waiting == 0:
            self.serial.write(bytes(cmd.encode()))

    def find_com_path(self):
        """Finds and returns the device port name path as string. Ex: '/dev/ttyUSB0 or '"""
        comports = serial.tools.list_ports.comports()
        products =[]
        for comport in comports:
            products.append(comport.product)
            if self.dev_board_name in comport.description: return comport.device
        # rospy.logfatal('IMU not found.')
        raise Exception('"{} not found in comport products: {}'.format(self.dev_board_name,products))

    def shutdown(self):
        self.serial.write(b'x0\n')
        self.serial.close()


def test():
    stepper = Stepper()
    stepper.clean_before_read_start()
    count = 0
    num = 50
    start = time.time()
    stepper.clean_before_read_start()
    while time.time() - start < 30:
        if stepper.serial.in_waiting > 0:
            print("Incoming in waiting: {}".format(stepper.serial.in_waiting))
            ans = stepper.read()
            print(ans)
            count += 1
        if stepper.serial.out_waiting == 0:
            cmd = 's' + str(num) + '\n'
            stepper.write(cmd)
            print(cmd)
            num += 1
            time.sleep(.01)
if __name__ == '__main__':
    test()
