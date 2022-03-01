import time

class UiNode(object):
    def __init__(self):
        self.gripper_mode_options = set({'passive', 'cur_based_pos_control', 'sinusoidal_motion_routine'})
        self.gripper_mode = 'passive'
        self.gripper_pos_increment = 5
        self.stepper_mode_options = set({'passive', 'position_control', 'speed_control'})
        self.stepper_mode = 'passive'
        self.stepper_pos_increment = 100
        self.stepper_upper_lim = None
        self.stepper_lower_lim = None

        self.current_menu = self.func

        self.main_loop()

    def func(self,string):
        print(string)
        time.sleep(.5)

    def main_loop(self):
        """Continuously get the key inputs from the user and pass the key to the current menu method."""
        while True:
            self.func()
            time.sleep(1)


x = UiNode()