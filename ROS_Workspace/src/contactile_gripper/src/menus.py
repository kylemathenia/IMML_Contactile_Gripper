

class Menu(object):
    def __init__(self):
        self.menu = self.main_menu
        self.k='test'

    def main_menu(self):
        print('h')

    main_menu.main_menu_p = "prompt {}".format(self.k)
