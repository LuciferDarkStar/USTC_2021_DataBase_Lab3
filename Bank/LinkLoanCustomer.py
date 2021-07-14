import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt

from LINK_LOAN_CUSTOMER import Ui_Form

class link_loan(QWidget):
    def __init__(self):
        super(link_loan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.link2)

    def link2(self):
        ID = self.ui.lineEdit.text()
        user_id = self.ui.lineEdit_3.text()
        if len(ID)==0 or len(user_id)==0:
            QMessageBox.information(self, '提示', '相关信息不能为空!', QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            cursor.execute("select * from loan where loan_id=%s;" % ID)
            info = cursor.fetchone()
            cursor.execute("select * from Customer where user_id=%s;" % user_id)
            info1 = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此贷款！", QMessageBox.Close, QMessageBox.Close)
            elif str(info1) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
            else:
                sql1 = "insert into Loan_Customer value(%s,%s);"
                try:
                    cursor.execute(sql1, (ID, user_id))
                    db.commit()
                    QMessageBox.information(self, '提示', '关联成功!', QMessageBox.Close, QMessageBox.Close)
                except Exception as e:
                    inf = '失败：' + e.args[1] + '!'
                    db.rollback()
                    QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            db.close()