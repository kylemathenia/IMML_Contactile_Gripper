

"""Get the motor working from a Python script."""
import serial
import serial.tools.list_ports
import atexit
import time

class Stepper(object):
    def __init__(self):
        # self.dev_board_name = 'Arduino Uno'
        self.dev_board_name = 'Arduino Micro'
        self.baudrate = 115_200
        self.com_path = self.find_com_path()
        self.serial = serial.Serial(self.com_path, baudrate=9600, timeout=1)
        atexit.register(self.shutdown)

    def clean_before_read_start(self):
        """Sets the read protocol pattern to align with the Arduino write protocol.
        This must be run once before starting to continuously read.
        The Ardunino write protocol is: 'xdata_ydata_zdata\n'"""
        self.serial.read_until() # Reads until \n by default.

    def read(self):
        """Returns x,y,z,com_success. com_success is boolean. Data comes in the form: 'xdata_ydata_zdata\n'"""
        line = self.serial.readline().decode('ascii').strip('\n\r')
        data = line.split('_')
        # Rarely, the IMU doesn't read all the data. Don't return anything if that happens.
        if len(data) == 3: return float(data[0]),float(data[1]),float(data[2]),True
        else: return None,None,None,False

    def find_com_path(self):
        """Finds and returns the device port name path as string. Ex: '/dev/ttyUSB0 or '"""
        comports = serial.tools.list_ports.comports()
        products =[]
        for comport in comports:
            products.append(comport.product)
            if self.dev_board_name in comport.description: return comport.device
        # rospy.logfatal('IMU not found.')
        raise Exception('"{} not found in comport products: {}'.format,self.dev_board_name,products)

    def shutdown(self):
        self.serial.close()

    def read_write(self,string):
        self.serial.write(string.encode('ascii'))
        # time.sleep(0.1)
        data = self.serial.readline().decode('ascii')
        return data

def main():
    arduino = Stepper()
    arduino.clean_before_read_start()

    count = 0
    start = time.time()
    while time.time() - start < 1:
        ans = arduino.read()
        # print(ans)
        count += 1
    print(count)

def secondary():
    arduino = Stepper()
    time.sleep(1)
    string = 'x32_y59_z20_\n'
    count = 0
    start = time.time()
    while time.time() - start < .05:
        # string = input("Enter a string: ")
        # string = 'echo'
        ans = arduino.read_write(string)
        count += 1
        print(ans)
    print(count)

if __name__ == '__main__':
    main()
    # secondary()
