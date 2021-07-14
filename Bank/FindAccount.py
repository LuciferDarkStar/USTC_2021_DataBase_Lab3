import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox,QTableWidgetItem
from FIND_ACCOUNT import Ui_Form

class find_account(QWidget):
    def __init__(self):
        super(find_account, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_5.clicked.connect(self.Find1)

    def Find1(self):
        ID = self.ui.lineEdit_9.text()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        if len(ID)==0:
            QMessageBox.information(self, '提示', "账户ID不能为空！", QMessageBox.Close, QMessageBox.Close)
            db.close()
        else:
            cursor.execute("select * from account where account_id=%s;"%ID)
            info=cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
            else:
                cursor.execute("select * from DepositAccount where account_id=%s;"%ID)
                info1=cursor.fetchone()
                cursor.execute("select * from CheckAccount where account_id=%s;" % ID)
                info2 = cursor.fetchone()
                if str(info2)=="None":
                    self.ui.lineEdit_10.setText(str(info1[1]))
                    self.ui.lineEdit_11.setText(str(info1[2]))
                    self.ui.lineEdit_12.setText(str(info1[3]))
                    self.ui.lineEdit_13.setText("储蓄账户")
                    self.ui.lineEdit_14.setText(str(info1[4]))
                    self.ui.lineEdit_15.setText(str(info1[5]))
                    self.ui.lineEdit_16.setText(None)
                    cursor.execute("select user_id,LastView_D from Customer_DepositAccount where account_id=%s;"%ID)
                    info3=cursor.fetchall()
                    if len(info3)>0:
                        for line in info3:
                            row = self.ui.tableWidget.currentRow()
                            self.ui.tableWidget.insertRow(row + 1)
                            newItem = QTableWidgetItem(str(line[0]))
                            self.ui.tableWidget.setItem(0, 0, newItem)
                            newItem = QTableWidgetItem(str(line[1]))
                            self.ui.tableWidget.setItem(0, 1, newItem)
                else:
                    self.ui.lineEdit_10.setText(str(info2[1]))
                    self.ui.lineEdit_11.setText(str(info2[2]))
                    self.ui.lineEdit_12.setText(str(info2[3]))
                    self.ui.lineEdit_13.setText("支票账户")
                    self.ui.lineEdit_14.setText(None)
                    self.ui.lineEdit_15.setText(None)
                    self.ui.lineEdit_16.setText(str(info2[4]))
                    cursor.execute("select user_id,LastView_C from Customer_CheckAccount where account_id=%s;" % ID)
                    info3 = cursor.fetchall()
                    if len(info3) > 0:
                        for line in info3:
                            row = self.ui.tableWidget.currentRow()
                            self.ui.tableWidget.insertRow(row + 1)
                            newItem = QTableWidgetItem(str(line[0]))
                            self.ui.tableWidget.setItem(0, 0, newItem)
                            newItem = QTableWidgetItem(str(line[1]))
                            self.ui.tableWidget.setItem(0, 1, newItem)
            db.close()