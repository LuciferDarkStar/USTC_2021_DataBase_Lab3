import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from LOAN_SUM import Ui_Form


class loan_sum(QWidget):
    def __init__(self):
        super(loan_sum, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.month)
        self.ui.pushButton.clicked.connect(self.season)
        self.ui.pushButton.clicked.connect(self.years)

    def month(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.clearContents()
        self.ui.tableWidget_4.setRowCount(0)
        self.ui.tableWidget_4.clearContents()
        bank = self.ui.comboBox.currentText()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        sql1 = "select DATE_FORMAT(Pay_Date,'%%Y-%%m') as month,SUM(Pay_money) as ss from pay,loan " \
               "where " \
               "DATE_FORMAT(Pay_Date,'%%Y-%%m')>DATE_FORMAT(date_sub(curdate(), interval 12 month),'%%Y-%%m') " \
               "and pay.loan_id=loan.loan_id and Bank_Name=%s group by month; "

        cursor.execute(sql1, bank)
        info1 = cursor.fetchall()

        if len(info1) != 0:
            for line in info1:
                row = self.ui.tableWidget.currentRow()
                self.ui.tableWidget.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget.setItem(0, 1, newItem)

        sql2 = "select DATE_FORMAT(Pay_Date,'%%Y-%%m') as month,count(distinct pay.loan_id) as ss from pay,loan " \
               "where " \
               "DATE_FORMAT(Pay_Date,'%%Y-%%m')>DATE_FORMAT(date_sub(curdate(), interval 12 month),'%%Y-%%m') " \
               "and pay.loan_id=loan.loan_id and Bank_Name=%s group by month; "

        cursor.execute(sql2, bank)
        info2 = cursor.fetchall()

        if len(info2) != 0:
            for line in info2:
                row = self.ui.tableWidget_4.currentRow()
                self.ui.tableWidget_4.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget_4.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget_4.setItem(0, 1, newItem)
        db.close()

    def season(self):
        self.ui.tableWidget_2.setRowCount(0)
        self.ui.tableWidget_2.clearContents()
        self.ui.tableWidget_5.setRowCount(0)
        self.ui.tableWidget_5.clearContents()
        bank = self.ui.comboBox.currentText()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        sql1 = "SELECT QUARTER(Pay_Date) createTime,sum(Pay_money) SS FROM pay,loan where pay.loan_id=loan.loan_id " \
               "and Bank_Name=%s" \
               "GROUP BY QUARTER(" \
               "Pay_Date) ORDER BY QUARTER(Pay_Date) DESC; "
        cursor.execute(sql1, bank)
        info1 = cursor.fetchall()
        if len(info1) != 0:
            for line in info1:
                row = self.ui.tableWidget_2.currentRow()
                self.ui.tableWidget_2.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget_2.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget_2.setItem(0, 1, newItem)

        sql2 = "SELECT QUARTER(Pay_Date) createTime,count(distinct pay.loan_id) SS FROM pay,loan where " \
               "pay.loan_id=loan.loan_id " \
               "and Bank_Name=%s" \
               "GROUP BY QUARTER(" \
               "Pay_Date) ORDER BY QUARTER(Pay_Date) DESC; "
        cursor.execute(sql2, bank)
        info2 = cursor.fetchall()
        if len(info2) != 0:
            for line in info2:
                row = self.ui.tableWidget_5.currentRow()
                self.ui.tableWidget_5.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget_5.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget_5.setItem(0, 1, newItem)
        db.close()

    def years(self):
        self.ui.tableWidget_3.setRowCount(0)
        self.ui.tableWidget_3.clearContents()

        self.ui.tableWidget_6.setRowCount(0)
        self.ui.tableWidget_6.clearContents()
        bank = self.ui.comboBox.currentText()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        sql1 = "SELECT YEAR(Pay_Date) createTime,sum(Pay_money) SS FROM pay,loan where pay.loan_id=loan.loan_id " \
               "and Bank_Name=%s" \
               "GROUP BY YEAR(" \
               "Pay_Date) ORDER BY YEAR(Pay_Date) DESC; "
        cursor.execute(sql1, bank)
        info1 = cursor.fetchall()
        if len(info1) != 0:
            for line in info1:
                row = self.ui.tableWidget_3.currentRow()
                self.ui.tableWidget_3.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget_3.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget_3.setItem(0, 1, newItem)
        sql2 = "SELECT YEAR(Pay_Date) createTime,count(distinct pay.loan_id) SS FROM pay,loan where " \
               "pay.loan_id=loan.loan_id " \
               "and Bank_Name=%s" \
               "GROUP BY YEAR(" \
               "Pay_Date) ORDER BY YEAR(Pay_Date) DESC; "
        cursor.execute(sql2, bank)
        info2 = cursor.fetchall()
        if len(info2) != 0:
            for line in info2:
                row = self.ui.tableWidget_6.currentRow()
                self.ui.tableWidget_6.insertRow(row + 1)
                newItem = QTableWidgetItem(str(line[0]))
                self.ui.tableWidget_6.setItem(0, 0, newItem)
                newItem = QTableWidgetItem(str(line[1]))
                self.ui.tableWidget_6.setItem(0, 1, newItem)
        db.close()