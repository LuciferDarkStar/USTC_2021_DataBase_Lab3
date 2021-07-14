import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
import time
from LINK_ACCOUNT import Ui_Form

class link_account(QWidget):
    def __init__(self):
        super(link_account, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Link)

    def Link(self):
        user_id = self.ui.lineEdit.text()
        account_id = self.ui.lineEdit_2.text()
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        if len(user_id)>0 and len(account_id)>0:
            cursor = db.cursor()
            cursor.execute("select * from Customer where user_id=%s;" % user_id)
            info1 = cursor.fetchone()
            cursor.execute("select * from Account where Account_ID=%s;" % account_id)
            info2 =cursor.fetchone()
            if str(info1)=="None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
            elif str(info2)=="None":
                QMessageBox.information(self, '提示', "不存在此账户！", QMessageBox.Close, QMessageBox.Close)
            else:
                cursor.execute("select Account_RegBank from CheckAccount where Account_ID=%s;" % account_id)
                info1 = cursor.fetchone()
                cursor.execute("select Account_RegBank from DepositAccount where Account_ID=%s;" % account_id)
                info2 = cursor.fetchone()
                if str(info1) == "None":
                    try:
                        sql="insert into Customer_DepositAccount value(%s,%s,%s,%s);"
                        cursor.execute(sql,(user_id,info2[0],account_id,str(date)))
                        db.commit()
                        QMessageBox.information(self, '提示', '关联成功!', QMessageBox.Close, QMessageBox.Close)
                    except Exception as e:
                        inf = '失败：' + e.args[1] + '!'
                        db.rollback()
                        QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)

                else:
                    try:
                        sql="insert into Customer_checkAccount value(%s,%s,%s,%s);"
                        cursor.execute(sql,(user_id,info1[0],account_id,str(date)))
                        db.commit()
                        QMessageBox.information(self, '提示', '关联成功!', QMessageBox.Close, QMessageBox.Close)
                    except Exception as e:
                        inf = '失败：' + e.args[1] + '!'
                        db.rollback()
                        QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)


        else:
            QMessageBox.information(self, '提示', "相关信息不能为空！", QMessageBox.Close, QMessageBox.Close)
        db.close()