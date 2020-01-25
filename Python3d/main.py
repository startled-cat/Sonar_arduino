import time
import statistics
import math
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import serial
import csv
import os

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets

from Punkt import Punkt
from Pomiar import Pomiar


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('Python3d\h.ui', self)

        # Const
        self.MAX_STEPS = 4076
        self.MAX_DEG = 360

        # Progress bar completition
        self.completed = 0

        self.pomiar = None

        self.setUi()
        self.disable_all()
        self.setup_later()

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
        self.statusBar = self.findChild(QtWidgets.QStatusBar, 'Ready')
        self.openFile = self.findChild(QtWidgets.QAction, 'actionOpen_File')
        self.saveFile = self.findChild(QtWidgets.QAction, 'actionSave')

        # Progress bar
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(self.completed)

    def setup_later(self):
        self.connectButton.clicked.connect(lambda: self.connect())
        self.startButton.clicked.connect(lambda: self.start_mes())
        self.typeBox.currentIndexChanged.connect(lambda: self.dimension_choice())
        self.exitButton.clicked.connect(lambda: self.exit())
        self.openFile.triggered.connect(lambda: self.openFilePomiar())
        self.saveFile.triggered.connect(lambda: self.saveFilePomiar())

    def disable_all(self):
        self.startButton.setEnabled(False)
        self.typeBox.setEnabled(False)
        self.numberBox.setEnabled(False)
        self.horizontalBox.setEnabled(False)
        self.verticalBox.setEnabled(False)
        self.title.setEnabled(False)
        self.saveFile.setEnabled(False)

    def enable_all(self):
        self.connectButton.setEnabled(True)
        self.startButton.setEnabled(True)
        self.exitButton.setEnabled(True)
        self.typeBox.setEnabled(True)
        self.numberBox.setEnabled(True)
        self.horizontalBox.setEnabled(True)
        self.verticalBox.setEnabled(True)
        self.title.setEnabled(True)

    def connect(self):
        print("Connect...")
        self.disable_all()
        self.connectButton.setText("Connecting...")

        try:
            print("establishing serial connection ... ")

            self.ser = serial.Serial(
                port='COM3',
                baudrate=9600,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                bytesize=serial.EIGHTBITS,
                timeout=0
            )

            print("serial object created")
            time.sleep(3)

            self.statusBar.setText("connected to : " + self.ser.portstr)

        except Exception as e:
            print("error while establishing serial connection : " + str(e))
            self.connectButton.setEnabled(True)
            self.showdialog(
                "Error", "error while establishing serial connection : " + str(e))

        print("connection established!")
        self.connectButton.setText("Reconnect")
        self.connectButton.setEnabled(True)
        self.exitButton.setEnabled(True)
        self.typeBox.setEnabled(True)

    def dimension_choice(self):
        if self.typeBox.currentText() == "2D":
            self.startButton.setEnabled(True)
            self.horizontalBox.setEnabled(True)
            self.verticalBox.setEnabled(False)
            self.title.setEnabled(True)
            self.numberBox.setEnabled(True)
        else:
            self.startButton.setEnabled(True)
            self.horizontalBox.setEnabled(True)
            self.verticalBox.setEnabled(True)
            self.title.setEnabled(True)
            self.numberBox.setEnabled(True)

    def openFilePomiar(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', ".", "(*.obj)")[0]
        if filename != "":
            print(filename)
            self.pomiar = Pomiar.load_pickle(filename)
            self.create_graph()
            self.typeBox.setEnabled(True)
            self.dimension_choice()

    def saveFilePomiar(self):
        self.pomiar.save_with_title("")

    def start_mes(self):
        self.disable_all()

        # reprezentuje krok w stopniach vertical
        ver_deg = int(self.verticalBox.currentText())
        # reprezentuje krok w stopniach horizontal
        hor_deg = int(self.horizontalBox.currentText())
        # reprezentuje ilosc pomiarow na jeden krok
        num_mes_per_deg = int(self.numberBox.currentText())

        # Single vertical and horizontal step calculation
        ver_step = int((ver_deg * self.MAX_STEPS) / self.MAX_DEG)
        hor_step = int((hor_deg * self.MAX_STEPS) / self.MAX_DEG)

        # Send data to arduino
        self.ser.write(bytes(num_mes_per_deg))
        self.ser.write(ver_step)
        self.ser.write(hor_step)

        # Calculate number of steps
        num_steps = int(((self.MAX_STEPS / 2) / hor_step) +
                        ((self.MAX_STEPS) / 4) / ver_step)

        count = 0
        seq = []
        self.pomiar = Pomiar(self.title.text(), num_steps)

        # Read data
        while True:
            for c in self.ser.read():
                if chr(c) == '\n':
                    point = Punkt(seq[0], seq[1] / 180, seq[2] / 180)
                    self.pomiar.add_point(point)

                    if count == self.pomiar.mes_num:
                        self.dimension_choice()
                        print("measurement done!")
                        self.ser.close()
                        print("connection closed")
                        return self.pomiar

                    seq = []
                    count += 1
                    break

                self.completed += int((num_steps * 3) / 100)
                self.progressBar.setValue(self.completed)
                seq.append(chr(c))

        self.pomiar.calculate_all()
        self.create_graph()
        self.saveFile.setEnabled(True)

    def create_graph(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.scatter3D(self.pomiar.x_list, self.pomiar.y_list, self.pomiar.z_list, c='r', cmap='OrRd_r')
        # Data for three-dimensional scattered points
        self.MplWidget.canvas.axes.set_xlabel('x axis')
        self.MplWidget.canvas.axes.set_ylabel('y axis')
        self.MplWidget.canvas.axes.set_zlabel('z axis')
        self.MplWidget.canvas.set_window_title(self.pomiar.mes_title)
        self.MplWidget.canvas.draw()

    def exit(self):
        print("exiting...")
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


if __name__ == "__main__":
    main()
