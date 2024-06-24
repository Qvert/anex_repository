import sys

from pyqt_class.main_class import QtWidgets, Ui


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


if __name__ == '__main__':
    main()
