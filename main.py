""" Главный файл приложения для запуска"""

import sys
from window import MainWindow
from PySide6 import QtWidgets
from multiprocessing import Process

def startGui():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(920, 609)
    window.show()
    app.exec()

if __name__ == "__main__":

    mainPrc = Process(target = startGui)
    mainPrc.start()
    mainPrc.join()

