print("hello")

import serial
import time
import statistics
import math
import matplotlib.pyplot as plt
import csv
import os

ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

print("connected to: " + ser.portstr)

time.sleep(3)

#this will store the line
seq = []
count = 1

measurements = input("Podaj liczbę pomiarów do wykonania: ")
measurements = measurements.strip()

if measurements == '2':
    ser.write(bytes(measurements, 'utf-8'))
elif measurements == '3':
    ser.write(bytes(measurements, 'utf-8'))
else:
    measurements = '1'
    ser.write(bytes(measurements, 'utf-8'))

measurements = int(measurements)

m = [0]*181

time.sleep(3)


def create_graph(data):
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
    
    i = 0
    while i < 180:
        y.append(math.sin(math.radians(i)) * data[i])
        x.append(math.cos(math.radians(i)) * data[i])
        # print(y)
        # print(x)
        # plt.pause(0.1)
        i += 1

    li.set_ydata(y)
    li.set_xdata(x)
    plt.show()


def save(data):
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


def read(filename):
    DIR = os.getcwd() + os.path.sep
    with open(DIR + filename) as file:
        data = []
        file_reader = csv.reader(file, delimiter=',')
        for row in file_reader:
            data.append(float(row[1]))
            
    return data
    
'''
def ArduinoSend(data):
    ser.write(format(('{}\n').format(data)).encode())

#ArduinoSend("")
'''
print("written")


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
                m[angle] = statistics.median(distance);
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

