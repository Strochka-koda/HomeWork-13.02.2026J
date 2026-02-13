import math

class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self) -> float:
        return self.length * self.width

    def perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Triangle:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print(f"Прямоугольник: площадь = {rect.area()}, периметр = {rect.perimeter()}")

    tri = Triangle(3, 4, 5)
    print(f"Треугольник: площадь = {tri.area()}, периметр = {tri.perimeter()}")

    circ = Circle(2)
    print(f"Круг: площадь = {circ.area()}, длина окружности = {circ.perimeter()}")