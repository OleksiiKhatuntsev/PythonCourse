import math

# Problem 1
# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line():

    def __init__(self, coordinate_1, coordinate_2):
        self.coordinate_1 = coordinate_1
        self.coordinate_2 = coordinate_2

    def get_distance(self):
        return math.sqrt((self.coordinate_2[0] - self.coordinate_1[0])**2 + (self.coordinate_2[1] - self.coordinate_1[1])**2)

    def get_slope(self):
        return (self.coordinate_2[1] - self.coordinate_1[1])/(self.coordinate_2[0] - self.coordinate_1[0])

# Problem 2
# Fill in the class Cylinder with volume and surface area methods

class Cylinder():

    PI = 3.14

    def __init__(self, h, r):
        self.h = h
        self.r = r

    def get_volume(self):
        return self.PI * self.r * self.r * self.h

    def get_surface_area(self):
        return 2*self.PI*self.r*(self.h + self.r)

line = Line((3,2), (8,10))
cylinder = Cylinder(2,3)

print(line.get_distance())
print(line.get_slope())

print(cylinder.get_volume())
print(cylinder.get_surface_area())

