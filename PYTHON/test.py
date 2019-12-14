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


import sys

import cv2 as cv

filename1 = "Sonar\dane_12_12\dane1.csv"
filename2 = "Sonar\dane_12_12\dane2.csv"
filename3 = "Sonar\dane_12_12\dane3.csv"

def morph(data, struct_size):
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

        return data

data1 = {}
data2 = {}
data3 = {}

data2_x = -19
data2_y = 0

data3_x = -9
data3_y = 18

with open(filename1, "rt") as file:
    file_reader = csv.reader(file, delimiter=',')
    for row in file_reader:
        data1[int(row[0])]=float(row[1])

with open(filename2, "rt") as file:
    file_reader = csv.reader(file, delimiter=',')
    for row in file_reader:
        data2[int(row[0])]=float(row[1])

with open(filename3, "rt") as file:
    file_reader = csv.reader(file, delimiter=',')
    for row in file_reader:
        data3[int(row[0])]=float(row[1])        

data1 = morph(data1, 15)
data2 = morph(data2, 15)
data3 = morph(data3, 15)

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


y1 = []
x1 = []

y2 = []
x2 = []

y3 = []
x3 = []
#mark, = ax.plot(th, y, marker='o', alpha=.5, ms=10)

li1, = ax.plot(x1, y1, marker='o', alpha=.5, ms=5)
li2, = ax.plot(x2, y2, marker='o', alpha=.5, ms=5)
li3, = ax.plot(x3, y3, marker='o', alpha=.5, ms=5)


axes = plt.gca()
axes.set_xlim([-100, 100])
axes.set_ylim([0, 100])

ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

i = 0
while i < len(data1) :
    y1.append(math.sin(math.radians(i)) * (data1.get(i)))
    x1.append(math.cos(math.radians(i)) * (data1.get(i)))
    i += 1

i = 0
while i < len(data2) :
    y2.append(math.sin(math.radians(i)) * (data2.get(i)) + data2_y)
    x2.append(math.cos(math.radians(i)) * (data2.get(i)) + data2_x)
    i += 1

i = 0
while i < len(data3) :
    y3.append(math.sin(math.radians(i)) * (data3.get(i)) + data3_y)
    x3.append(math.cos(math.radians(i)) * (data3.get(i)) + data3_x)
    i += 1


li1.set_ydata(y1)
li1.set_xdata(x1)

li2.set_ydata(y2)
li2.set_xdata(x2)

li3.set_ydata(y3)
li3.set_xdata(x3)

plt.title("title")
plt.show()




import matplotlib.pyplot as plt
from skimage import draw
arr = np.zeros((200, 200))
stroke = 3
# Create an outer and inner circle. Then subtract the inner from the outer.
radius = 80
inner_radius = radius - (stroke // 2) + (stroke % 2) - 1 
outer_radius = radius + ((stroke + 1) // 2)
ri, ci = draw.circle(100, 100, radius=inner_radius, shape=arr.shape)
ro, co = draw.circle(100, 100, radius=outer_radius, shape=arr.shape)

arr[ro, co] = 1
arr[ri, ci] = 0

plt.imshow(arr)
plt.show()