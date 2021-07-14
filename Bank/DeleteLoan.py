import pymysql
from PyQt5.QtWidgets import QWidget,QMessageBox
from DELETE_LOAN import Ui_Form

class delete_loan(QWidget):
    def __init__(self):
        super(delete_loan, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.deleteL)

    def deleteL(self):
        ID = self.ui.lineEdit.text()
        if len(ID)==0:
            QMessageBox.information(self, '提示', "贷款ID不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank', charset="utf8")
            cursor = db.cursor()
            cursor.execute("select * from loan where loan_id=%s;" % ID)
            info = cursor.fetchone()
            if str(info) == "None":
                QMessageBox.information(self, '提示', "不存在此贷款！", QMessageBox.Close, QMessageBox.Close)
            else:
                money=float(info[2])
                cursor.execute("select SUM(pay_money) from Pay where loan_id=%s;" % ID)
                info1 = cursor.fetchone()
                if str(info1[0]) == "None":
                    s = 0.0
                else:
                    s = float(info1[0])
                s2=money-s
                if s==0 or s2==0:
                    try:
                        cursor.execute("delete from Loan_Customer where loan_id=%s;"%ID)
                        cursor.execute("delete from pay where loan_id=%s;" % ID)
                        cursor.execute("delete from loan where loan_id=%s;" % ID)
                        db.commit()
                        QMessageBox.information(self, '提示', "成功删除！", QMessageBox.Close, QMessageBox.Close)
                    except Exception as e:
                        inf = '失败：' + e.args[1] + '!'
                        db.rollback()
                        QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
                else:
                    QMessageBox.information(self, '提示', "贷款发放中，不能删除！", QMessageBox.Close, QMessageBox.Close)
            db.close()