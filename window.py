""" 
Файл в котором, размещены кнопки,
указанны ссылки на собития и указаны
ссылки на стили 
"""

from widgets import Lable, Button, GroupBox, LineEdit, Widget
from PySide6.QtWidgets import QMainWindow
from events import getCoordinateRequest, transformationCoordinate, transformationDecimalOnDegries, filingTableCoordinate, writeCoordinateToExcel, openFile, recordingGeografyСoordinates, openFolder
from multiprocessing import Process
import json


with open("apiKey.json", "r", encoding = "UTF-8") as file:

    apiKey = json.load(file)["apiKey"]

info = "Правила пользования программой.\nВ этой программе вы сможете преобразовать десятичные данные в нормальный вид и записать все в таблицу \nТак же найти коардинаты объекта по его названию, но не более 500 в сутки!!!! \\n1. Выбрать таблицу формата xlsx, с которой вы будете работаь"

class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.mainWindow()
        
    def mainWindow(self):
        """Размещаем свои виджеты"""
        centralWidget = Widget() #Создали центарльный виджет в котором будут располагаться другие виджеты
        self.setCentralWidget(centralWidget) #Разместили центральныйтвиджет в главном окне

        self.setStyleSheet("background-color:qconicalgradient(cx:0, cy:0, angle:135, stop:0.0454545 rgba(188, 55, 255, 144), stop:0.164773 rgba(80, 4, 197, 146), stop:0.272727 rgba(75, 46, 213, 162), stop:0.369318 rgba(162, 36, 251, 175), stop:0.494318 rgba(185, 98, 237, 175), stop:0.590909 rgba(231, 69, 222, 130), stop:0.698864 rgba(209, 36, 185, 188), stop:0.789773 rgba(189, 0, 122, 140), stop:0.897727 rgba(107, 10, 204, 153), stop:1 rgba(100, 0, 219, 157));\n"
                            "font: 10pt \"Noto Serif\";")
        
        LabelInfo = Lable(centralWidget, x = 4, y = 4, w = 916, h = 414, text = info)

        GroupBoxUseCastomFuncion = GroupBox(centralWidget, x = 4, y = 490, w =916 , h = 30) #Создали коробку для кнопок паузы, и возабновления
        ButtonTransformGD = Button(GroupBoxUseCastomFuncion, text = "Пересчитать из градусов в десятичные", x = 4, y = 4, w = 300, h = 22)
        ButtonTransformGD.clicked.connect(lambda: LabelError.setText("Еще так не может, надо? Обращайтесь!"))
        ButtonTransformDG = Button(GroupBoxUseCastomFuncion, text = "Пересчитать из десятичных в градусы", x = 308, y = 4, w = 300, h = 22)
        ButtonTransformDG.clicked.connect(lambda: recordingGeografyСoordinates(LineEditPathFile.text(), getInfo = LabelError))
        ButtonParse = Button(GroupBoxUseCastomFuncion, text = "Найти коардинаты объекта по названию", x = 612, y = 4, w = 300, h = 22)
        ButtonParse.clicked.connect(lambda: filingTableCoordinate(LineEditPathFile.text(), apiKey, getInfo = LabelError))

        GroupBoxChangeFile = GroupBox(centralWidget, x = 20, y = 524, w = 661, h = 30) #Создали коробку для размещения опций выбора источника потока/изображения/видео
        ButtonChangeFile = Button(GroupBoxChangeFile, text = "Выбрать", x = 4, y = 4, w = 96, h = 22) #Создали кнопку выбора
        ButtonChangeFile.clicked.connect(lambda: openFile(LineEditPathFile))
        LineEditPathFile= LineEdit(GroupBoxChangeFile, x = 106, y = 4, w = 449, h = 22) #Создали строку ввода (вводится автоматически при выобре пути, через кнопку Change или можно ввести вручную и нажать кнопуку Open)

        GroupBoxChangeFolder = GroupBox(centralWidget, x = 20, y = 458, w = 661, h = 30) #Создали коробку для размещения опций выбора источника потока/изображения/видео
        ButtonChangeFolder = Button(GroupBoxChangeFolder, text = "Выбрать", x = 4, y = 4, w = 96, h = 22) #Создали кнопку выбора
        ButtonChangeFolder.clicked.connect(lambda: openFolder(LineEditPathFolder))
        LineEditPathFolder= LineEdit(GroupBoxChangeFolder, x = 106, y = 4, w = 449, h = 22)

        GroupBoxUseCastomFuncionFolder = GroupBox(centralWidget, x = 4, y = 424, w =916 , h = 30) #Создали коробку для кнопок паузы, и возабновления
        ButtonUseFuction1 = Button(GroupBoxUseCastomFuncionFolder, text = "Кнопка1", x = 4, y = 4, w = 300, h = 22)
        ButtonUseFuction1.clicked.connect(lambda: LabelError.setText("Еще так не может, надо? Обращайтесь!"))
        ButtonUseFuction2 = Button(GroupBoxUseCastomFuncionFolder, text = "Кнопка2", x = 308, y = 4, w = 300, h = 22)
        ButtonUseFuction2.clicked.connect(lambda: LabelError.setText("Еще так не может, надо? Обращайтесь!"))
        ButtonUseFuction3 = Button(GroupBoxUseCastomFuncionFolder, text = "Кнопка3", x = 612, y = 4, w = 300, h = 22)
        ButtonUseFuction3.clicked.connect(lambda: LabelError.setText("Еще так не может, надо? Обращайтесь!"))

        ButtonClose = Button(centralWidget, text = "Закрыть", x = 700, y = 524, w = 201, h = 30) #Создали кнопку закрытия
        ButtonClose.clicked.connect(self.close) #Закрываем приложение

        LabelError = Lable(centralWidget, x = 20, y = 558, w = 661, h = 47)
    