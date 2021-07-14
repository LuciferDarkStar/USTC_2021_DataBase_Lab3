import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox
from ADD_CUSTOMER import Ui_Form


class add_customer(QWidget):
    def __init__(self):
        super(add_customer, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ACC)



    def ACC(self):
        ID = self.ui.lineEdit.text()
        name = str(self.ui.lineEdit_2.text())
        phone = self.ui.lineEdit_3.text()
        if len(ID)==0 or len(name)==0 or len(phone)==0:
            QMessageBox.information(self, '提示', '必填信息不能为空!', QMessageBox.Close, QMessageBox.Close)
        else:
            addr = self.ui.lineEdit_4.text()
            if len(addr) == 0:
                addr = None
            c_name = self.ui.lineEdit_5.text()
            if len(c_name) == 0:
                c_name = None
            c_phone = self.ui.lineEdit_6.text()
            if len(c_phone) == 0:
                c_phone = None
            c_mail = self.ui.lineEdit_7.text()
            if len(c_mail) == 0:
                c_mail = None
            c_relation = self.ui.lineEdit_8.text()
            if len(c_relation) == 0:
                c_relation = None

            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
            cursor = db.cursor()
            sql = "insert into customer value(%s,%s,%s,%s,%s,%s,%s,%s);"
            try:
                cursor.execute(sql, (ID, name, phone, addr, c_name, c_phone, c_mail, c_relation))
                db.commit()
                QMessageBox.information(self, '提示', '增加新客户成功!', QMessageBox.Close, QMessageBox.Close)
            except Exception as e:
                inf = '失败：' + e.args[1] + '!'
                db.rollback()
                QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            finally:
                db.close()


