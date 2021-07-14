import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from FIND_CUSTOMER import Ui_Form

class find_customer(QWidget):
    def __init__(self):
        super(find_customer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.Find)


    def Find(self):
        ID = self.ui.lineEdit_9.text()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        if len(ID) > 0:
            cursor.execute("select * from customer where user_id=%s;" % ID)
            info = cursor.fetchone()
            cursor.execute("select Account_ID,Bank_Name from Customer_CheckAccount where user_id=%s;" % ID)
            info1 = cursor.fetchall()
            cursor.execute("select Account_ID,Bank_Name from Customer_DepositAccount where user_id=%s;" % ID)
            info2 = cursor.fetchall()
            db.close()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
                self.ui.lineEdit_10.setText(None)
                self.ui.lineEdit_11.setText(None)
                self.ui.lineEdit_12.setText(None)
                self.ui.lineEdit_13.setText(None)
                self.ui.lineEdit_14.setText(None)
                self.ui.lineEdit_15.setText(None)
                self.ui.lineEdit_16.setText(None)
            else:
                self.ui.lineEdit_10.setText(str(info[1]))
                self.ui.lineEdit_11.setText(str(info[2]))
                if str(info[3]) != "None":
                    self.ui.lineEdit_12.setText(str(info[3]))
                if str(info[4]) != "None":
                    self.ui.lineEdit_13.setText(str(info[4]))
                if str(info[5]) != "None":
                    self.ui.lineEdit_14.setText(str(info[5]))
                if str(info[6]) != "None":
                    self.ui.lineEdit_15.setText(str(info[6]))
                if str(info[7]) != "None":
                    self.ui.lineEdit_16.setText(str(info[7]))
                if len(info1)!=0:
                    for line in info1:
                        row = self.ui.tableWidget.currentRow()
                        self.ui.tableWidget.insertRow(row + 1)
                        newItem = QTableWidgetItem(str(line[0]))
                        self.ui.tableWidget.setItem(0, 0, newItem)
                        newItem = QTableWidgetItem(str(line[1]))
                        self.ui.tableWidget.setItem(0, 1, newItem)
                if len(info2)!=0:
                    for line in info2:
                        row = self.ui.tableWidget.currentRow()
                        self.ui.tableWidget.insertRow(row + 1)
                        newItem = QTableWidgetItem(str(line[0]))
                        self.ui.tableWidget.setItem(0, 0, newItem)
                        newItem = QTableWidgetItem(str(line[1]))
                        self.ui.tableWidget.setItem(0, 1, newItem)

        else:
            QMessageBox.information(self, '提示', "身份证不能为空！", QMessageBox.Close, QMessageBox.Close)
            self.ui.lineEdit_10.setText(None)
            self.ui.lineEdit_11.setText(None)
            self.ui.lineEdit_12.setText(None)
            self.ui.lineEdit_13.setText(None)
            self.ui.lineEdit_14.setText(None)
            self.ui.lineEdit_15.setText(None)
            self.ui.lineEdit_16.setText(None)