from typing import Any


class Vector:

    def __init__(self, initial_x = 0):
        self.values = []
        self.x = initial_x

    @property
    def x(self):
        return self.__x * 2 


    @x.setter
    def x(self, new_value):
        self.__x = new_value

v = Vector(12)  
print(v.x)
v.x = 15