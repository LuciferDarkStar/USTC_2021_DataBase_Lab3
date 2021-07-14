import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox,QTableWidgetItem
from PyQt5.QtCore import QDate, Qt

from FIND_LOAN import Ui_Form

class find_loan(QWidget):
    def __init__(self):
        super(find_loan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.FL)

    def FL(self):
        self.ui.lineEdit_2.setText(None)
        self.ui.lineEdit_3.setText(None)
        self.ui.lineEdit_4.setText(None)
        self.ui.lineEdit_5.setText(None)
        self.ui.lineEdit_6.setText(None)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.clearContents()
        ID=self.ui.lineEdit.text()
        if len(ID)==0:
            QMessageBox.information(self, '提示', "贷款ID不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
            cursor = db.cursor()
            cursor.execute("select * from loan where loan_id=%s;"%ID)
            info1=cursor.fetchone()
            if str(info1)=="None":
                QMessageBox.information(self, '提示', "不存在相关贷款记录！", QMessageBox.Close, QMessageBox.Close)
            else:
                self.ui.lineEdit_2.setText(str(info1[1]))
                self.ui.lineEdit_3.setText(str(info1[2]))
                cursor.execute("select user_id from Loan_Customer where loan_id=%s;" % ID)
                info2=cursor.fetchall()
                if len(info2) > 0:
                    for line in info2:
                        row = self.ui.tableWidget.currentRow()
                        self.ui.tableWidget.insertRow(row + 1)
                        newItem = QTableWidgetItem(str(line[0]))
                        self.ui.tableWidget.setItem(0, 0, newItem)
                cursor.execute("select pay_money,pay_date from Pay where loan_id=%s;" % ID)
                info3 = cursor.fetchall()
                if len(info3) > 0:
                    for line in info3:
                        row = self.ui.tableWidget_2.currentRow()
                        self.ui.tableWidget_2.insertRow(row + 1)
                        newItem = QTableWidgetItem(str(line[0]))
                        self.ui.tableWidget_2.setItem(0, 0, newItem)
                        newItem = QTableWidgetItem(str(line[1]))
                        self.ui.tableWidget_2.setItem(0, 1, newItem)
                cursor.execute("select SUM(pay_money) from Pay where loan_id=%s;" % ID)
                info4 = cursor.fetchone()
                if str(info4[0]) == "None":
                    s = 0.0
                else:
                    s = float(info4[0])
                s2=float(info1[2])-s
                self.ui.lineEdit_4.setText(str(s))
                self.ui.lineEdit_5.setText(str(s2))
                if s==0:
                    self.ui.lineEdit_6.setText("未开始发放")
                elif s2>0:
                    self.ui.lineEdit_6.setText("发放中")
                else:
                    self.ui.lineEdit_6.setText("已全部发放")
            db.close()