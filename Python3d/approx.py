import math
import numpy as np
import matplotlib.pyplot as plt

def approx(pomiar_morph, radius, main):
    z = [] 

    main.MplWidget2daprox.canvas2.axes.clear()

    for i in range(0, pomiar_morph.mes_num-1, 20):                             
        tupleoflists = approximation(radius, pomiar_morph.x_list, pomiar_morph.y_list, pomiar_morph.x_list[i], pomiar_morph.y_list[i])       
        temp = tupleoflists[0]                                  
        z.append(temp[0])                                       
        trendpoly = np.poly1d(tupleoflists[0])

        x_line = range(-400, 400, 1)
        y_line = trendpoly(x_line)

        main.MplWidget2daprox.canvas2.axes.set_xlim([-100, 100])
        main.MplWidget2daprox.canvas2.axes.set_ylim([0, 80])
        main.MplWidget2daprox.canvas2.axes.plot(x_line, y_line)

    main.MplWidget2daprox.canvas2.draw()

    return x_line, y_line


                                                                       
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
    #print(z[0])                                                        
    listoflists = (list(z), list(new_x))                               
    return listoflists                                                 