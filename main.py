print("hello")


class Arduino:

    def __init__(self):
        self.ser = 0
        self.measurements = 0
        self.h_step = 0
        self.v_step = 0
        self.baudrate = 38400
        self.com_port = 'COM3'
    
    def connect(self):
        self.ser = serial.Serial(
        port=self.com_port,\
        baudrate=self.baudrate,\
        parity=serial.PARITY_NONE,\
        stopbits=serial.STOPBITS_ONE,\
        bytesize=serial.EIGHTBITS,\
            timeout=0)
        print("connected to: " + self.ser.portstr)



    def disconnect(self):
        self.ser.close()

    def start(self, measurements, h_step, v_step):
        self.measurements = measurements
        self.h_step = h_step
        self.v_step = v_step
        sent_bytes = self.ser.write(struct.pack("<BHH", measurements, h_step, v_step))

    def get_pomiary(self):
        r = []
        h = []
        v = []

        how_many_measurements = (4076/2/self.h_step) * (4076/4/self.v_step) # ilosc wszystkich pomiarow do zrobienia
        print("how_many_measurements = " + str(how_many_measurements))
        i = 0
        while i < how_many_measurements:
            
            h1=self.ser.readline() 
            if h1:
                if 1 == 1: # len(h1) == (4+2+2+2):
                    #is legit pomiar
                    print(i)
                    i1, i2, i3 = struct.unpack('<LHHxx', h1)
                    print("=======================")
                    print("r = " + str(i1))
                    print("h = " + str(i2))
                    print("v = " + str(i3))
                    r.append(i1)
                    h.append(i2)
                    v.append(i3)
                    #print("=======================")
                    #print(' '.join(format(ord(x), 'b') for x in h1))
                    i += 1



import serial
import time
import statistics
import math
import matplotlib.pyplot as plt
import csv
import os
import struct 


print("creating arduino object ... ")
a = Arduino()
print("connecting ... ")
a.connect()

time.sleep(3)

print("starting ... ")
a.start(2, 185, 105)
print("getting ... ")
a.get_pomiary()
a.disconnect()




# def packIntegerAsB(value):
#     """Packs a python 4 byte unsigned integer to an arduino unsigned long"""
#     return struct.pack('b', value)    

# def packIntegerAsULong(value):
#     """Packs a python 4 byte unsigned integer to an arduino unsigned long"""
#     return struct.pack('h', value)   

# ser = serial.Serial(
#     port='COM3',\
#     baudrate=115200,\
#     parity=serial.PARITY_NONE,\
#     stopbits=serial.STOPBITS_ONE,\
#     bytesize=serial.EIGHTBITS,\
#         timeout=0)

# print("connected to: " + ser.portstr)

# time.sleep(3)

# #this will store the line
# print("writing ... ")
# send_bytes = ser.write(struct.pack(">BHH", 3, 200, 100))
# print("bytes sent = " + str(send_bytes))

# i = 0
# buff = struct.pack("<BHH", 3, 200, 100)
# for e in buff:
#     print(str(i) + " > " + str(int(e)))
#     i += 1

# # print(" ... writing 3")
# # send_bytes = ser.write(packIntegerAsB(3))
# # print(str(send_bytes) + " ... writing 200")
# # send_bytes = ser.write(packIntegerAsULong(200))
# # print(str(send_bytes) + " ... writing 100")
# # send_bytes = ser.write(packIntegerAsULong(100))
# # print(str(send_bytes))
# buff = []

# while True:

#     h1=ser.readline()
    
#     if h1:
#         print(str(h1))
#         print("=======================")
#         print(' '.join(format(ord(x), 'b') for x in str(h1)))
#         print("=======================")
#         if len(h1) == (4+2+2+2):
#             i1, i2, i3 = struct.unpack('<LHHxx', h1)
#             print("=======================")
#             print("1 = " + str(i1))
#             print("2 = " + str(i2))
#             print("3 = " + str(i3))
        
    
    # if ser.read() :
    #     print("avg : ") # 4 bytes
    #     buff = ser.read()
    #     #avg = struct.unpack('i', buff)
    #     print(buff)

    # if ser.read() :
    #     print("h position : ") # 2 bytes
    #     buff = ser.read()
    #     #h_pos = struct.unpack('i', buff)
    #     print(buff)

    # if ser.read() :
    #     print("v position : ") # 2 bytes
    #     buff = ser.read()
    #     #v_pos = struct.unpack('i', buff)
    #     print(buff)



#ser.close()

