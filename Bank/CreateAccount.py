import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt

from CREATE_ACCOUNT import Ui_Form


class create_account(QWidget):
    def __init__(self):
        super(create_account, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.ui.pushButton.clicked.connect(self.Create)


    def Create(self):
        ID = self.ui.lineEdit_11.text()
        Money = self.ui.lineEdit_10.text()
        date = self.ui.dateEdit.date().toString(Qt.ISODate)
        bank = self.ui.comboBox.currentText()
        kind = self.ui.comboBox_2.currentText()
        rate = self.ui.lineEdit_12.text()
        currtype = self.ui.comboBox_3.currentText()
        overflow = self.ui.lineEdit_14.text()
        if len(ID) == 0:
            QMessageBox.information(self, '提示', "账户ID不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            user_id = self.ui.lineEdit_13.text()
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            cursor.execute("select user_id from customer where User_ID=%s;" % user_id)
            db.close()
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
            else:
                if len(Money) == 0:
                    Money = 0
                if str(kind) == "储蓄账户":
                    if len(rate) == 0:
                        QMessageBox.information(self, '提示', "相关信息不能为空！", QMessageBox.Close, QMessageBox.Close)
                    else:
                        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                             charset="utf8")
                        cursor = db.cursor()
                        sql1 = "insert into account value(%s,%s,%s,%s);"
                        sql2 = "insert into DepositAccount value(%s,%s,%s,%s,%s,%s);"
                        sql3 = "insert into Customer_DepositAccount value(%s,%s,%s,%s);"
                        try:
                            cursor.execute(sql1, (ID, Money, date, bank))
                            cursor.execute(sql2, (ID, Money, date, bank, rate, currtype))
                            cursor.execute(sql3, (user_id, bank, ID, date))
                            db.commit()
                            QMessageBox.information(self, '提示', '开户成功!', QMessageBox.Close, QMessageBox.Close)
                            self.ui.lineEdit_10.setText(None)
                            self.ui.lineEdit_11.setText(None)
                            self.ui.lineEdit_12.setText(None)
                            self.ui.lineEdit_13.setText(None)
                            self.ui.lineEdit_14.setText(None)
                        except Exception as e:
                            inf = '失败：' + e.args[1] + '!'
                            db.rollback()
                            QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
                        finally:
                            db.close()
                else:
                    if len(overflow) == 0 or float(overflow) < 0:
                        QMessageBox.information(self, '提示', "相关信息不能为空或为负值！", QMessageBox.Close, QMessageBox.Close)
                    else:
                        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                             charset="utf8")
                        cursor = db.cursor()
                        sql1 = "insert into account value(%s,%s,%s,%s);"
                        sql2 = "insert into CheckAccount value(%s,%s,%s,%s,%s);"
                        sql3 = "insert into Customer_CheckAccount value(%s,%s,%s,%s);"
                        try:
                            cursor.execute(sql1, (ID, Money, date, bank))
                            cursor.execute(sql2, (ID, Money, date, bank, overflow))
                            cursor.execute(sql3, (user_id, bank, ID, date))
                            db.commit()
                            QMessageBox.information(self, '提示', '开户成功!', QMessageBox.Close, QMessageBox.Close)
                            self.ui.lineEdit_10.setText(None)
                            self.ui.lineEdit_11.setText(None)
                            self.ui.lineEdit_12.setText(None)
                            self.ui.lineEdit_13.setText(None)
                            self.ui.lineEdit_14.setText(None)
                        except Exception as e:
                            inf = '失败：' + e.args[1] + '!'
                            db.rollback()
                            QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
                        finally:
                            db.close()
