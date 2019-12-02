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

import cv2 as cv



class Ui_MainWindow(QMainWindow):
    plot_title_raw = "Raw data "
    plot_title_morph = "After morphology "
    
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(688, 431)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 651, 371))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.openButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setObjectName("openButton")
        self.gridLayout.addWidget(self.openButton, 2, 0, 1, 1)
        self.startButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.startButton.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
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
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio1.sizePolicy().hasHeightForWidth())
        self.radio1.setSizePolicy(sizePolicy)
        self.radio1.setObjectName("radio1")
        self.horizontalLayout_2.addWidget(self.radio1)
        self.radio3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio3.sizePolicy().hasHeightForWidth())
        self.radio3.setSizePolicy(sizePolicy)
        self.radio3.setChecked(True)
        self.radio3.setObjectName("radio3")
        self.horizontalLayout_2.addWidget(self.radio3)
        self.radio2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radio2.sizePolicy().hasHeightForWidth())
        self.radio2.setSizePolicy(sizePolicy)
        self.radio2.setObjectName("radio2")
        self.horizontalLayout_2.addWidget(self.radio2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.connectLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.connectLabel.setObjectName("connectLabel")
        self.gridLayout.addWidget(self.connectLabel, 0, 1, 1, 1)
        self.connectButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectButton.sizePolicy().hasHeightForWidth())
        self.connectButton.setSizePolicy(sizePolicy)
        self.connectButton.setBaseSize(QtCore.QSize(0, 0))
        self.connectButton.setObjectName("connectButton")
        self.gridLayout.addWidget(self.connectButton, 0, 0, 1, 1)
        self.openLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.openLabel.setText("")
        self.openLabel.setObjectName("openLabel")
        self.gridLayout.addWidget(self.openLabel, 2, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 20, 421, 81))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.saveButtonM = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButtonM.sizePolicy().hasHeightForWidth())
        self.saveButtonM.setSizePolicy(sizePolicy)
        self.saveButtonM.setObjectName("saveButtonM")
        self.horizontalLayout_6.addWidget(self.saveButtonM)
        self.displayGraphButtonM = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayGraphButtonM.sizePolicy().hasHeightForWidth())
        self.displayGraphButtonM.setSizePolicy(sizePolicy)
        self.displayGraphButtonM.setObjectName("displayGraphButtonM")
        self.horizontalLayout_6.addWidget(self.displayGraphButtonM)
        self.saveGraphButtonM = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveGraphButtonM.sizePolicy().hasHeightForWidth())
        self.saveGraphButtonM.setSizePolicy(sizePolicy)
        self.saveGraphButtonM.setObjectName("saveGraphButtonM")
        self.horizontalLayout_6.addWidget(self.saveGraphButtonM)
        self.displayImageButtonM = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayImageButtonM.sizePolicy().hasHeightForWidth())
        self.displayImageButtonM.setSizePolicy(sizePolicy)
        self.displayImageButtonM.setObjectName("displayImageButtonM")
        self.horizontalLayout_6.addWidget(self.displayImageButtonM)
        self.saveImageButtonM = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveImageButtonM.sizePolicy().hasHeightForWidth())
        self.saveImageButtonM.setSizePolicy(sizePolicy)
        self.saveImageButtonM.setObjectName("saveImageButtonM")
        self.horizontalLayout_6.addWidget(self.saveImageButtonM)
        self.gridLayout.addWidget(self.groupBox_2, 4, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 20, 421, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.saveButton.setEnabled(False)
        self.saveButtonM.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout_4.addWidget(self.saveButton)
        self.displayGraphButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayGraphButton.sizePolicy().hasHeightForWidth())
        self.displayGraphButton.setSizePolicy(sizePolicy)
        self.displayGraphButton.setObjectName("displayGraphButton")
        self.horizontalLayout_4.addWidget(self.displayGraphButton)
        self.saveGraphButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveGraphButton.sizePolicy().hasHeightForWidth())
        self.saveGraphButton.setSizePolicy(sizePolicy)
        self.saveGraphButton.setObjectName("saveGraphButton")
        self.horizontalLayout_4.addWidget(self.saveGraphButton)
        self.displayImageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.displayImageButton.sizePolicy().hasHeightForWidth())
        self.displayImageButton.setSizePolicy(sizePolicy)
        self.displayImageButton.setObjectName("displayImageButton")
        self.horizontalLayout_4.addWidget(self.displayImageButton)
        self.saveImageButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveImageButton.sizePolicy().hasHeightForWidth())
        self.saveImageButton.setSizePolicy(sizePolicy)
        self.saveImageButton.setObjectName("saveImageButton")
        self.horizontalLayout_4.addWidget(self.saveImageButton)
        self.gridLayout.addWidget(self.groupBox, 3, 1, 1, 1)
        self.exitButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setObjectName("exitButton")
        self.gridLayout.addWidget(self.exitButton, 5, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.formLayout.setObjectName("formLayout")
        self.spinBox = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(150)
        self.spinBox.setProperty("value", 10)
        self.spinBox.setObjectName("spinBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 688, 21))
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
        self.dataM = {}
        
        self.openButton.clicked.connect(lambda: self.openFile())

        self.saveButton.clicked.connect(lambda: self.saveFile(self.data))
        self.saveButtonM.clicked.connect(lambda: self.saveFileM())

        self.exitButton.clicked.connect(lambda: self.exit())

        self.displayGraphButton.clicked.connect(lambda: self.displayGraph(self.data))
        self.saveGraphButton.clicked.connect(lambda: self.saveGraph(self.data))
        self.displayImageButton.clicked.connect(lambda: self.displayImage(self.data))
        self.saveImageButton.clicked.connect(lambda: self.saveImage(self.data))

        self.displayGraphButtonM.clicked.connect(lambda: self.displayGraphM())
        self.saveGraphButtonM.clicked.connect(lambda: self.saveGraphM())
        self.displayImageButtonM.clicked.connect(lambda: self.displayImageM())
        self.saveImageButtonM.clicked.connect(lambda: self.saveImageM())

        self.connectButton.clicked.connect(lambda: self.connect())
        self.startButton.clicked.connect(lambda: self.start())

        self.setAnalyzeButtons(False)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sonar"))
        self.openButton.setText(_translate("MainWindow", "Open csv file"))
        self.startButton.setText(_translate("MainWindow", "Start meauserement"))
        self.label.setText(_translate("MainWindow", "Number of measurements at every position:"))
        self.radio1.setText(_translate("MainWindow", "1"))
        self.radio3.setText(_translate("MainWindow", "2"))
        self.radio2.setText(_translate("MainWindow", "3"))
        self.connectLabel.setText(_translate("MainWindow", "Ready..."))
        self.connectButton.setText(_translate("MainWindow", "Connect to Arduino"))
        self.groupBox_2.setTitle(_translate("MainWindow", "After morphology"))

        self.saveButtonM.setText(_translate("MainWindow", "Save as csv file"))

        self.displayGraphButtonM.setText(_translate("MainWindow", "Display graph"))
        self.saveGraphButtonM.setText(_translate("MainWindow", "Save graph"))
        self.displayImageButtonM.setText(_translate("MainWindow", "Display img"))
        self.saveImageButtonM.setText(_translate("MainWindow", "Save image"))
        self.groupBox.setTitle(_translate("MainWindow", "Raw data"))
        self.saveButton.setText(_translate("MainWindow", "Save as csv file"))
        self.displayGraphButton.setText(_translate("MainWindow", "Display graph"))
        self.saveGraphButton.setText(_translate("MainWindow", "Save graph"))
        self.displayImageButton.setText(_translate("MainWindow", "Display img"))
        self.saveImageButton.setText(_translate("MainWindow", "Save image"))
        self.exitButton.setText(_translate("MainWindow", "Exit"))
        self.label_2.setText(_translate("MainWindow", "Size of structuring element"))

    def setAnalyzeButtons(self, state):
        
        self.saveButton.setEnabled(state)
        self.displayGraphButton.setEnabled(state)
        self.saveGraphButton.setEnabled(state)
        self.displayImageButton.setEnabled(state)
        self.saveImageButton.setEnabled(state)

        self.saveButtonM.setEnabled(state)
        self.displayGraphButtonM.setEnabled(state)
        self.saveGraphButtonM.setEnabled(state)
        self.displayImageButtonM.setEnabled(state)
        self.saveImageButtonM.setEnabled(state)

    def exit(self):
        print("exiting...")
        self.MainWindow.close()
        
    def displayGraph(self, data):
        print("displayGraph")
        self.old_create_graph(data, True, self.plot_title_raw)
        
    def saveGraph(self, data):
        print("saveGraph")
        self.old_create_graph(data, False, self.plot_title_raw)
        
    def displayImage(self, data):
        print("displayImage")
        self.create_image(data, True, self.plot_title_raw)
        
    def saveImage(self, data):
        print("saveImage")
        self.create_image(data, False, self.plot_title_raw)
    
    def displayGraphM(self):
        self.updateMorph()
        self.old_create_graph(self.dataM, True, self.plot_title_morph + "[size=" + str(self.spinBox.value()) + "]")

    def saveGraphM(self):
        self.updateMorph()
        self.old_create_graph(self.dataM, False, self.plot_title_morph + "[size=" + str(self.spinBox.value()) + "]")

    def displayImageM(self):
        self.updateMorph()
        self.create_image(self.dataM, True, self.plot_title_morph + "[size=" + str(self.spinBox.value()) + "]")
        
    def saveImageM(self):
        self.updateMorph()
        self.create_image(self.dataM, False, self.plot_title_morph + "[size=" + str(self.spinBox.value()) + "]")

    def saveFileM(self):
        self.updateMorph()
        self.saveFile(self.dataM)

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

        time.sleep(1)
        while True:
            for c in self.ser.read():
                if chr(c) == '\n':
                    data = joined_seq.split(",")
                    try:

                        if data.__len__() < 2 :
                            break
                        angle = int(data[0])
                        distance = []
                        i = 0
                        while i < measurements:
                            distance.append(int(data[i+1]) / 58.2)
                            i += 1
                        print("angle: " + str(angle) + "; " + str(distance))
                        
                        self.data[int(angle)] = float(statistics.median(distance))

                        if angle == 180:
                            #print("creating graph ... ")
                            #self.data = m

                            #self.saveFile()

                            
                            self.setAnalyzeButtons(True)
                            print("measurement done!")
                            #self.statusbar.setText("measurements collected!")
                            self.startButton.setEnabled(True)
                            self.ser.close()
                            print("connection closed")
                            return
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



    def morph(self, struct_size):
        w, h = 180, 400
        img = [[0 for x in range(w)] for y in range(h)] 
        img = np.zeros((h, w))

        i = 0
        while i < w :
            value = int(self.data.get(i))
            if value >= h : value = h-1
            #print("set: " +str(i) + ", " + str(value) + " to 1" )
            img[:value, i] = 1
            i = i+1

        img = np.flip(img, 0)
        
        #img = cv.imread('image.bmp', 0)
        #img = img/255
        kernel = np.ones((struct_size, struct_size),np.uint8)
        opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
        closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

        y, x = closing.shape
        
        #print(y,x, img[0,1])
        
        j=0
        data={}
        while j<x:
            i=0
            while closing[i,j]==0 :
                i+=1
            #print(y-i)
            data[j]=float(y-i)
            j+=1

        self.dataM = data

    def updateMorph(self):
        struct_size = self.spinBox.value()
        print("Struct_size = " + str(struct_size))
        #todo: check if update necessary
        self.morph(struct_size)
        

    def connect(self):
        print("connect...")
        self.connectButton.setEnabled(False)
        self.connectButton.setText("Connecting...")

        try:
            print("establishing serial connection ... ")
            self.ser = serial.Serial(
            port='COM3',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
                timeout=0)
            print("serial object created")
            time.sleep(3)
            self.connectLabel.setText("connected to : " + self.ser.portstr)
            self.connectButton.setText("Reconnect")
        except Exception as e: 
            print("error while establishing serial connection : " + str(e))
            self.connectButton.setEnabled(True)
            self.showdialog("Error", "error while establishing serial connection : " + str(e))


        print("connection established!")
        self.connectButton.setText("Reconnect")
        self.connectButton.setEnabled(True)
        self.startButton.setEnabled(True)

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
    
    def saveFile(self, data):
        print("(NOT DONE)saving file ...")
        try:
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
            if filename == "" : return
            with open(filename, 'w', newline='') as file:
                angle = 0
                file = csv.writer(file, delimiter=',')
                i = 0
                while i < len(data):
                    file.writerow([str(i), str(data.get(i))])
                    i += 1

                # for element in self.data:
                #     file.writerow([str(angle), str(element)])
                #     angle += 1
        except Exception as e:
            self.showdialog("Error", "failed to save file :(\n" + str(e))


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
    
    def old_create_graph(self, data, display, title):
        #print(data)
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
        #print(self.data)
        while i < len(data) :
            #print("i = " + str(i) + " value = " + str(data.get(i)))
            y.append(math.sin(math.radians(i)) * (data.get(i)))
            x.append(math.cos(math.radians(i)) * (data.get(i)))
            i += 1
        li.set_ydata(y)
        li.set_xdata(x)
        if display:
            plt.title(title)
            plt.show()
        else:
            filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
            plt.savefig(filename)

    def create_image(self, data, display, title):
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
            plt.title(title)
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
