import os
import cv2
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QColor, QImage
from pyqt_class.select_chanel import SelectChanel


class ImageWindow(QWidget):
    def __init__(self, path_file=None, form=None):
        super().__init__()
        uic.loadUi('design/widget_image.ui', self)
        self.COUNT_FILE = 1
        self.form = form
        self.image_cv2 = None
        self.pixmap = QPixmap(path_file)
        self.path_file = path_file
        self.label_picture.setScaledContents(True)
        self.label_picture.setPixmap(self.pixmap)
        self.setWindowTitle('Photo editing')
        self.circle.clicked.connect(self.circle_function)
        self.gaussian_blur.clicked.connect(self.gaussian_blur_function)
        self.negative.clicked.connect(self.negative_function)
        self.save_change.clicked.connect(self.save_picture)
        self.view_channels.clicked.connect(self.show_channels)
        self.show()

    def show_channels(self):
        self.widget_with_channels = SelectChanel()
        self.widget_with_channels.show()

    def negative_function(self):
        if self.pixmap:
            image = self.pixmap.toImage()
            for y in range(image.height()):
                for x in range(image.width()):
                    color = image.pixelColor(x, y)
                    inverted_color = QColor(255 - color.red(), 255 - color.green(), 255 - color.blue())
                    image.setPixelColor(x, y, inverted_color)
            self.set_picture_label(image)

    def gaussian_blur_function(self):
        """
        Gaussian blurring of the image
        :return: None
        """
        self.image_cv2 = cv2.imread(self.path_file)
        if self.image_cv2 is not None:
            sigma, ok = QInputDialog.getDouble(self, 'Gaussian Blur', 'Enter sigma value:', min=0.1, max=70)
            if ok:
                blurred_image = cv2.GaussianBlur(self.image_cv2, (0, 0), sigma)
                self.display_image(blurred_image)

    def circle_function(self):
        """
        Draw circle in QLabel
        :return: None
        """
        self.image_cv2 = cv2.imread(self.path_file)
        if self.image_cv2 is not None:
            radius, ok = QInputDialog.getInt(self, 'Draw Circle', 'Enter radius:', min=1)
            if ok:
                x, ok1 = QInputDialog.getInt(self, 'Draw Circle', 'Enter x coordinate:', min=0,
                                             max=self.image_cv2.shape[1])
                if ok1:
                    y, ok2 = QInputDialog.getInt(self, 'Draw Circle', 'Enter y coordinate:', min=0,
                                                 max=self.image_cv2.shape[0])
                    if ok2:
                        image_with_circle = self.image_cv2.copy()
                        cv2.circle(image_with_circle, (x, y), radius, (255, 0, 0), 2)
                        self.display_image(image_with_circle)

    def display_image(self, image):
        """
        Converting opencv image to Pyqt
        :param image: Image
        :return: None
        """
        qformat = QImage.Format_Indexed8
        if len(image.shape) == 3:  # rows[0], cols[1], channels[2]
            if image.shape[2] == 4:
                qformat = QImage.Format_RGBA8888
            else:
                qformat = QImage.Format_RGB888

        img = QImage(image, image.shape[1], image.shape[0], image.strides[0], qformat)
        img = img.rgbSwapped()
        self.set_picture_label(img)

    def set_picture_label(self, img):
        """
        Set picture in QLabel
        :param img: Image
        :return: None
        """
        self.label_picture.setPixmap(QPixmap.fromImage(img).scaled(self.label_picture.size(),
                                                                   Qt.KeepAspectRatio))

    def save_picture(self):
        """
        Function save picture to dir
        :return: None
        """
        try:
            path_save = 'save_file/save_picture' + self.form
            img = self.label_picture.pixmap().toImage()
            if os.path.isfile(path_save):
                img.save(f'{path_save[:-4]} ({self.COUNT_FILE}).jpg')
                self.COUNT_FILE += 1
            else:
                img.save(path_save)
            self.label_picture.setPixmap(QPixmap(path_save))
        except Exception as _err:
            warning = QMessageBox.warning(
                self,
                "Внимание",
                "Ошибка сохранения",
            )
        finally:
            info = QMessageBox.information(
                self,
                "Внимание",
                "Успешно сохранено",
            )
