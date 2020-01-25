import time
import statistics
import math
from mpl_toolkits import mplot3d
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

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


def save_file_3d(self, data):
    print("(NOT DONE)saving file ...")
    try:
        filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if filename == "":
            return
        with open(filename, 'w', newline='') as file:
            file = csv.writer(file, delimiter=',')

            horizontal_angle = 0
            vertical_angle = 0

            while horizontal_angle < len(data):
                while len(data.get(horizontal_angle)):
                    file.writerow([
                        str(horizontal_angle),
                        str(vertical_angle),
                        str(data[horizontal_angle].get(vertical_angle))
                    ])
                    vertical_angle += 1
                horizontal_angle += 5

    except Exception as e:
        self.showdialog("Error", "failed to save file :(\n" + str(e))


def open_file_3d():
    print("opening file...")
    #self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.csv)")[0]
    filename = "data/great-angles-2d.csv"
    data = {}
    inner_data = {}
    count = 0
    if filename:
        with open(filename, "rt") as file:
            #self.openLabel.setText("opened: " + self.filename)
            file_reader = csv.reader(file, delimiter=',')
            for row in file_reader:
                # self.data.append(float(row[1]))
                
                inner_data[int(row[1])] = float(row[2])
                count += 1

                if (count == 180):
                    data[int(row[0])] = inner_data
                    count = 0
                #print("reading: " + str(row[0]) + " > " + str(row[1]))

    return data
    # print(self.data)
    # self.saveButton.setEnabled(True)
    # self.setButtonsEnable(True)


def new_create_graph(data, title):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    zdata = []
    xdata = []
    ydata = []

    # convert data to coordinates
    for vertical_angle, data_item in data.items():
        for horizontal_angle in data_item:
            xdata.append(float(data_item[horizontal_angle]) * math.sin(math.radians(90 - int(vertical_angle))) * math.cos(math.radians(int(horizontal_angle))))
            ydata.append(float(data_item[horizontal_angle]) * math.sin(math.radians(90 - int(vertical_angle))) * math.sin(math.radians(int(horizontal_angle))))
            zdata.append(float(data_item[horizontal_angle]) * math.cos(math.radians(90 - int(vertical_angle))))
        
        #i += 10

    print(zdata)

    # Data for three-dimensional scattered points
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='OrRd_r')
    ax.set_xlabel('x axis')
    ax.set_ylabel('y axis')
    ax.set_zlabel('z axis')
    plt.title(title)
    plt.show()





if __name__ == "__main__":

    '''
    p = Punkt(10, 30, 40)
    print(p.calculate())

    pomiar = Pomiar("random ttiel")
    pomiar.add_point(p)

    pomiar.save_pickle("pickle_pomiar.obj")
    print("saved")

    pomiar.save_with_title("")

    pomiar2 = Pomiar.load_pickle(pomiar.mes_title + ".obj")
    pomiar2.print_info()
    '''

    data = open_file_3d()
    p = Pomiar("test", 1)

    for vertical_angle, data_item in data.items():
        for horizontal_angle in data_item:
            p.add_point(Punkt(data_item[horizontal_angle], horizontal_angle, vertical_angle))

    p.calculate_all()
    p.display_plot()

