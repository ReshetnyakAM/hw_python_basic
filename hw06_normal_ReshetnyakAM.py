'''
Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.
'''
from math import sqrt
class Point:
    def __init__(self, x = 0, y = 0):
        self.X = x
        self.Y = y

class Triangle:
    A = Point()
    B = Point()
    C = Point()

    def perimeter(self):
        AB = sqrt((self.A.X - self.B.X)**2 + (self.A.Y - self.B.Y)**2)
        BC = sqrt((self.B.X - self.C.X)**2 + (self.B.Y - self.C.Y)**2)
        AC = sqrt((self.A.X - self.C.X)**2 + (self.A.Y - self.C.Y)**2)
        return AB + BC + AC

    # Векторное произведение векторов равно площади параллелограма на них построенного
    # Нахожу векторное произведение и делю пополам т.к. треугольник - половина параллелограмма
    def square(self):
        vAB = Point(self.A.X - self.B.X, self.A.Y - self.B.Y)
        vAC = Point(self.A.X - self.C.X, self.A.Y - self.C.Y)
        return ((vAB.X * vAC.Y) - (vAB.Y * vAC.X))/2

    
    def h(self):
        AB = sqrt((self.A.X - self.B.X)**2 + (self.A.Y - self.B.Y)**2)
        BC = sqrt((self.B.X - self.C.X)**2 + (self.B.Y - self.C.Y)**2)
        AC = sqrt((self.A.X - self.C.X)**2 + (self.A.Y - self.C.Y)**2)
        S = self.square()
        h1 = 2 * S / AB
        h2 = 2 * S / BC
        h3 = 2 * S / AC
        return {'h1': h1, 'h2': h2, 'h3': h3}

triangle = Triangle()
triangle.A = Point(0,0)
triangle.B = Point(1,0)
triangle.C = Point(0,1)
print(triangle.perimeter())
print(triangle.square())
print(triangle.h())


