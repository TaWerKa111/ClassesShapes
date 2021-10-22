from math import sqrt, pi


class Shape:
    """ Класс фигура """
    title = 'Фигура'
    COUNT = 0

    def __int__(self):
        self.__class__.COUNT += 1

    def area(self):
        """ Площадь фигуры, или ее поверхности """
        pass

    def show_info(self):
        pass

    @classmethod
    def count_shapes(cls):
        return cls.COUNT


class Square(Shape):
    title = 'Квадрат'

    def __init__(self, length: float):
        super().__init__()
        self.length = length

    def area(self) -> float:
        return self.length ** 2

    def perimeter(self) -> float:
        return self.length * 4

    def diagonal(self) -> float:
        return sqrt((self.length ** 2) * 2)

    def show_info(self):
        print(f'Площадь квадрата = {self.area()}\n'
              f'Периметр квадрата = {self.perimeter()}\n'
              f'Диаганаль квадрата = {self.diagonal()}\n')


class Rectangle(Shape):
    title = 'Прямоугольник'

    def __init__(self, width: float, length: float):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> float:
        return self.width * self.length

    def perimeter(self) -> float:
        return (self.width + self.length) * 2

    def diagonal(self) -> float:
        return sqrt(self.width ** 2 + self.length ** 2)

    def show_info(self):
        print(f'Площадь прямоугольника = {self.area()}\n'
              f'Периметр прямоугольника = {self.perimeter()}\n'
              f'Диаганаль прямоугольника = {self.diagonal()}\n')


class Circle(Shape):
    title = 'Круг'

    def __init__(self, radius: float):
        """ Инициальзация значений.
            radius - радиус круга"""
        super().__init__()
        self.radius = radius

    def area(self) -> float:
        """ Площадь круга """
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        """ Периметр круга """
        return 2 * pi * self.radius

    def diameter(self) -> float:
        """ Диаметр круга """
        return 2 * self.radius

    def show_info(self):
        print(f'Площадь окружности = {self.area()}\n'
              f'Периметр окружности = {self.perimeter()}\n'
              f'Диаметр окружности = {self.diameter()}\n')


class Triangle(Shape):
    title = 'Треугольник'

    def __init__(self, side1: float, side2: float, side3: float):
        """ Инициальизация строно треугольника """
        super().__init__()
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        """ Расчет площади треугольника по формуле Герона,
            p - полупериметр"""
        p = (self.side1 + self.side2 + self.side3) / 2
        return sqrt(p*(p - self.side1)*(p-self.side2)*(p-self.side3))

    def perimeter(self) -> float:
        """ Расчет периметри треугольника """
        return self.side1 + self.side2 + self.side3

    def high(self, side: int) -> float:
        """ Расчет высоты проведенно к стороне side, p - полупериметр"""
        sides = {
            1: self.side1,
            2: self.side2,
            3: self.side3
        }
        return 2 * self.area() / sides[side]

    def show_info(self):
        print(f'Площадь триугольника = {self.area()}\n'
              f'Периметр триугольника = {self.perimeter()}\n'
              f'Высота триугольника, проведенной к 1ой стороне = {self.high(1)}\n')


class Trapezoid(Shape):
    title = 'Трапеция'

    def __init__(self, big_foot: float, small_foot: float, side1: float, side2: float):
        super().__init__()
        self.big_foot = big_foot
        self.small_foot = small_foot
        self.side1 = side1
        self.side2 = side2

    def area(self):
        """ Расчет площади трапеции по формуле Герона.
            p - полумпериметр
            div_foot = частное от суммы оснований на разность оснований"""
        p = (self.side1 + self.side2 + self.big_foot + self.small_foot) / 2
        div_foot = (self.big_foot + self.small_foot) / (self.big_foot - self.small_foot)
        return div_foot * sqrt((p - self.big_foot) *\
                               (p - self.small_foot) *\
                               (p - self.big_foot - self.side1) *\
                               (p - self.big_foot - self.side2))

    def perimeter(self) -> float:
        return self.side1 + self.side1 + self.small_foot + self.big_foot

    def show_info(self):
        print(f'Площадь трапеции = {self.area()}\n'
              f'Периметр трапеции = {self.perimeter()}\n')


class Rhomb(Shape):
    title = 'Ромб'

    def __init__(self, diagonal1: float, diagonal2: float):
        """ Инициализация значений.
            diagonal1 и diagonal2 - диагонали ромба
            side - сторона ромба (Находятся по свойству: Сумма квадратов
            диагоналей равна квадрату стороны, умноженному на 4.)"""
        super().__init__()
        self.diagonal1 = diagonal1
        self.diagonal2 = diagonal2
        self.side = sqrt((self.diagonal1**2 + self.diagonal2**2) / 4)

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return self.side * 4

    def show_info(self):
        print(f'Площадь ромба = {self.area()}\n'
              f'Периметр ромба = {self.perimeter()}\n'
              f'Сторона ромба = {self.side}\n')
