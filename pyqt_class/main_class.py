from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
from pyqt_class.web_stream import WebcamStream
from pyqt_class.window_fix import ImageWindow


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
        if file_path != '':
            self.image_window = ImageWindow(path_file=file_path)
            self.image_window.show()

    def stream_camera(self):
        self.web_stream_widget = WebcamStream()
        self.web_stream_widget.show()
