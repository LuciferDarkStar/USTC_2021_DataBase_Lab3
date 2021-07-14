import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox
from DELETE_CUSTOMER import Ui_Form

class delete_customer(QWidget):
    def __init__(self):
        super(delete_customer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton.clicked.connect(self.confirm)
        self.ui.pushButton_2.clicked.connect(self.delete)

    def confirm(self):
        ID = self.ui.lineEdit.text()
        if len(ID)==0:
            QMessageBox.information(self, '提示', "身份证号不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
            cursor = db.cursor()
            cursor.execute("select user_id,user_name from customer where user_id=%s;" % ID)
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
                self.ui.pushButton_2.setEnabled(False)
            else:
                self.ui.lineEdit_3.setText(str(info[0]))
                self.ui.lineEdit_2.setText(str(info[1]))
                self.ui.pushButton_2.setEnabled(True)
            db.close()

    def delete(self):
        ID = self.ui.lineEdit.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        cursor.execute("select * from Customer_CheckAccount where user_id=%s;"%ID)
        info1=cursor.fetchone()
        cursor.execute("select * from Customer_DepositAccount where user_id=%s;" % ID)
        info2 = cursor.fetchone()
        cursor.execute("select * from Loan_Customer where user_id=%s;" % ID)
        info3 = cursor.fetchone()
        if str(info1)!="None" or str(info2)!="None":
            QMessageBox.information(self, '提示', "存在关联账户，无法删除！", QMessageBox.Close, QMessageBox.Close)
        elif str(info3)!="None":
            QMessageBox.information(self, '提示', "存在贷款，无法删除！", QMessageBox.Close, QMessageBox.Close)
        else:
            try:
                cursor.execute("delete from customer where user_id=%s;" % ID)
                db.commit()
                QMessageBox.information(self, '提示', "成功删除！", QMessageBox.Close, QMessageBox.Close)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.lineEdit_3.setText(None)
                self.ui.lineEdit_2.setText(None)
            except Exception as e:
                inf = '失败：' + e.args[1] + '!'
                db.rollback()
                QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
                self.ui.pushButton_2.setEnabled(False)
                self.ui.lineEdit_3.setText(None)
                self.ui.lineEdit_2.setText(None)
        db.close()








