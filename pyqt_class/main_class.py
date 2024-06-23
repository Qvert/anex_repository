from PyQt5 import QtWidgets, uic

from pyqt_class.web_stream import WebcamStream


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('design/main.ui', self)
        self.show()
        self.camera_veb.clicked.connect(self.show_stream)

    def show_stream(self):
        stream = WebcamStream()
