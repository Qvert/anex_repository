from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from pyqt_class.web_stream import WebcamStream


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('design/main.ui', self)
        self.choice_picture.clicked.connect(self.choice_file)
        self.camera_veb.clicked.connect(self.stream_camera)
        self.show()

    def choice_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Выбрать файл", "", "File .png (*.png);;File .jpeg (*.jpeg)",
                                                   options=options)

    def stream_camera(self):
        self.web_stream_widget = WebcamStream()
        self.web_stream_widget.show()
