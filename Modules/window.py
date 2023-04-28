# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowLAAUhf.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
from .rc_resource import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(966, 701)
        icon = QIcon()
        icon.addFile(u":/icon/icon/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(252, 255, 230);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"border-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgba(174, 99, 255,150), stop:1 rgba(255, 255, 255, 0));")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame\n"
"{\n"
"background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0,stop:0 rgba(174, 99, 255,150), stop:1 rgba(255, 255, 255, 0));	\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.btn_Login = QPushButton(self.frame_2)
        self.btn_Login.setObjectName(u"btn_Login")

        self.verticalLayout.addWidget(self.btn_Login)

        self.btn_PersonalInfo = QPushButton(self.frame_2)
        self.btn_PersonalInfo.setObjectName(u"btn_PersonalInfo")

        self.verticalLayout.addWidget(self.btn_PersonalInfo)

        self.btn_PersonScores = QPushButton(self.frame_2)
        self.btn_PersonScores.setObjectName(u"btn_PersonScores")

        self.verticalLayout.addWidget(self.btn_PersonScores)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.btn_exit = QPushButton(self.frame_2)
        self.btn_exit.setObjectName(u"btn_exit")

        self.verticalLayout.addWidget(self.btn_exit)


        self.horizontalLayout_4.addWidget(self.frame_2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(173, 182, 229, 100);")
        self.Info = QWidget()
        self.Info.setObjectName(u"Info")
        self.horizontalLayout_3 = QHBoxLayout(self.Info)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.Info)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_2.addWidget(self.label_8)

        self.cbx_search = QComboBox(self.frame_5)
        self.cbx_search.addItem("")
        self.cbx_search.addItem("")
        self.cbx_search.addItem("")
        self.cbx_search.addItem("")
        self.cbx_search.setObjectName(u"cbx_search")

        self.horizontalLayout_2.addWidget(self.cbx_search)

        self.line_search = QLineEdit(self.frame_5)
        self.line_search.setObjectName(u"line_search")

        self.horizontalLayout_2.addWidget(self.line_search)

        self.btn_search = QPushButton(self.frame_5)
        self.btn_search.setObjectName(u"btn_search")

        self.horizontalLayout_2.addWidget(self.btn_search)

        self.btn_delete = QPushButton(self.frame_5)
        self.btn_delete.setObjectName(u"btn_delete")

        self.horizontalLayout_2.addWidget(self.btn_delete)

        self.btn_insert = QPushButton(self.frame_5)
        self.btn_insert.setObjectName(u"btn_insert")

        self.horizontalLayout_2.addWidget(self.btn_insert)

        self.btn_import = QPushButton(self.frame_5)
        self.btn_import.setObjectName(u"btn_import")

        self.horizontalLayout_2.addWidget(self.btn_import)

        self.btn_export = QPushButton(self.frame_5)
        self.btn_export.setObjectName(u"btn_export")

        self.horizontalLayout_2.addWidget(self.btn_export)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.info_table = QTableWidget(self.Info)
        self.info_table.setObjectName(u"info_table")

        self.verticalLayout_2.addWidget(self.info_table)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.stackedWidget.addWidget(self.Info)
        self.Scores = QWidget()
        self.Scores.setObjectName(u"Scores")
        self.verticalLayout_6 = QVBoxLayout(self.Scores)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_6 = QFrame(self.Scores)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_5.addWidget(self.label_9)

        self.cbxscoremode = QComboBox(self.frame_6)
        self.cbxscoremode.addItem("")
        self.cbxscoremode.addItem("")
        self.cbxscoremode.setObjectName(u"cbxscoremode")

        self.horizontalLayout_5.addWidget(self.cbxscoremode)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_5.addWidget(self.label_10)

        self.cbx_score = QComboBox(self.frame_6)
        self.cbx_score.addItem("")
        self.cbx_score.addItem("")
        self.cbx_score.addItem("")
        self.cbx_score.setObjectName(u"cbx_score")

        self.horizontalLayout_5.addWidget(self.cbx_score)

        self.btn_sort = QPushButton(self.frame_6)
        self.btn_sort.setObjectName(u"btn_sort")

        self.horizontalLayout_5.addWidget(self.btn_sort)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.btn_show = QPushButton(self.frame_6)
        self.btn_show.setObjectName(u"btn_show")

        self.horizontalLayout_5.addWidget(self.btn_show)

        self.Score_import = QPushButton(self.frame_6)
        self.Score_import.setObjectName(u"Score_import")

        self.horizontalLayout_5.addWidget(self.Score_import)

        self.Score_export = QPushButton(self.frame_6)
        self.Score_export.setObjectName(u"Score_export")

        self.horizontalLayout_5.addWidget(self.Score_export)


        self.verticalLayout_5.addWidget(self.frame_6)

        self.score_table = QTableWidget(self.Scores)
        self.score_table.setObjectName(u"score_table")

        self.verticalLayout_5.addWidget(self.score_table)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.stackedWidget.addWidget(self.Scores)
        self.Login = QWidget()
        self.Login.setObjectName(u"Login")
        self.Login.setStyleSheet(u"border-radius: 10px;\n"
"border-bottom-left-radius: 0px;\n"
"color: rgb(255, 255, 255);\n"
"background-image: url(:/icon/icon/images.jpg);")
        self.verticalLayout_7 = QVBoxLayout(self.Login)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_3 = QFrame(self.Login)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.btn_log = QPushButton(self.frame_3)
        self.btn_log.setObjectName(u"btn_log")

        self.gridLayout_2.addWidget(self.btn_log, 6, 1, 1, 1)

        self.line_usr = QLineEdit(self.frame_3)
        self.line_usr.setObjectName(u"line_usr")

        self.gridLayout_2.addWidget(self.line_usr, 4, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 3, 2, 1, 1)

        self.label_5 = QLabel(self.frame_3)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 3, 1, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_13, 1, 1, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 8, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 9, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 3, 0, 1, 1)

        self.line_pwd = QLineEdit(self.frame_3)
        self.line_pwd.setObjectName(u"line_pwd")
        self.line_pwd.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.line_pwd, 5, 1, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_11, 7, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_7, 2, 1, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.Login)

        self.horizontalLayout_4.addWidget(self.stackedWidget)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.dateTimeEdit = QDateTimeEdit(self.frame)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")

        self.horizontalLayout.addWidget(self.dateTimeEdit)


        self.verticalLayout_3.addWidget(self.frame)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u4fe1\u606f\u7ba1\u7406\u7cfb\u7edf", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u6b22\u8fce\u6765\u5230\u5b66\u751f\u7ba1\u7406\u7cfb\u7edf</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u4e3b\u9875</span></p></body></html>", None))
        self.btn_Login.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
        self.btn_PersonalInfo.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u4e2a\u4eba\u4fe1\u606f", None))
        self.btn_PersonScores.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u751f\u6210\u7ee9\u4fe1\u606f", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u4e2a\u4eba\u7528\u6237", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa\u767b\u5165", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u65b9\u5f0f", None))
        self.cbx_search.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.cbx_search.setItemText(1, QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None))
        self.cbx_search.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5b66\u53f7", None))
        self.cbx_search.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e13\u4e1a", None))

        self.line_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u67e5\u8be2\u6587\u672c", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.btn_insert.setText(QCoreApplication.translate("MainWindow", u"\u63d2\u5165", None))
        self.btn_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f\u6a21\u5f0f", None))
        self.cbxscoremode.setItemText(0, QCoreApplication.translate("MainWindow", u"\u964d\u5e8f", None))
        self.cbxscoremode.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5347\u5e8f", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f\u65b9\u5f0f", None))
        self.cbx_score.setItemText(0, QCoreApplication.translate("MainWindow", u"\u82f1\u8bed", None))
        self.cbx_score.setItemText(1, QCoreApplication.translate("MainWindow", u"C\u8bed\u8a00", None))
        self.cbx_score.setItemText(2, QCoreApplication.translate("MainWindow", u"Python", None))

        self.btn_sort.setText(QCoreApplication.translate("MainWindow", u"\u6392\u5e8f", None))
        self.btn_show.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u53ef\u89c6\u5316", None))
        self.Score_import.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.Score_export.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6210\u7ee9\u8868", None))
        self.btn_log.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5165", None))
#if QT_CONFIG(shortcut)
        self.btn_log.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.line_usr.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u7528\u6237\u540d", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\">\u7528\u6237\u767b\u5165\u754c\u9762</span></p></body></html>", None))
        self.line_pwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u4f5c\u8005", None))
    # retranslateUi

