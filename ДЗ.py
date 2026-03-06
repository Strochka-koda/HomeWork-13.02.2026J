import math

class Figure:
    def calculate(self):
        pass

class Sphere(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate(self):
        volume = (4/3) * math.pi * (self.radius ** 3)
        area = 4 * math.pi * (self.radius ** 2)
        return volume, area

    def __str__(self):
        v, a = self.calculate()
        return f"СФЕРА: Объём = {v:.2f}, Площадь = {a:.2f}"

class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calculate(self):
        area = self.side ** 2
        return 0, area

    def __str__(self):
        _, a = self.calculate()
        return f"КВАДРАТ: Площадь = {a:.2f}"

class Triangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate(self):
        area = 0.5 * self.base * self.height
        return 0, area

    def __str__(self):
        _, a = self.calculate()
        return f"ТРЕУГОЛЬНИК: Площадь = {a:.2f}"
