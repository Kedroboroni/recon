""" Файл в котором  созданы кастомные виджеты на основе родителей PySide6 """


from PySide6.QtWidgets import QPushButton, QLabel,  QLineEdit, QGroupBox, QWidget
from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import QRect
        

class Lable(QLabel):
    """Формат вызова (self, место по x, место по y, ширина, высота)"""
    def __init__(self, place, mouseX = None, mouseY = None, x = None, y = None, w = None, h = None, text = None):
        super().__init__(place)
        self.mouseX = mouseX
        self.mouseY = mouseY
        self.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0.0454545 rgba(188, 55, 255, 144), stop:0.164773 rgba(80, 4, 197, 146), stop:0.272727 rgba(75, 46, 213, 162), stop:0.369318 rgba(162, 36, 251, 175), stop:0.494318 rgba(185, 98, 237, 175), stop:0.590909 rgba(231, 69, 222, 130), stop:0.698864 rgba(209, 36, 185, 188), stop:0.789773 rgba(189, 0, 122, 140), stop:0.897727 rgba(107, 10, 204, 153), stop:1 rgba(100, 0, 219, 157));\n"
                                "\n"
                                "font: 10pt \"Noto Serif\";\n"
                                "border-radius:7px;\n"
                                "border:1px solid rgba(255,255,255,40);")
        #self.setMouseTracking(True)
        self.setScaledContents(True)
        if text:
            self.setText(text)
        if x and y and w and h:
            self.setGeometry(QRect(x, y, w, h))

    def mouseMoveEvent(self, event):
        if self.mouseX and self.mouseY:
            self.event = event
            self.X = int(QMouseEvent.x(event))
            self.Y = int(QMouseEvent.y(event))
            self.mouseX.setText("x = {0}".format(self.X))
            self.mouseY.setText("y = {0}".format(self.Y))
        

class Button(QPushButton):
    """Формат вызова (self, место по x, место по y, ширина, высота)"""
    def __init__(self, place, text = "YouNeedInstallTTextThisButton", x = None, y = None, w = None, h = None):
        super().__init__(place)
        self.setText(text)
        self.setStyleSheet("QPushButton {\n"
                            "background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0.0454545 rgba(188, 55, 255, 144), stop:0.164773 rgba(80, 4, 197, 146), stop:0.272727 rgba(75, 46, 213, 162), stop:0.369318 rgba(162, 36, 251, 175), stop:0.494318 rgba(185, 98, 237, 175), stop:0.590909 rgba(231, 69, 222, 130), stop:0.698864 rgba(209, 36, 185, 188), stop:0.789773 rgba(189, 0, 122, 140), stop:0.897727 rgba(107, 10, 204, 153), stop:1 rgba(100, 0, 219, 157));\n"
                            "font: 10pt \"Noto Serif\";\n"
                            "border-radius:7px;\n"
                            "border:1px solid rgba(255,255,255,40);\n"
                            "}\n"
                            "QPushButton:hover {\n"
                            "background-color: rgba(148, 25, 255,40);\n"
                            "font: 10pt \"Noto Serif\";\n"
                            "border-radius:7px;\n"
                            "border:1px solid rgba(255,255,255,40);\n"
                            "}\n"
                            "QPushButton:pressed {\n"
                            "background-color: rgba(120, 25, 200,50);\n"
                            "font: 10pt \"Noto Serif\";\n"
                            "border-radius:7px;\n"
                            "border:1px solid rgba(255,255,255,40);\n"
                            "}")
        if x and y and w and h:
            self.setGeometry(QRect(x, y, w, h))


class GroupBox(QGroupBox):
    """Формат вызова (self, место по x, место по y, ширина, высота)"""
    def __init__(self, place, x = None, y = None, w = None, h = None):
        super().__init__(place)
        self.setStyleSheet("border-radius:7px;\n"
                            "border:1px solid rgba(255,255,255,40)")
        if x and y and w and h:
            self.setGeometry(QRect(x, y, w, h))


class LineEdit(QLineEdit):
    """Формат вызова (self, место по x, место по y, ширина, высота)"""
    def __init__(self, place,  x = None, y = None, w = None, h = None):
        super().__init__(place)
        self.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0.0454545 rgba(188, 55, 255, 144), stop:0.164773 rgba(80, 4, 197, 146), stop:0.272727 rgba(75, 46, 213, 162), stop:0.369318 rgba(162, 36, 251, 175), stop:0.494318 rgba(185, 98, 237, 175), stop:0.590909 rgba(231, 69, 222, 130), stop:0.698864 rgba(209, 36, 185, 188), stop:0.789773 rgba(189, 0, 122, 140), stop:0.897727 rgba(107, 10, 204, 153), stop:1 rgba(100, 0, 219, 157));\n"
                            "font: 10pt \"Noto Serif\";\n"
                            "border-radius:7px;\n"
                            "border:1px solid rgba(255,255,255,40);")
        if x and y and w and h:
            self.setGeometry(QRect(x, y, w, h))


class Widget(QWidget):
    def __init__(self):
        super().__init__()


        

        

