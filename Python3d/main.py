import time
import statistics
import math
import importlib
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import serial
import csv
import os
import cv2 as cv

from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication
import sys

from inputDialog import InputDialog
from InputDialog2 import InputDialog2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore, QtWidgets

from Punkt import Punkt
from Pomiar import Pomiar
from approx import approx

from Arduino import Arduino

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
        self.pomiar_morph = None
        self.data = None
        self.x_list = None
        self.y_list = None

        self.setWindowTitle("Bonar")
        self.setWindowIcon(QtGui.QIcon('bonar-icon2.png'))

        self.setUi()
        self.disable_all()
        self.disable_graph_opt()
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
        self.stackWidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.display2dGraph = self.findChild(QtWidgets.QAction, 'action2DGraph')
        self.display3dGraph = self.findChild(QtWidgets.QAction, 'action3DGraph')
        self.display2dGraphMorph = self.findChild(QtWidgets.QAction, 'actionDisplayMorf')
        self.display2dGraphApprox = self.findChild(QtWidgets.QAction, 'actionDisplayAprox')
        self.approxSetParam = self.findChild(QtWidgets.QAction, 'actionSetAprox')
        self.morphSetParam = self.findChild(QtWidgets.QAction, 'actionSet_parametrs')

        # Progress bar
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(self.completed)

    def setup_later(self):
        self.connectButton.clicked.connect(lambda: self.connect())
        self.startButton.clicked.connect(lambda: self.start_mes())
        self.typeBox.currentIndexChanged.connect(lambda: self.dimension_choice())
        self.exitButton.clicked.connect(lambda: self.exit())
        self.openFile.triggered.connect(lambda: self.open_file_pomiar())
        self.saveFile.triggered.connect(lambda: self.save_file_pomiar())

        self.display3dGraph.triggered.connect(lambda: self.swap_stacked_widget(0))
        self.display2dGraph.triggered.connect(lambda: self.swap_stacked_widget(1))
        self.display2dGraphMorph.triggered.connect(lambda: self.swap_stacked_widget(2))
        self.morphSetParam.triggered.connect(lambda: self.set_morph_parameters())
        self.display2dGraphApprox.triggered.connect(lambda: self.swap_stacked_widget(3))
        self.approxSetParam.triggered.connect(lambda: self.set_approx_parameters())

        self.ardiuno = Arduino()

    def disable_all(self):
        self.startButton.setEnabled(False)
        self.typeBox.setEnabled(False)
        self.numberBox.setEnabled(False)
        self.horizontalBox.setEnabled(False)
        self.verticalBox.setEnabled(False)
        self.title.setEnabled(False)
        self.saveFile.setEnabled(False)

    def disable_graph_opt(self):
        self.display2dGraph.setEnabled(False)
        self.display3dGraph.setEnabled(False)
        self.display2dGraphApprox.setEnabled(False)
        self.display2dGraphMorph.setEnabled(False)
        self.approxSetParam.setEnabled(False)  
        self.morphSetParam.setEnabled(False)
        
    def enable_graph_opt(self):
        self.display2dGraph.setEnabled(True)
        self.display3dGraph.setEnabled(True)
        self.approxSetParam.setEnabled(True)
        self.morphSetParam.setEnabled(True)   

    def enable_all(self):
        self.connectButton.setEnabled(True)
        self.startButton.setEnabled(True)
        self.exitButton.setEnabled(True)
        self.typeBox.setEnabled(True)
        self.numberBox.setEnabled(True)
        self.horizontalBox.setEnabled(True)
        self.verticalBox.setEnabled(True)
        self.title.setEnabled(True)

    def set_morph_parameters(self):
        dialog = InputDialog()
        if dialog.exec():
            paramet = dialog.getInputs()
            self.update_morph(paramet[0], paramet[1])

        self.display2dGraphMorph.setEnabled(True)

    def set_approx_parameters(self):
        dialog = InputDialog2()
        if dialog.exec():
            self.approx(dialog.getInputs())

        self.display2dGraphApprox.setEnabled(True)

    def approx(self, inputs):
        print("event handler")
        self.update_morph(inputs[0], inputs[1])
        self.x_list, self.y_list = approx(self.pomiar_morph, inputs[2], self)
        print(self.x_list)
        print(self.y_list)

    def swap_stacked_widget(self, i):
        print(i)
        self.stackWidget.setCurrentIndex(i)
        if i == 1:
            self.create_graph2d()
        elif i == 0:
            self.create_graph()
        elif i == 2:
            self.create_graph2d_morph()
        elif i == 3:
            self.create_graph2d_aprox()

    def connect(self):
        print("Connect...")
        self.disable_all()
        self.connectButton.setText("Connecting...")

        try:
            print("establishing serial connection ... ")

            # self.ser = serial.Serial(
            #     port='COM3',
            #     baudrate=115200,
            #     parity=serial.PARITY_NONE,
            #     stopbits=serial.STOPBITS_ONE,
            #     bytesize=serial.EIGHTBITS,
            #     timeout=0
            # )
            self.ardiuno.connect()

            print("serial object created")
            #time.sleep(3)

            self.statusBar.setText("connected to : " + self.ser.portstr)

        except Exception as e:
            print("error while establishing serial connection : " + str(e))
            self.connectButton.setEnabled(True)
            #self.showdialog(
            #    "Error", "error while establishing serial connection : " + str(e))

        print("connection established!")
        self.connectButton.setText("Reconnect")
        self.connectButton.setEnabled(True)
        self.exitButton.setEnabled(True)
        self.typeBox.setEnabled(True)
        self.dimension_choice()

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

    def open_file_pomiar(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, 'Open File', ".", "(*.obj)")[0]
        if filename != "":
            self.pomiar = Pomiar.load_pickle(filename)
            self.pomiar.calculate_all()
            self.create_graph()
            self.enable_graph_opt()

        self.setWindowTitle("Bonar - " + filename)

    def save_file_pomiar(self):
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
        print("num_mes_per_deg = " + str(num_mes_per_deg))
        print("hor_step = " + str(hor_step))
        print("ver_step = " + str(ver_step))
        self.ardiuno.start(num_mes_per_deg, hor_step, ver_step)
        # self.ser.write(bytes(num_mes_per_deg))
        # self.ser.write(ver_step)
        # self.ser.write(hor_step)

        # Calculate number of steps
        num_steps = int(((self.MAX_STEPS / 2) / hor_step) +
                        ((self.MAX_STEPS) / 4) / ver_step)

        #count = 0
        seq = []
        self.pomiar = Pomiar(self.title.text(), num_steps)

        # Read data
        print("measurement in progress")
        temp_pomiar = self.ardiuno.get_pomiary()
        print("measurement done 1!")
        self.pomiar.points_list = temp_pomiar.points_list
        self.dimension_choice()
        print("measurement done 2!")
        self.ardiuno.disconnect()
        print("connection closed")
        
        # while True:
        #     for c in self.ser.read():
        #         if chr(c) == '\n':
        #             point = Punkt(seq[0], seq[1] / 180, seq[2] / 180)
        #             self.pomiar.add_point(point)

        #             if count == self.pomiar.mes_num:
        #                 self.dimension_choice()
        #                 print("measurement done!")
        #                 self.ser.close()
        #                 print("connection closed")
        #                 return self.pomiar

        #             seq = []
        #             count += 1
        #             break

        #         self.completed += int((num_steps * 3) / 100)
        #         self.progressBar.setValue(self.completed)
        #         seq.append(chr(c))

        self.pomiar.calculate_all()
        self.create_graph()
        self.saveFile.setEnabled(True)

    def create_graph(self):
        self.MplWidget.canvas.axes.clear()
        self.MplWidget.canvas.axes.scatter3D(self.pomiar.x_list, self.pomiar.y_list, self.pomiar.z_list, c='r', cmap='OrRd_r')
        self.MplWidget.canvas.axes.scatter3D([0], [0], [0], c='b', cmap='OrRd_r', s=250)
        # Data for three-dimensional scattered points
        self.MplWidget.canvas.axes.set_xlabel('x axis')
        self.MplWidget.canvas.axes.set_ylabel('y axis')
        self.MplWidget.canvas.axes.set_zlabel('z axis')
        self.MplWidget.canvas.set_window_title(self.pomiar.mes_title)
        self.MplWidget.canvas.draw()

    def create_graph2d(self):
        self.MplWidget2d.canvas.axes.clear()
        self.MplWidget2d.canvas.axes.plot(self.pomiar.x_list[:179], self.pomiar.y_list[:179], '.')
        
        # Data for two-dimensional scattered points
        self.MplWidget2d.canvas.axes.set_xlabel('x axis')
        self.MplWidget2d.canvas.axes.set_ylabel('y axis')
        self.MplWidget2d.canvas.set_window_title(self.pomiar.mes_title)
        self.MplWidget2d.canvas.draw()

    def create_graph2d_morph(self):
        self.MplWidget2dmorf.canvas.axes.clear()
        self.MplWidget2dmorf.canvas.axes.plot(self.pomiar.x_list[:179], self.pomiar.y_list[:179], '.')
        
        # Data for two-dimensional scattered points (1st graph)
        self.MplWidget2dmorf.canvas.axes.set_xlabel('x axis')
        self.MplWidget2dmorf.canvas.axes.set_ylabel('y axis')
        self.MplWidget2dmorf.canvas.draw()
        
        self.MplWidget2dmorf.canvas2.axes.clear()
        self.MplWidget2dmorf.canvas2.axes.plot(self.pomiar_morph.x_list, self.pomiar_morph.y_list, '.')
        
        # Data for two-dimensional scattered points (2nd graph)
        self.MplWidget2dmorf.canvas2.axes.set_xlabel('x axis')
        self.MplWidget2dmorf.canvas2.axes.set_ylabel('y axis')
        self.MplWidget2dmorf.canvas2.draw()

    def create_graph2d_aprox(self):
        self.MplWidget2daprox.canvas.axes.clear()
        self.MplWidget2daprox.canvas.axes.plot(self.pomiar.x_list, self.pomiar.y_list, '.')

        # Data for two-dimensional scattered points (1st graph)
        self.MplWidget2daprox.canvas.axes.set_xlabel('x axis')
        self.MplWidget2daprox.canvas.axes.set_ylabel('y axis')
        self.MplWidget2daprox.canvas.draw()

        # Data for two-dimensional scattered points (2nd graph)
        self.MplWidget2daprox.canvas2.axes.set_xlabel('x axis')
        self.MplWidget2daprox.canvas2.axes.set_ylabel('y axis')

        self.MplWidget2daprox.canvas2.axes = plt.gca()
        self.MplWidget2daprox.canvas2.axes.set_xlim([-100, 100])
        self.MplWidget2daprox.canvas2.axes.set_ylim([0, 80])

    def update_morph(self, struct_size, struct_type):
        # todo: check if update necessary
        self.morph(struct_size, struct_type)

    def morph(self, struct_size, struct_type):
        w, h = 180, 400
        img = [[0 for x in range(w)] for y in range(h)]
        img = np.zeros((h, w))

        i = 0
        for point in self.pomiar.points_list:
            img[:int(point.d), i] = 1
            i += 1
            if i == 180:
                break

        # Odwróć obraz
        img = np.flip(img, 0)

        # Element strukturalny
        kernel = np.zeros((struct_size, struct_size))

        if struct_type == 1:
            kernel = np.ones((struct_size, struct_size), np.uint8)
        elif struct_type == 0:
            kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (struct_size, struct_size))

        opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
        closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

        y, x = closing.shape

        j = 0
        data = {}

        # Utworzenie pomiaru dla morphology
        self.pomiar_morph = Pomiar("Morphology", 180)
        while j < x:
            i = 0
            while closing[i, j] == 0:
                i += 1
            self.pomiar_morph.add_point(Punkt(float(y - i), j, 0))
            j += 1
            
        self.pomiar_morph.calculate_all()
        print(self.pomiar_morph.y_list)


    def exit(self):
        print("exiting...")
        self.close()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()


if __name__ == "__main__":
    main()
