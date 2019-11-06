print("hello")

import serial
import time
import statistics
import math
import matplotlib.pyplot as plt

ser = serial.Serial(
    port='COM3',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)


print("connected to: " + ser.portstr)

#this will store the line
seq = []
count = 1
measurements = 3;

m = [180]

time.sleep(3)


def create_graph(data):
    fig = plt.figure(figsize=(10, 10))
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
    li, = ax.plot(x, y, 'o')
    # Set default axis in range of -100 to 100
    # plt.axis([-200, 200, -200, 200])
    axes = plt.gca()
    axes.set_xlim([-200, 200])
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


def ArduinoSend(data):
    ser.write(format(('{}\n').format(data)).encode())

ArduinoSend("")

print("witten")


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
                i=0
                while i < measurements:
                    distance.append(int(data[i+1]) / 58.2)
                    i+=1
                print("angle: " + str(angle) + "; " + str(distance))
                m.insert(angle, statistics.median(distance))
                if angle == 180:
                    print("creating graph ... ")
                    create_graph(m)
                    print("done!")
            except ValueError:
                print(joined_seq)
            except IndexError:
                print(joined_seq)

            seq = []
            count += 1
            break
        seq.append(chr(c))  # convert from ANSII
        joined_seq = ''.join(str(v) for v in seq)  # Make a string from array


ser.close()

