import pymysql
from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import QDate, Qt

from PAY import Ui_Form

class pay_money(QWidget):
    def __init__(self):
        super(pay_money, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.dateEdit.setDate(QDate.currentDate())
        self.ui.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.ui.pushButton.clicked.connect(self.pm)

    def pm(self):
        ID = self.ui.lineEdit.text()
        Money = self.ui.lineEdit_2.text()
        date = self.ui.dateEdit.date().toString(Qt.ISODate)
        if len(ID)==0 or len(Money)==0:
            QMessageBox.information(self, '提示', "相关信息不能为空！", QMessageBox.Close, QMessageBox.Close)
        else:
            db = pymysql.connect(host='127.0.0.1', user='root', password='qweasdzxc12', database='bank',
                                 charset="utf8")
            cursor = db.cursor()
            cursor.execute("select * from loan where loan_id=%s;"%ID)
            info1=cursor.fetchone()
            cursor.execute("select SUM(Pay_Money) from pay where loan_id=%s;" % ID)
            info2 = cursor.fetchone()
            cursor.execute("select Loan_Money from loan where loan_id=%s;" % ID)
            info3 = cursor.fetchone()
            if str(info2[0])=="None":
                s=0
            else:
                s=float(info2[0])
            if str(info1)=="None":
                QMessageBox.information(self, '提示', "不存在此贷款！", QMessageBox.Close, QMessageBox.Close)
            elif float(info3[0])-s-float(Money)<0:
                QMessageBox.information(self, '提示', "发放超额！", QMessageBox.Close, QMessageBox.Close)
            else:
                sql1="insert into Pay value(%s,%s,%s);"
                try:
                    cursor.execute(sql1,(ID,date,Money))
                    db.commit()
                    QMessageBox.information(self, '提示', '支付成功!', QMessageBox.Close, QMessageBox.Close)
                except Exception as e:
                    inf = '失败：' + e.args[1] + '!'
                    db.rollback()
                    QMessageBox.information(self, '提示', inf, QMessageBox.Close, QMessageBox.Close)
            db.close()
