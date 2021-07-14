import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt

from ALTER_ACCOUNT import Ui_Form

class alter_account(QWidget):
    def __init__(self):
        super(alter_account, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.confirm)
        self.ui.pushButton_2.clicked.connect(self.alter)

    def confirm(self):
        ID = self.ui.lineEdit.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        self.ui.lineEdit_5.setText(None)
        if len(ID)>0:
            cursor.execute("select * from account where Account_ID=%s;" % ID)
            db.close()
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此账户！", QMessageBox.Close, QMessageBox.Close)
                self.ui.pushButton_2.setEnabled(False)
            else:
                db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                     charset="utf8")
                cursor = db.cursor()
                cursor.execute("select * from DepositAccount where Account_ID=%s;" % ID)
                info1= cursor.fetchone()
                cursor.execute("select * from CheckAccount where Account_ID=%s;" % ID)
                info2 = cursor.fetchone()
                db.close()
                if str(info2)=="None":
                    self.ui.pushButton_2.setEnabled(True)
                    self.ui.lineEdit_2.setText(str(info1[1]))
                    self.ui.lineEdit_3.setText(str(info1[4]))
                    if str(info1[5])=="人名币":
                        self.ui.comboBox_3.setCurrentIndex(0)
                    elif str(info1[5])=="美元":
                        self.ui.comboBox_3.setCurrentIndex(1)
                    else:
                        self.ui.comboBox_3.setCurrentIndex(2)
                    self.ui.lineEdit_4.setText(None)
                    self.ui.lineEdit_5.setText(None)
                else:
                    self.ui.pushButton_2.setEnabled(True)
                    self.ui.lineEdit_2.setText(str(info2[1]))
                    self.ui.lineEdit_4.setText(str(info2[4]))
                    self.ui.lineEdit_3.setText(None)
                    self.ui.lineEdit_5.setText(None)

        else:
            QMessageBox.information(self, '提示', "账户ID不能为空！", QMessageBox.Close, QMessageBox.Close)
            db.close()
            self.ui.pushButton_2.setEnabled(False)
            self.ui.lineEdit_2.setText(None)
            self.ui.lineEdit_3.setText(None)
            self.ui.lineEdit_4.setText(None)
            self.ui.lineEdit_5.setText(None)

    def alter(self):
        ID = self.ui.lineEdit.text()
        currtype = self.ui.comboBox_3.currentText()
        money = self.ui.lineEdit_2.text()
        rate = self.ui.lineEdit_3.text()
        overflow=self.ui.lineEdit_4.text()
        user_id=self.ui.lineEdit_5.text()
        if len(overflow)==0:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            sql1="update account set Account_Money=%s where account_id=%s;"
            sql2="update DepositAccount set Account_Money=%s,InterestRate=%s,Currencytype=%s where account_id=%s;"
            sql3="delete from Customer_DepositAccount where account_id=%s and user_id=%s;"
            try:
                cursor.execute(sql1,(money,ID))
                cursor.execute(sql2, (money, rate,currtype,ID))
                if len(user_id)>0:
                    cursor.execute(sql3,(ID,user_id))
                db.commit()
                QMessageBox.information(self, '提示', '修改账户信息成功!', QMessageBox.Close, QMessageBox.Close)
            except Exception as e:
                inf = '失败：' + e.args[1] + '!'
                db.rollback()
                QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            sql1 = "update account set Account_Money=%s where account_id=%s;"
            sql2 = "update CheckAccount set Account_Money=%s,Overdraft=%s where account_id=%s;"
            sql3 = "delete from Customer_CheckAccount where account_id=%s and user_id=%s;"
            try:
                cursor.execute(sql1,(money,ID))
                cursor.execute(sql2, (money, overflow,ID))
                if len(user_id)>0:
                    cursor.execute(sql3,(ID,user_id))
                db.commit()
                QMessageBox.information(self, '提示', '修改账户信息成功!', QMessageBox.Close, QMessageBox.Close)
            except Exception as e:
                inf = '失败：' + e.args[1] + '!'
                db.rollback()
                QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
        self.ui.pushButton_2.setEnabled(False)
        db.close()