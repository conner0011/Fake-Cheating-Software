from theming.styles import globalStyles
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os
from theming.styles import globalStyles


def no_abort(a, b, c):
    sys.__excepthook__(a, b, c)


sys.excepthook = no_abort


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.show()

    def Inject(self):
        # stop showing the window
        self.hide()
        # run the application in the background
        os.system("start /B python inject.py")

    def setupUi(self, MainWindow):
        MainWindow.setFixedSize(1109, 600)
        # background color for main UI
        MainWindow.setStyleSheet("background-color: {};".format(globalStyles["backgroundDark"]))
        MainWindow.setWindowTitle("Battle-Bit Titanium Software")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 1109, 50))
        self.label.setStyleSheet("font-size: 30px; color: {};".format(globalStyles["underLine"]))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setText("Battle-Bit Titanium Software")
        self.tabWidget = QtWidgets.QTabWidget(MainWindow)
        self.tabWidget.setGeometry(QtCore.QRect(0, 50, 1109, 551))
        self.tabWidget.setStyleSheet("background-color: {};".format(globalStyles["backgroundLight"]))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setMovable(True)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.pushButton = QtWidgets.QPushButton(MainWindow)
        self.pushButton.setGeometry(QtCore.QRect(500, 300, 100, 50))
        self.pushButton.setStyleSheet("background-color: {};".format(globalStyles["underLine"]))
        self.pushButton.setText("Inject")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Inject)
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(500, 200, 100, 50))
        self.label_2.setStyleSheet("font-size: 15px; color: {};".format(globalStyles["underLine"]))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setText("Undetected 🟢")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(500, 235, 100, 50))
        self.label_3.setStyleSheet("font-size: 8px; color: {};".format(globalStyles["gray"]))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setText("Last checked: " + QtCore.QDate.currentDate().toString("dd/MM/yyyy"))
        self.label_2.setAutoFillBackground(False)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setWordWrap(True)
        self.label_2.setStyleSheet("background-color: {};".format(globalStyles["backgroundLight"]))
        self.label_3.setStyleSheet("background-color: {};".format(globalStyles["backgroundLight"]))
        self.label_2.setStyleSheet("color: {};".format(globalStyles["underLine"]))
        self.label_3.setStyleSheet("color: {};".format(globalStyles["gray"]))
        









if __name__ == "__main__":
    ui_app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    os._exit(ui_app.exec_())
