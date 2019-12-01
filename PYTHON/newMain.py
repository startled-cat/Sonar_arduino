# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import serial
import time
import statistics
import math
import matplotlib.pyplot as plt
import csv
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets




class Ui_MainWindow(QMainWindow):
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
        #self.startButton.setEnabled(False)
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
        self.setupLater()

    def setupLater(self):
        print("setupLater ... ")
        self.filename = ''
        self.data = {}
        
        self.openButton.clicked.connect(lambda: self.openFile())
        self.saveButton.clicked.connect(lambda: self.saveFile())
        self.exitButton.clicked.connect(lambda: self.exit())
        self.analyzeButton.clicked.connect(lambda: self.analyze())
        self.connectButton.clicked.connect(lambda: self.connect())
        self.startButton.clicked.connect(lambda: self.start())
        
        

        

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


    def exit(self):
        print("exiting...")

    def analyze(self):
        print("analyze...")
        self.old_create_graph(self.data)

    def start(self):
        print("starting...")
        self.startButton.setEnabled(False)
        seq = []
        count = 1

        if self.radio1.isChecked : measurements = 1
        elif self.radio2.isChecked : measurements = 2
        elif self.radio3.isChecked : measurements = 3

        if measurements == '2':
            self.ser.write(bytes(measurements, 'utf-8'))
        elif measurements == '3':
            self.ser.write(bytes(measurements, 'utf-8'))
        else:
            measurements = '1'
            self.ser.write(bytes(measurements, 'utf-8'))

        measurements = int(measurements)

        m = [180]
        progres = 0
        time.sleep(3)
        while True:
            for c in self.ser.read():
                if chr(c) == '\n':
                    data = joined_seq.split(",")
                    try:
                        # print(str(data))
                        # print(str(data.__len__()))
                        if data.__len__() < 2 :
                            break
                        angle = int(data[0])
                        distance = []
                        i = 0
                        while i < measurements:
                            distance.append(int(data[i+1]) / 58.2)
                            i += 1
                        print("angle: " + str(angle) + "; " + str(distance))
                        m.insert(angle, statistics.median(distance))
                        progres += 1
                        self.progressBar.setValue = progres
                        if angle == 180:
                            #print("creating graph ... ")
                            #create_graph(m)
                            #save(m)
                            print("done!")
                            self.data = m
                            return m
                    except ValueError:
                        print(joined_seq)
                    except IndexError:
                        print(joined_seq)

                    seq = []
                    count += 1
                    break
                seq.append(chr(c))  # convert from ANSII
                joined_seq = ''.join(str(v) for v in seq)  # Make a string from arrays


        self.ser.close()



    def connect(self):
        print("connect...")
        self.connectButton.setEnabled(False)
        self.connectButton.setText("Connecting...")

        try:
            self.ser = serial.Serial(
            port='COM3',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
                timeout=0)

            time.sleep(3)
            self.connectLabel.setText("connected to : " + self.ser.portstr)
            self.connectButton.setText("Reconnect")
        except:
            self.showdialog("error", "couldnt connect")


        

        self.connectButton.setEnabled(True)

        
    def showdialog(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        #msg.buttonClicked.connect(lambda button: button.text())
        retval = msg.exec_()
        print("value of pressed message box button:", retval)
        return retval
    
    def saveFile(self):
        print("saving file ...")
        # bedzie zapisywal pomiary do pliku csv


        #  # Only open dialog if there is no filename yet
        # # PYQT5 Returns a tuple in PyQt5, we only need the filename
        # if not self.filename:
        #     self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]

        # if self.filename:
        #     # We just store the contents of the text file along with the
        #     # format in html, which Qt does in a very nice way for us
        #     with open(self.filename, "wt") as file:
        #         file.write(self.text.toPlainText())

        #     self.changesSaved = True



    def openFile(self):
        print("opening file...")
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.csv)")[0]

        if self.filename:
            with open(self.filename, "rt") as file:
                self.openLabel.setText("opened: " + self.filename)
                file_reader = csv.reader(file, delimiter=',')
                for row in file_reader:
                    #self.data.append(float(row[1]))
                    self.data[int(row[0])]=float(row[1])
                    print("reading: " + str(row[0]) + " > " + str(row[1]))
        self.analyzeButton.setEnabled(True)
        print(self.data)
                


    
    def old_save(data):
        DIR = os.getcwd() + "\\data"
        names = os.listdir(DIR)

        index = len(names)
        index += 1

        with open(DIR + "\\data" + str(index) + ".csv", 'w', newline='') as file:
            angle = 0
            file = csv.writer(file, delimiter=',')
            for element in data:
                file.writerow([str(angle), str(element)])
                angle += 1


    def old_read(filename):
        DIR = os.getcwd() + os.path.sep
        with open(DIR + filename) as file:
            data = []
            file_reader = csv.reader(file, delimiter=',')
            for row in file_reader:
                data.append(float(row[1]))
                
        return data
    
    def old_create_graph(self, data):
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot()
        # Move left y-axis and bottom x-axis to centre, passing through (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')
        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        y = []
        x = []
        # Initialize with no points, and circle markers, return Line2D object
        li, = ax.plot(x, y, '.')
        # Set default axis in range of -100 to 100
        # plt.axis([-200, 200, -200, 200])
        axes = plt.gca()
        axes.set_xlim([-400, 400])
        axes.set_ylim([0, 400])

        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_position(('data', 0))
        # Interactive plot ON
        # plt.ion()

        # for key, value in self.data_dict.items():
        # print(data)
        # i = 0
        # while i < 180:
        #     print(str(i) + " > " + str(data.get(i)))

        #     #x.append()
        #     i += 1

        
        i = 0
        while i <= 180 :
            print("i = " + str(i) + "value = " + str(data.get(i)))
            y.append(math.sin(math.radians(i)) * (data.get(i)))
            x.append(math.cos(math.radians(i)) * (data.get(i)))
            i += 1

        

        # i = 0
        # while i < 180:
        #     y.append(math.sin(math.radians(i)) * data.get(i))
        #     x.append(math.cos(math.radians(i)) * data.get(i))
        #     # print(y)
        #     # print(x)
        #     # plt.pause(0.1)
        #     i += 1

        li.set_ydata(y)
        li.set_xdata(x)
        plt.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
