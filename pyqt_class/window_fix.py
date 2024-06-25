from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap


class ImageWindow(QWidget):
    def __init__(self, path_file=None):
        super().__init__()
        uic.loadUi('design/widget_image.ui', self)
        pixmap = QPixmap(path_file)
        self.label_picture.setScaledContents(True)
        self.label_picture.setPixmap(pixmap)
        self.setWindowTitle('Image in QLabel')
        self.show()

