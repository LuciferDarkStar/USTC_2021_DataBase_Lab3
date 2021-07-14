import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWin import Ui_MainWindow
from PyQt5.QtGui import QIcon
from AddCustomer import add_customer
from DeleteCustomer import delete_customer
from AlterCustomer import alter_customer
from FindCustomer import find_customer
from CreateAccount import create_account
from DeleteAccount import delete_account
from LinkAccount import link_account
from AlterAccount import alter_account
from FindAccount import find_account
from CreateLoan import create_loan
from LinkLoanCustomer import link_loan
from PayMoney import pay_money
from FindLoan import find_loan
from DeleteLoan import delete_loan
from DepositSum import d_sum
from LoanSum import loan_sum


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 主窗口需要有一个UI界面，我们使用TablePage作为主窗口显示的UI界面
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.initBinding()

    def initBinding(self):
        # 将主界面按钮点击动作绑定到函数
        self.ui.pushButton.clicked.connect(self.mainAddCustomer)
        self.ui.pushButton_2.clicked.connect(self.mainDeleteCustomer)
        self.ui.pushButton_3.clicked.connect(self.mainAlterCustomer)
        self.ui.pushButton_4.clicked.connect(self.mainFindCustomer)
        self.ui.pushButton_5.clicked.connect(self.mainCreateAccount)
        self.ui.pushButton_6.clicked.connect(self.mainDeleteAccount)
        self.ui.pushButton_7.clicked.connect(self.mainAlterAccount)
        self.ui.pushButton_8.clicked.connect(self.mainFindAccount)
        self.ui.pushButton_9.clicked.connect(self.mainCreateLoan)
        self.ui.pushButton_10.clicked.connect(self.mainDeleteLoan)
        self.ui.pushButton_11.clicked.connect(self.mainDespoitSum)
        self.ui.pushButton_12.clicked.connect(self.mainFindLoan)
        self.ui.pushButton_14.clicked.connect(self.mainLoanSum)
        self.ui.pushButton_15.clicked.connect(self.mainLinkAccount)
        self.ui.pushButton_16.clicked.connect(self.mainLinkLoan)
        self.ui.pushButton_17.clicked.connect(self.mainPay)

    def mainAddCustomer(self):
        self.addc = add_customer()
        self.addc.show()

    def mainDeleteCustomer(self):
        self.dele = delete_customer()
        self.dele.show()

    def mainAlterCustomer(self):
        self.alter = alter_customer()
        self.alter.show()

    def mainFindCustomer(self):
        self.find = find_customer()
        self.find.show()

    def mainCreateAccount(self):
        self.ca = create_account()
        self.ca.show()

    def mainDeleteAccount(self):
        self.de = delete_account()
        self.de.show()

    def mainLinkAccount(self):
        self.link = link_account()
        self.link.show()
    def mainAlterAccount(self):
        self.alterA= alter_account()
        self.alterA.show()
    def mainFindAccount(self):
        self.f1 = find_account()
        self.f1.show()
    def mainCreateLoan(self):
        self.loan1 = create_loan()
        self.loan1.show()
    def mainLinkLoan(self):
        self.link2=link_loan()
        self.link2.show()
    def mainPay(self):
        self.pay=pay_money()
        self.pay.show()
    def mainFindLoan(self):
        self.findloan=find_loan()
        self.findloan.show()
    def mainDeleteLoan(self):
        self.deleteloan=delete_loan()
        self.deleteloan.show()
    def mainDespoitSum(self):
        self.ds=d_sum()
        self.ds.show()
    def mainLoanSum(self):
        self.ls=loan_sum()
        self.ls.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("#MainWindow{border-image:url(./background3.jpg);}")
    w.setWindowIcon(QIcon("./ustc.jpg"))  # 设置窗口图标
    w.setWindowTitle("银行管理系统")  # 设置窗口名
    w.resize(1050, 850)
    sys.exit(app.exec_())
