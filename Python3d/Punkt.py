import math

class Punkt:

    def __init__(self, d, h_ang, v_ang):
        self.x = 0
        self.y = 0
        self.z = 0
        self.d = d  # odległość
        self.horizontal_angle = h_ang
        self.vertical_angle = v_ang

    def calculate(self):
        if(self.d>400 or self.vertical_angle>30) :
            self.d=0
        self.x = float(self.d) * math.sin(math.radians(int(self.vertical_angle)-90)) * math.cos(math.radians(int(self.horizontal_angle)))
        self.y = float(self.d) * math.sin(math.radians(int(self.vertical_angle)-90)) * math.sin(math.radians(int(self.horizontal_angle)))
        self.z = float(self.d) * math.cos(math.radians(int(self.vertical_angle)-90))



        if self.vertical_angle == 0:
            self.z = 0
        
        return (self.x, self.y, self.z)

