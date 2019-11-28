from PIL import Image
import PIL
import serial
import time
import statistics
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

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
        MainWindow.setObjectName("Sonar")
        MainWindow.resize(480, 342)

        self.MainWindow = MainWindow

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 460, 284))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.displayGraphButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        

        self.displayGraphButton.setObjectName("displayGraphButton")
        self.horizontalLayout.addWidget(self.displayGraphButton)
        self.saveGraphButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        

        self.saveGraphButton.setObjectName("saveGraphButton")
        self.horizontalLayout.addWidget(self.saveGraphButton)
        self.displayImageButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.displayImageButton.setObjectName("displayImageButton")
        
        
        self.horizontalLayout.addWidget(self.displayImageButton)
        self.saveImageButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveImageButton.setObjectName("saveImageButton")
        

        self.horizontalLayout.addWidget(self.saveImageButton)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.saveButton.setEnabled(False)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 0, 1, 1)
        self.openButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 2, 0, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 7, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setBaseSize(QtCore.QSize(0, 0))
        self.startButton.setCheckable(False)
        self.startButton.setChecked(False)
        self.startButton.setObjectName("startButton")
        self.gridLayout.addWidget(self.startButton, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radio1 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio1.setObjectName("radio1")
        self.horizontalLayout_2.addWidget(self.radio1)
        self.radio3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio3.setChecked(True)
        self.radio3.setObjectName("radio3")
        self.horizontalLayout_2.addWidget(self.radio3)
        self.radio2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radio2.setObjectName("radio2")
        self.horizontalLayout_2.addWidget(self.radio2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
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
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.connectLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.connectLabel.setObjectName("connectLabel")
        self.gridLayout.addWidget(self.connectLabel, 0, 2, 1, 1)
        self.openLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openLabel.setText("")
        self.openLabel.setObjectName("openLabel")
        self.gridLayout.addWidget(self.openLabel, 2, 2, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
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

        self.displayGraphButton.clicked.connect(lambda: self.displayGraph())
        self.saveGraphButton.clicked.connect(lambda: self.saveGraph())
        self.displayImageButton.clicked.connect(lambda: self.displayImage())
        self.saveImageButton.clicked.connect(lambda: self.saveImage())

        self.connectButton.clicked.connect(lambda: self.connect())
        self.startButton.clicked.connect(lambda: self.start())

        self.setAnalyzeButtons(False)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sonar"))
        self.displayGraphButton.setText(_translate("MainWindow", "Display graph"))
        self.saveGraphButton.setText(_translate("MainWindow", "Save graph"))
        self.displayImageButton.setText(_translate("MainWindow", "Display img"))
        self.saveImageButton.setText(_translate("MainWindow", "Save image"))
        self.saveButton.setText(_translate("MainWindow", "Save as csv file"))
        self.openButton.setText(_translate("MainWindow", "Open csv file"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.startButton.setText(_translate("MainWindow", "Start meauserement"))
        self.label.setText(_translate("MainWindow", "Number of measurements at every position:"))
        self.radio1.setText(_translate("MainWindow", "1"))
        self.radio3.setText(_translate("MainWindow", "2"))
        self.radio2.setText(_translate("MainWindow", "3"))
        self.connectLabel.setText(_translate("MainWindow", "Ready..."))
        self.connectButton.setText(_translate("MainWindow", "Connect to Arduino"))

    def setAnalyzeButtons(self, state):
        self.displayGraphButton.setEnabled(state)
        self.saveGraphButton.setEnabled(state)
        self.displayImageButton.setEnabled(state)
        self.saveImageButton.setEnabled(state)

    def exit(self):
        print("exiting...")
        self.MainWindow.close()
        
    def displayGraph(self):
        print("displayGraph")
        self.old_create_graph(self.data, True)
        
    def saveGraph(self):
        print("saveGraph")
        self.old_create_graph(self.data, False)
        
    def displayImage(self):
        print("displayImage")
        self.create_image(self.data, True)
        
    def saveImage(self):
        print("saveImage")
        self.create_image(self.data, False)
    
    def start(self):
        print("starting...")
        self.startButton.setEnabled(False)
        seq = []
        count = 1

        if self.radio1.isChecked : measurements = 1
        elif self.radio2.isChecked : measurements = 2
        elif self.radio3.isChecked : measurements = 3

        if measurements == '2':
            ser.write(bytes(measurements, 'utf-8'))
        elif measurements == '3':
            ser.write(bytes(measurements, 'utf-8'))
        else:
            measurements = '1'
            ser.write(bytes(measurements, 'utf-8'))

        measurements = int(measurements)

        m = [180]

        time.sleep(3)
        while True:
            for c in ser.read():
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
                        if angle == 180:
                            print("creating graph ... ")
                            create_graph(m)
                            save(m)
                            print("done!")
                    except ValueError:
                        print(joined_seq)
                    except IndexError:
                        print(joined_seq)

                    seq = []
                    count += 1
                    break
                seq.append(chr(c))  # convert from ANSII
                joined_seq = ''.join(str(v) for v in seq)  # Make a string from arrays


        ser.close()

    def connect(self):
        print("connect...")
        self.connectButton.setEnabled(False)
        self.connectButton.setText("Connecting...")

        try:
            self.ser = serial.Serial(
            port='COM4',\
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
        print("(NOT DONE)saving file ...")
        
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        with open(filename, 'w', newline='') as file:
            angle = 0
            file = csv.writer(file, delimiter=',')
            i = 0
            while i < len(self.data):
                file.writerow([str(i), str(self.data.get(i))])
                i += 1

            # for element in self.data:
            #     file.writerow([str(angle), str(element)])
            #     angle += 1

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
                    #print("reading: " + str(row[0]) + " > " + str(row[1]))
        
        #print(self.data)
        self.saveButton.setEnabled(True)
        self.setAnalyzeButtons(True)
                
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
    
    def old_create_graph(self, data, display):
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
       
        i = 0
        while i <= 180 :
            #print("i = " + str(i) + " value = " + str(data.get(i)))
            y.append(math.sin(math.radians(i)) * (data.get(i)))
            x.append(math.cos(math.radians(i)) * (data.get(i)))
            i += 1
        li.set_ydata(y)
        li.set_xdata(x)
        if display:
            plt.show()
        else:
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
            plt.savefig(filename)

    def create_image(self, data, display):
        w, h = 180, 400
        img = [[0 for x in range(w)] for y in range(h)] 
        img = np.zeros((h, w))

        i = 0
        while i < w :
            value = int(data.get(i))
            if value >= h : value = h-1
            #print("set: " +str(i) + ", " + str(value) + " to 1" )
            img[:value, i] = 1
            i = i+1
        
        if display : 

            fig, ax = plt.subplots()
            ax.set_xlabel("angle [°]")
            ax.set_ylabel("distance [cm]")
            ax.set_ylim([0, 400])
            plt.imshow(img, cmap='gray', vmin=0, vmax=1)
            plt.show()
        else:
            #flip vertically before saving 
            img = np.flip(img, 0)

            #Rescale to 0-255 and convert to uint8
            rescaled = (255.0 / img.max() * (img - img.min())).astype(np.uint8)

            im = Image.fromarray(rescaled)
             # Only open dialog if there is no filename yet
            # PYQT5 Returns a tuple in PyQt5, we only need the filename
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]

            im.save(filename)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
