import threading

import cv2
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from pyqt_class.web_stream import WebcamStream
from pyqt_class.window_fix import ImageWindow
import shutil


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.file_path = None
        self.file_path_new = 'save_file/save_picture'
        uic.loadUi('design/main.ui', self)
        self.setWindowTitle("Photo editor")
        self.choice_picture.clicked.connect(self.choice_file)
        self.camera_veb.clicked.connect(self.stream_camera)
        self.show()

    def choice_file(self):
        options = QFileDialog.Options()
        self.file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "File .png (*.png);;File .jpeg ("
                                                                                  "*.jpeg)",
                                                   options=options)
        if self.file_path != '':
            if self.file_path.endswith('jpg'):
                self.create_example_Image_window('.jpg')
            else:
                self.create_example_Image_window('.png')

    def stream_camera(self):
        cap = cv2.VideoCapture(0)
        if cap is None or not cap.isOpened():
            warning = QMessageBox.warning(
                self,
                "Внимание",
                "Невозможно подключиться к камере",
            )
        else:
            self.web_stream_widget = WebcamStream()
            self.web_stream_widget.show()

    def create_example_Image_window(self, form):
        self.file_path_new += form
        shutil.copy(self.file_path, self.file_path_new)
        self.image_window = ImageWindow(path_file=self.file_path_new, form=form)
