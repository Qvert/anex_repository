from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QColor


class ImageWindow(QWidget):
    def __init__(self, path_file=None):
        super().__init__()
        uic.loadUi('design/widget_image.ui', self)
        self.pixmap = QPixmap(path_file)
        self.label_picture.setScaledContents(True)
        self.label_picture.setPixmap(self.pixmap)
        self.setWindowTitle('Image in QLabel')
        # self.circle.clicked.connect()
        # self.gaussian_blur.clicked.connect()
        self.negative.clicked.connect(self.negative_function)
        self.show()

    def negative_function(self):
        if self.pixmap:
            image = self.pixmap.toImage()
            for y in range(image.height()):
                for x in range(image.width()):
                    color = image.pixelColor(x, y)
                    inverted_color = QColor(255 - color.red(), 255 - color.green(), 255 - color.blue())
                    image.setPixelColor(x, y, inverted_color)
            self.label_picture.setPixmap(QPixmap.fromImage(image).
                                         scaled(self.label_picture.size(),
                                         aspectRatioMode=Qt.KeepAspectRatio))

    def gaussian_blur_function(self):
        pass

    def circle_function(self):
        pass
