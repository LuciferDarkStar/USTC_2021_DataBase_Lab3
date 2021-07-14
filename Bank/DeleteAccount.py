import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt
from DELETE_ACCOUNT import Ui_Form

class delete_account(QWidget):
    def __init__(self):
        super(delete_account, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.confirm)
        self.ui.pushButton_2.clicked.connect(self.delete)

    def confirm(self):
        ID = self.ui.lineEdit.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        if len(ID)>0:
            cursor.execute("select * from account where Account_ID=%s;" % ID)
            db.close()
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此账户！", QMessageBox.Close, QMessageBox.Close)
                self.ui.lineEdit_2.setText(None)
                self.ui.lineEdit_3.setText(None)
                self.ui.lineEdit_4.setText(None)
                self.ui.lineEdit_5.setText(None)
                self.ui.lineEdit_6.setText(None)
                self.ui.lineEdit_7.setText(None)
                self.ui.lineEdit_8.setText(None)
                self.ui.pushButton_2.setEnabled(False)
            else:
                self.ui.pushButton_2.setEnabled(True)
                self.ui.lineEdit_2.setText(str(info[1]))
                self.ui.lineEdit_3.setText(str(info[2]))
                self.ui.lineEdit_4.setText(str(info[3]))
                db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                     charset="utf8")
                cursor = db.cursor()
                cursor.execute("select * from CheckAccount where Account_ID=%s;" % ID)
                info = cursor.fetchone()
                if str(info) == "None":
                    cursor.execute("select * from DepositAccount where Account_ID=%s;" % ID)
                    info = cursor.fetchone()
                    self.ui.lineEdit_5.setText(str("储蓄账户"))
                    self.ui.lineEdit_6.setText(str(info[4]))
                    self.ui.lineEdit_7.setText(str(info[5]))
                    self.ui.lineEdit_8.setText(None)
                else:
                    self.ui.lineEdit_5.setText(str("支票账户"))
                    self.ui.lineEdit_8.setText(str(info[4]))
                    self.ui.lineEdit_6.setText(None)
                    self.ui.lineEdit_7.setText(None)
                db.close()
        else:
            QMessageBox.information(self, '提示', "账户ID不能为空！", QMessageBox.Close, QMessageBox.Close)
            db.close()
            self.ui.pushButton_2.setEnabled(False)
            self.ui.lineEdit_2.setText(None)
            self.ui.lineEdit_3.setText(None)
            self.ui.lineEdit_4.setText(None)
            self.ui.lineEdit_5.setText(None)
            self.ui.lineEdit_6.setText(None)
            self.ui.lineEdit_7.setText(None)
            self.ui.lineEdit_8.setText(None)

    def delete(self):
        ID = self.ui.lineEdit.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        try:
            cursor.execute("delete from Customer_CheckAccount where Account_ID=%s;" % ID)
            cursor.execute("delete from Customer_DepositAccount where Account_ID=%s;" % ID)
            cursor.execute("delete from CheckAccount where Account_ID=%s;" % ID)
            cursor.execute("delete from DepositAccount where Account_ID=%s;" % ID)
            cursor.execute("delete from Account where Account_ID=%s;" % ID)
            db.commit()
            QMessageBox.information(self, '提示', '销户成功!', QMessageBox.Close, QMessageBox.Close)
            self.ui.pushButton_2.setEnabled(False)
        except Exception as e:
            inf='失败：'+e.args[1]+'!'
            db.rollback()
            QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            self.ui.pushButton_2.setEnabled(False)
        finally:
            db.close()