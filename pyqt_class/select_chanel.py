import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic


class SelectChanel(QWidget):
    def __init__(self, path_file=None, form=None):
        super().__init__()
        uic.loadUi("design/chanels_rgb.ui", self)
        self.setWindowTitle("Select chanel")
        self.initUI(path_to_file=path_file)
        self.path_file = path_file
        self.form = form
        self.red_channel.clicked.connect(self.select_red_channel)
        self.green_channel.clicked.connect(self.select_green_channel)
        self.blue_channel.clicked.connect(self.select_blue_channel)
        self.show()

    def initUI(self, path_to_file):
        image = cv2.imread(path_to_file)
        b, g, r = cv2.split(image)
        self.r_img = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
        self.g_img = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
        self.b_img = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])
        self.displayChannel(self.r_img, self.red_label)
        self.displayChannel(self.g_img, self.green_label)
        self.displayChannel(self.b_img, self.blue_label)

    def select_red_channel(self):
        self.show_image_window(self.r_img)

    def select_green_channel(self):
        self.show_image_window(self.g_img)

    def select_blue_channel(self):
        self.show_image_window(self.b_img)

    @classmethod
    def displayChannel(cls, channel, label):
        rgb_image = cv2.cvtColor(channel, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(400, 400, aspectRatioMode=1)
        label.setPixmap(QPixmap.fromImage(p))

    def show_image_window(self, channel):
        from pyqt_class.window_fix import ImageWindow
        cv2.imwrite(self.path_file, channel)
        self.image_window = ImageWindow(path_file=self.path_file, form=self.form)
        self.image_window.show()
        self.close()
