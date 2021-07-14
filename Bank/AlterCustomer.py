import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox
from ALTER_CUSTOMER import Ui_Form

class alter_customer(QWidget):
    def __init__(self):
        super(alter_customer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_5.clicked.connect(self.confirm)
        self.ui.pushButton_3.clicked.connect(self.alter)

    def confirm(self):
        ID = self.ui.lineEdit_9.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        if len(ID)>0:
            cursor.execute("select * from customer where user_id=%s;" % ID)
            db.close()
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
                self.ui.lineEdit_10.setText(None)
                self.ui.lineEdit_11.setText(None)
                self.ui.lineEdit_12.setText(None)
                self.ui.lineEdit_13.setText(None)
                self.ui.lineEdit_14.setText(None)
                self.ui.lineEdit_15.setText(None)
                self.ui.lineEdit_16.setText(None)
                self.ui.pushButton_3.setEnabled(False)
            else:
                self.ui.pushButton_3.setEnabled(True)
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
        else:
            QMessageBox.information(self, '提示', "身份证不能为空！", QMessageBox.Close, QMessageBox.Close)

    def alter(self):
        ID = self.ui.lineEdit_9.text()
        db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
        cursor = db.cursor()
        name = str(self.ui.lineEdit_10.text())
        phone = self.ui.lineEdit_11.text()
        addr = self.ui.lineEdit_12.text()
        if len(addr) == 0:
            addr = None
        c_mail = self.ui.lineEdit_15.text()
        if len(c_mail) == 0:
            c_mail = None
        c_relation = self.ui.lineEdit_16.text()
        if len(c_relation) == 0:
            c_relation = None
        c_name = self.ui.lineEdit_13.text()
        if len(c_name) == 0:
            c_name=None
        c_phone = self.ui.lineEdit_14.text()
        if len(c_phone) == 0:
            c_phone=None
        if len(name) == 0 or len(phone) == 0:
            QMessageBox.information(self, '提示', "姓名或电话不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            sql = "update customer set user_name=%s,user_phone=%s,user_address=%s,User_Contact_Name=%s,User_Contact_Phone=%s,User_Contact_Email=%s,User_Contact_Relation=%s where user_id=%s;"
            try:
                cursor.execute(sql, (name, phone, addr, c_name, c_phone, c_mail, c_relation, ID))
                db.commit()
                QMessageBox.information(self, '提示', '修改客户信息成功!', QMessageBox.Close, QMessageBox.Close)
            except Exception as e:
                inf = '失败：' + e.args[1] + '!'
                db.rollback()
                QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            finally:
                db.close()
