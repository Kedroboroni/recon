import requests
import json
from openpyxl import load_workbook
import openpyxl
from PySide6.QtWidgets import  QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Slot, QUrl, QTimer

#from docx.shared import Pt
#from docx.enum.text import WD_ALIGN_PARAGRAPH
#from docx.shared import RGBColor

#Использую символы: ° ′ ″ для форматирования градусов, минут, секунд соответсвенно

apiKey =  'b25d4bd7-6564-4cb9-8a26-5b1f1c9a414b'
fileName = "testTable.xlsx"

def getCoordinateRequest(namePlace, apiKey):

    try:

        # Вернет кортеж (широта, долгота) в десятичном представлении
        lang = 'ru_RU'
        req = requests.get(f'https://search-maps.yandex.ru/v1/?apikey={apiKey}&text={namePlace}&lang={lang}')
        #print(req.json())
        feature = req.json()['features'][0]# Извлечение координат
        coordinates = feature['geometry']['coordinates']
        #print(f"\n Coordinate: {coordinates[1]}, {coordinates[0]} ")
        return (coordinates[1], coordinates[0])
    
    except:
        return ("ОШИБКА", "ОШИБКА")


def transformationCoordinate(latitudeDecimal, longitudeDecimal):

    #вернет словарь {latitudeGeografy:"строкаШироты" longitudeGeografy "строкаДолготы"}
    latitudeGeografy = transformationDecimalOnDegries(latitudeDecimal)
    longitudeGeografy = transformationDecimalOnDegries(longitudeDecimal)
    #print(f"А так мы их отформатировали: \nlatitudeGeografy: {latitudeGeografy[0]}°{latitudeGeografy[1]}′{latitudeGeografy[2]}″ \nlongitudeGeografy: {longitudeGeografy[0]}°{longitudeGeografy[1]}′{longitudeGeografy[2]}″")

    return {"latitudeGeografy": f"{latitudeGeografy[0]}°{latitudeGeografy[1]}′{latitudeGeografy[2]}″", "longitudeGeografy" : f"{longitudeGeografy[0]}°{longitudeGeografy[1]}′{longitudeGeografy[2]}″"}


def transformationDecimalOnDegries(values):

    abs_decimal = abs(values)
    degrees = int(abs_decimal)
    minutes = int((abs_decimal - degrees) * 60)
    seconds = round((abs_decimal - degrees - minutes / 60) * 3600, 2)
    #print(f"Работа функции трансформации дестичных градусов в нормальные{(degrees, minutes, seconds)}")

    return (degrees, minutes, seconds)


def filingTableCoordinate(fileName, apiKey, getInfo = None):

    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.active
    for rowNumber in range(1,sheet.max_row+1):
        namePlace = sheet.cell(row = rowNumber, column = 1).value

        decimalCoordinate = getCoordinateRequest(namePlace, apiKey) #Кортеж с широтой и долготой

        try:

            geografyCoordinate = transformationCoordinate(decimalCoordinate[0], decimalCoordinate[1]) #Слоаврь со строками
            writeCoordinateToExcel(workbook, fileName, rowNumber, 2, decimalCoordinate[0], decimalCoordinate[1], geografyCoordinate["latitudeGeografy"], geografyCoordinate["longitudeGeografy"])

            if getInfo:
                getInfo.setText("Объекты найдены успешно!")

        except:
            writeCoordinateToExcel(workbook, fileName, rowNumber, 2, "ОШИБКА", "ОШИБКА", "ОШИБКА", "ОШИБКА")


def writeCoordinateToExcel(workbook, fileName, row_number, column_number, value1, value2, value3, value4):

    sheet = workbook.active
    sheet.cell(row=row_number, column=column_number).value = value1
    sheet.cell(row=row_number, column=column_number+1).value = value2

    sheet.cell(row=row_number, column=column_number+2).value = value3
    sheet.cell(row=row_number, column=column_number+3).value = value4
    workbook.save(fileName)


@Slot()
def openFile(parent):
    options = QFileDialog.Options()
    fileName, _ = QFileDialog.getOpenFileName(parent, options=options)
    if fileName:
        parent.setText(fileName)



def recordingGeografyСoordinates(fileName, getInfo = None):
    workbook = openpyxl.load_workbook(fileName)
    sheet = workbook.active
    for rowNumber in range(1,sheet.max_row+1):

        try:

            recordGeographyCoordinate = transformationCoordinate(sheet.cell(row = rowNumber, column = 1).value, sheet.cell(row = rowNumber, column = 2).value)
            sheet.cell(row=rowNumber, column=3).value = recordGeographyCoordinate["latitudeGeografy"]
            sheet.cell(row=rowNumber, column=4).value = recordGeographyCoordinate["longitudeGeografy"]

        except:
            sheet.cell(row=rowNumber, column=3).value ="ОШИБКА"
            sheet.cell(row=rowNumber, column=4).value = "ОШИБКА"

    if getInfo:
        getInfo.setText("Перобразование успшно произошло")
    workbook.save(fileName)
