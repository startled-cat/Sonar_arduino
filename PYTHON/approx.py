import math
import numpy as np
import matplotlib.pyplot as plt

def approx(data, radius):
    x, y = toXY(data)

    z = [] 

    for i in range(0, len(data)-1):                             
        tupleoflists = approximation(radius, x, y, x[i], y[i])       
        temp = tupleoflists[0]                                  
        z.append(temp[0])                                       
        trendpoly = np.poly1d(tupleoflists[0])                  
        plt.plot(tupleoflists[1], trendpoly(tupleoflists[1]))   

def toXY(data):
    y = []
    x = []
    i = 0
    while i < len(data) :
        y.append(math.sin(math.radians(i)) * (data.get(i)))
        x.append(math.cos(math.radians(i)) * (data.get(i)))
        i += 1
    return x, y

                                                                       
def approximation(r, x, y, start_x, start_y):                          
    new_x = []                                                         
    new_y = []                                                         
    new_x.append(start_x)                                              
    new_y.append(start_y)                                              
    for i, j in zip(x, y):                                             
        points_len = math.hypot(i - start_x, j - start_y)              
        if points_len > r:                                             
            continue                                                   
        new_x.append(i)                                                
        new_y.append(j)                                                
                                                                       
        #print(str(len(new_x)))                                        
                                                                       
    z = np.polyfit(new_x, new_y, 1)                                    
    print(z[0])                                                        
    listoflists = (list(z), list(new_x))                               
    return listoflists                                                 