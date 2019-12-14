import math

def approx(data, radius):
    x, y = toXY(data)

    #write your code here

    print(x)
    print(y)
    print(radius)

def toXY(data):
    y = []
    x = []
    i = 0
    while i < len(data) :
        y.append(math.sin(math.radians(i)) * (data.get(i)))
        x.append(math.cos(math.radians(i)) * (data.get(i)))
        i += 1
    return x, y