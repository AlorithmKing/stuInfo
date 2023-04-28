import sys

import PySide6
from PyQt6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
import openpyxl

C_Score = []
Python_Score = []
English_Score = []
workbook = openpyxl.load_workbook('./学生成绩信息.xlsx')
if workbook:
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, min_col=5, max_col=7):
        C_Score.append(row[0].value)
        Python_Score.append(row[1].value)
        English_Score.append(row[2].value)


class ChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cseries = QLineSeries()
        pseries = QLineSeries()
        eseries = QLineSeries()
        # 设置图表标题
        cseries.setName("C语言成绩")
        pseries.setName("Python成绩")
        eseries.setName("英语成绩")

        for i in range(0, len(C_Score)):
            cseries.append(i, C_Score[i])
            pseries.append(i, Python_Score[i])
            eseries.append(i, English_Score[i])
        chart = QChart()
        # 设置图表标题
        chart.setTitle("学生成绩信息")
        # 设置图标坐标轴标尺
        chart.setAnimationOptions(QChart.SeriesAnimations)
        # 添加图表序列
        chart.legend().setVisible(True)

        chart.addSeries(cseries)
        chart.addSeries(pseries)
        chart.addSeries(eseries)
        # 创建坐标轴

        chart.createDefaultAxes()
        # 设置x轴刻度
        chart.axisX().setTickCount(15)
        chart.axisX().setRange(0, len(C_Score))
        # 设置y轴刻度
        chart.axisY().setTickCount(10)
        chart.axisY().setRange(0, 100)
        chartView = QChartView(chart)
        self.setCentralWidget(chartView)
        self.resize(800, 600)
        self.setWindowTitle("Qt Charts Example")




