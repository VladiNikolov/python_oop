import math
from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def calculate_area(self):
        return math.pi * self.__radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.__radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self._width = width
        self.__height = height

    def calculate_area(self):
        return  self._width * self.__height

    def calculate_perimeter(self):
        return (self._width + self.__height) * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
