# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(450, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 421, 284))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.openButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 2, 0, 1, 1)

        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 0, 1, 1)

        self.exitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 6, 0, 1, 1)

        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setEnabled(False)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 1, 0, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.radio1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio1.setObjectName("radio1")
        self.verticalLayout.addWidget(self.radio1)

        self.radio3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio3.setChecked(True)
        self.radio3.setObjectName("radio3")
        self.verticalLayout.addWidget(self.radio3)

        self.radio2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio2.setObjectName("radio2")
        self.verticalLayout.addWidget(self.radio2)

        self.progressBar = QtWidgets.QProgressBar(self.gridLayoutWidget)
        self.progressBar.setEnabled(False)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(180)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)

        self.analyzeButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.analyzeButton.setEnabled(False)
        self.analyzeButton.setObjectName("analyzeButton")
        self.gridLayout.addWidget(self.analyzeButton, 3, 0, 1, 1)

        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)

        self.openLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openLabel.setObjectName("openLabel")
        self.gridLayout.addWidget(self.openLabel, 2, 1, 1, 1)

        self.connectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 0, 1, 1)

        self.connectLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.connectLabel.setObjectName("connectLabel")
        self.gridLayout.addWidget(self.connectLabel, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openButton.setText(_translate("MainWindow", "Open file"))
        self.saveButton.setText(_translate("MainWindow", "Save file"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.startButton.setText(_translate("MainWindow", "Start meauserement"))
        self.label.setText(_translate("MainWindow", "Number of measurements at every position"))
        self.radio1.setText(_translate("MainWindow", "1"))
        self.radio3.setText(_translate("MainWindow", "2"))
        self.radio2.setText(_translate("MainWindow", "3"))
        self.analyzeButton.setText(_translate("MainWindow", "Analyze"))
        self.label_4.setText(_translate("MainWindow", "[placeholder]"))
        self.openLabel.setText(_translate("MainWindow", "[filename of opened file]"))
        self.connectButton.setText(_translate("MainWindow", "Connect to Arduino"))
        self.connectLabel.setText(_translate("MainWindow", "Ready..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
