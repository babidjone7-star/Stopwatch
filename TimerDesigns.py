# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimerDesign.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(216, 171)
        Dialog.setStyleSheet(u"")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 11, 201, 158))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Timer = QTimeEdit(self.widget)
        self.Timer.setObjectName(u"Timer")
        self.Timer.setStyleSheet(u"color: black;\n"
"font: 9pt \"Segoe Script\";")

        self.verticalLayout.addWidget(self.Timer)

        self.StartButton = QPushButton(self.widget)
        self.StartButton.setObjectName(u"StartButton")
        self.StartButton.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 9pt \"Segoe Print\";")

        self.verticalLayout.addWidget(self.StartButton)

        self.ResetButton = QPushButton(self.widget)
        self.ResetButton.setObjectName(u"ResetButton")
        self.ResetButton.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 9pt \"Segoe Print\";\n"
"")

        self.verticalLayout.addWidget(self.ResetButton)

        self.StopButton = QPushButton(self.widget)
        self.StopButton.setObjectName(u"StopButton")
        self.StopButton.setStyleSheet(u"color: white;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 9pt \"Segoe Print\";")

        self.verticalLayout.addWidget(self.StopButton)

        self.TimeLabel = QLabel(self.widget)
        self.TimeLabel.setObjectName(u"TimeLabel")
        self.TimeLabel.setStyleSheet(u"font: 10pt \"Segoe Script\";")

        self.verticalLayout.addWidget(self.TimeLabel)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.StartButton.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.ResetButton.setText(QCoreApplication.translate("Dialog", u"Reset", None))
        self.StopButton.setText(QCoreApplication.translate("Dialog", u"Stop", None))
        self.TimeLabel.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u0430 \u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c!", None))
    # retranslateUi
