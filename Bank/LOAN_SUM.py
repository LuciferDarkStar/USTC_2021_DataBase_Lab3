# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOAN_SUM.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1060, 729)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(450, 10, 151, 51))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(530, 130, 151, 16))
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(530, 160, 261, 481))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 91, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 430, 91, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(940, 680, 111, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget_2 = QtWidgets.QTableWidget(Form)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 160, 261, 261))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        self.tableWidget_3 = QtWidgets.QTableWidget(Form)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 460, 261, 261))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        self.tableWidget_4 = QtWidgets.QTableWidget(Form)
        self.tableWidget_4.setGeometry(QtCore.QRect(790, 160, 261, 481))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(2)
        self.tableWidget_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        self.tableWidget_5 = QtWidgets.QTableWidget(Form)
        self.tableWidget_5.setGeometry(QtCore.QRect(270, 160, 261, 261))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(2)
        self.tableWidget_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        self.tableWidget_6 = QtWidgets.QTableWidget(Form)
        self.tableWidget_6.setGeometry(QtCore.QRect(270, 460, 261, 261))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(2)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 70, 293, 30))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">????????????</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "????????????(???12??????)???"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "??????"))
        self.label_4.setText(_translate("Form", "??????????????????"))
        self.label_5.setText(_translate("Form", "???????????????"))
        self.pushButton_2.setText(_translate("Form", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Form", "?????????"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Form", "?????????"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Form", "??????"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Form", "?????????"))
        self.label_2.setText(_translate("Form", "?????????"))
        self.comboBox.setItemText(0, _translate("Form", "????????????"))
        self.comboBox.setItemText(1, _translate("Form", "????????????"))
        self.pushButton.setText(_translate("Form", "??????"))

