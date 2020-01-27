import serial
import time
import os
import struct 
import copy

from Pomiar import Pomiar
from Punkt import Punkt


class Arduino:

    def __init__(self):
        self.ser = 0
        self.measurements = 0
        self.h_step = 0
        self.v_step = 0
        self.baudrate = 38400
        self.com_port = 'COM3'
        self.pomiar = None
    
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
        how_many_measurements = (4076/2/self.h_step) * (4076/4/self.v_step) # ilosc wszystkich pomiarow do zrobienia
        self.pomiar = Pomiar("czxczxc", how_many_measurements)
        print("how_many_measurements = " + str(how_many_measurements))
        i = 0
        h2=None
        while i < how_many_measurements:#todo 
            count = 0
            seq = []
            
            h1=self.ser.readline() 
            
            if h1:
                if(h2!=None):
                    h1=h2+h1
                    print("len1 = " + str(len(h1)) + " "+str(len(h2)))
                    h2=None
                if(len(h1)<10 and h2==None):
                    h2=copy.copy(h1)
                

                try:
                    i1, i2, i3 = struct.unpack('<LHHxx', bytes(h1))
                    print("=======================")
                    print("r = " + str(i1))
                    print("h = " + str(i2))
                    print("v = " + str(i3))
                    if(i1==0 and i2==257 and i3==257):
                        break
                    if i1 == 0 and i2 == 1 and i3 == 1:
                        break
                    
                    distance = i1 / 58.2
                    h_ang = ((i2-32) /4076) * 360
                    v_ang = ((i3-32) /4076) * 360
                    p = Punkt(distance, h_ang, v_ang)
                    self.pomiar.add_point(p)
                except:
                    pass

            

                
        print("done lol")              
        return self.pomiar