from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class SelectChanel(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("design/chanels_rgb.ui", self)
        self.setWindowTitle("Select chanel")
        self.show()

    def select_red_channel(self):
        pass

    def select_green_channel(self):
        pass

    def select_blue_channel(self):
        pass
