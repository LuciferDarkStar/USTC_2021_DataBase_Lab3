import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt

from CREATE_LOAN import Ui_Form

class create_loan(QWidget):
    def __init__(self):
        super(create_loan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Create2)

    def Create2(self):
        ID= self.ui.lineEdit.text()
        bank = self.ui.comboBox.currentText()
        money=self.ui.lineEdit_2.text()
        user_id=self.ui.lineEdit_3.text()
        if len(ID)==0 or len(bank)==0 or len(money)==0 or len(user_id)==0:
            QMessageBox.information(self, '提示', "相关信息不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            cursor.execute("select * from Customer where user_id=%s;" % user_id)
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此客户！", QMessageBox.Close, QMessageBox.Close)
            else:
                if len(ID) == 0 or len(bank) == 0 or len(money) == 0 or float(money) < 0:
                    QMessageBox.information(self, '提示', "相关信息不能为空或为负值！", QMessageBox.Close, QMessageBox.Close)
                else:
                    sql1 = "insert into loan value(%s,%s,%s);"
                    sql2 = "insert into Loan_Customer value(%s,%s);"
                    try:
                        cursor.execute(sql1, (ID, bank, money))
                        cursor.execute(sql2, (ID, user_id))
                        db.commit()
                        QMessageBox.information(self, '提示', '新增贷款成功!', QMessageBox.Close, QMessageBox.Close)
                    except Exception as e:
                        inf = '失败：' + e.args[1] + '!'
                        db.rollback()
                        QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            db.close()

