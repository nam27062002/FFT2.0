from PyQt5 import QtGui, QtWidgets, QtCore
import sys, os,UIStart,ShowSignal,Training,ShowEigenvectors,UIStatistical
class UI:
    def __init__(self):
        self.ui = ""
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.URL = ""
        self.train = Training.Training()
    def __UIStart(self):
        self.ui = UIStart.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.ui.frame.setAcceptDrops(True)
        self.ui.frame.dragEnterEvent = self.DragEnter
        self.ui.frame.drop = self.DragEnter
        self.ui.frame.dropEvent = self.dropEvent
        self.ui.frame.mousePressEvent = self.openFolder
        self.ui.pushButton.clicked.connect(self.showVector)
        self.ui.pushButton_2.clicked.connect(self.__UIStatistical)
    def __UIStatistical(self):
        self.ui = UIStatistical.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow,self.train.Percent,self.train.Statistical[self.train.Percent.index(max(self.train.Percent))])
        self.MainWindow.show()
        self.ui.pushButton.clicked.connect(self.__UIStart)
    def showVector(self):
        ShowEigenvectors.Show(self.train.getEigenvectors()).show()
    def openFolder(self,e):
        directory = QtWidgets.QFileDialog.getOpenFileName(filter="Images (*.wav)")
        if directory[0] != "":
            self.showASignal(directory[0])
    def DragEnter(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
        else:
            event.ignore()
    def dropEvent(self, event):
        x = event.mimeData().urls()[0].toLocalFile()
        s = ""
        for i in range(len(x) - 1, -1, -1):
            if x[i] != ".":
                s = x[i] + s
            else:
                break
        if s == "wav":
            event.accept()
            self.showASignal(x)
        else:
            event.ignore()
    def showASignal(self,url):
        ShowSignal.ShowSignal(url,self.train.compare(url=url,N_FFT=1024)[1]).show()
    def loop(self):
        self.__UIStart()
        sys.exit(self.app.exec_())
