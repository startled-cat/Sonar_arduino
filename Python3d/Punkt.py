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
        self.x = float(self.d) * math.sin(math.radians(int(self.vertical_angle))) * math.cos(math.radians(int(self.horizontal_angle)))
        self.y = float(self.d) * math.sin(math.radians(int(self.horizontal_angle)))
        self.z = float(self.d) * math.cos(math.radians(int(self.vertical_angle))) * math.cos(math.radians(int(self.horizontal_angle)))
        
        return (self.x, self.y, self.z)

