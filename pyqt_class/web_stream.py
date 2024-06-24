import cv2
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer


class WebcamStream(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(20)

    def initUI(self):
        self.image_label = QLabel(self)
        self.snapchot = QPushButton('Сделать снимок', self)
        self.quit_button = QPushButton('Выход', self)

        self.snapchot.clicked.connect(self.snapchot_function)
        self.quit_button.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.snapchot)
        vbox.addWidget(self.quit_button)
        self.setLayout(vbox)

        self.setWindowTitle('Webcam Stream')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            bytes_per_line = ch * w
            convert_to_Qt_format = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
            p = convert_to_Qt_format.scaled(800, 600, aspectRatioMode=1)
            self.image_label.setPixmap(QPixmap.fromImage(p))

    def snapchot_function(self, event):
        try:
            ret, frame = self.cap.read()
        except Exception as _err:
            pass
        finally:
            self.cap.release()
            event.accept()

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

