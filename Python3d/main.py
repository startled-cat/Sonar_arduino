from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('h.ui', self)
        self.setUi()

        self.show()

    def setUi(self):
        self.connectButton = self.findChild(QtWidgets.QPushButton, 'connectButton')
        self.startButton = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.exitButton = self.findChild(QtWidgets.QPushButton, 'exitButton')
        self.typeBox = self.findChild(QtWidgets.QComboBox, 'typeMeasurement')
        self.numberBox = self.findChild(QtWidgets.QComboBox, 'numberMeasurement')
        self.horizontalBox = self.findChild(QtWidgets.QComboBox, 'hStep')
        self.verticalBox = self.findChild(QtWidgets.QComboBox, 'vStep')
        self.title = self.findChild(QtWidgets.QLineEdit, 'titleEdit')
        self.progressBar = self.findChild(QtWidgets.QProgressBar, 'progressBar')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()



