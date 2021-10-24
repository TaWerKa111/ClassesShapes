from Classes2DShapes import Rectangle, Rhomb, Circle, Square, Triangle, Trapezoid
import unittest
from math import pi


class Test_Square(unittest.TestCase):
    """ Юнит тесты для класс квадрат """
    def test_area(self):
        """ Проверка вычисления площади """
        self.assertEqual(Square(2).area(), 2 * 2)
        self.assertEqual(Square(1).area(), 1)
        self.assertEqual(Square(0).area(), 0)
        self.assertEqual(Square(2.5).area(), 2.5 * 2.5)

    def test_perimeter(self):
        """ Проверка вычисления периметра """
        self.assertEqual(Square(2).perimeter(), 2 * 4)
        self.assertEqual(Square(1).perimeter(), 4)
        self.assertEqual(Square(0).perimeter(), 0)
        self.assertEqual(Square(2.5).perimeter(), 2.5 * 4)

    def test_diagonal(self):
        """ Проверка вычисления периметра """
        self.assertEqual(round(Square(2).diagonal(), 2), round(2.8284271247461903, 2))
        self.assertEqual(round(Square(1).diagonal(), 2), round(1.4142135623730951, 2))
        self.assertEqual(Square(0).diagonal(), 0)
        self.assertEqual(round(Square(2.5).diagonal(), 2), round(3.5355339059327378, 2))

    def test_values(self):
        """ Проверка значений """
        self.assertRaises(ValueError, Square, -1)
        self.assertRaises(ValueError, Square, -10)

    def test_type(self):
        """ Проверка типов значений """
        self.assertRaises(TypeError, Square, '21')
        self.assertRaises(TypeError, Square, [12])
        self.assertRaises(TypeError, Square, True)
        self.assertRaises(TypeError, Square, {12})


class Test_Rectangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Rectangle(2, 1).area(), 2 * 1)
        self.assertEqual(Rectangle(1, 1).area(), 1)
        self.assertEqual(Rectangle(0, 0).area(), 0)
        self.assertEqual(Rectangle(2.5, 3.5).area(), 2.5 * 3.5)

    def test_perimeter(self):
        self.assertEqual(Rectangle(2, 1).perimeter(), 6)
        self.assertEqual(Rectangle(1, 1).perimeter(), 4)
        self.assertEqual(Rectangle(0, 0).perimeter(), 0)
        self.assertEqual(Rectangle(2.5, 3.5).perimeter(), 12)

    def test_diagonal(self):
        self.assertEqual(round(Rectangle(2, 1).diagonal(), 2), round(2.23606797749979, 2))
        self.assertEqual(round(Rectangle(1, 1).diagonal(), 2), round(1.4142135623730951, 2))
        self.assertEqual(Rectangle(0, 0).diagonal(), 0)
        self.assertEqual(round(Rectangle(2.5, 3.5).diagonal(), 2), round(4.301162633521313, 2))

    def test_values(self):
        self.assertRaises(ValueError, Rectangle, -1, -2)
        self.assertRaises(ValueError, Rectangle, -10, -3)

    def test_type(self):
        self.assertRaises(TypeError, Rectangle, '21', '12')
        self.assertRaises(TypeError, Rectangle, [12], [12])
        self.assertRaises(TypeError, Rectangle, True, True)
        self.assertRaises(TypeError, Rectangle, {12}, {'we'})


class Test_Circle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Circle(2).area(), pi * 2**2)
        self.assertEqual(Circle(1).area(), pi)
        self.assertEqual(Circle(0).area(), 0)
        self.assertEqual(Circle(2.5).area(), pi*2.5**2)

    def test_perimeter(self):
        self.assertEqual(Circle(2).perimeter(), 4 * pi)
        self.assertEqual(Circle(1).perimeter(), 2 * pi)
        self.assertEqual(Circle(0).perimeter(), 0)
        self.assertEqual(Circle(2.5).perimeter(), 5 * pi)

    def test_diameter(self):
        self.assertEqual(Circle(2).diameter(), 4)
        self.assertEqual(Circle(1).diameter(), 2)
        self.assertEqual(Circle(0).diameter(), 0)
        self.assertEqual(Circle(2.5).diameter(), 2.5 * 2)

    def test_values(self):
        self.assertRaises(ValueError, Circle, -1)
        self.assertRaises(ValueError, Circle, -10)

    def test_type(self):
        self.assertRaises(TypeError, Circle, '21')
        self.assertRaises(TypeError, Circle, [12])
        self.assertRaises(TypeError, Circle, True)
        self.assertRaises(TypeError, Circle, {12})


class Test_Rhomb(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Rhomb(2, 3).area(), 3)
        self.assertEqual(Rhomb(1, 1).area(), 0.5)
        self.assertEqual(Rhomb(0, 0).area(), 0)
        self.assertEqual(Rhomb(2.5, 3.5).area(), 4.375)

    def test_perimeter(self):
        self.assertEqual(round(Rhomb(2, 3).perimeter(), 2), round(7.21112, 2))
        self.assertEqual(round(Rhomb(1, 1).perimeter(), 2), round(2.828428, 2))
        self.assertEqual(round(Rhomb(0, 0).perimeter(), 2), 0)
        self.assertEqual(round(Rhomb(2.5, 3.5).perimeter(), 2), round(8.60232, 2))

    def test_values(self):
        self.assertRaises(ValueError, Rhomb, -1, -2)
        self.assertRaises(ValueError, Rhomb, -10, -3)

    def test_type(self):
        self.assertRaises(TypeError, Rhomb, '21', 'five')
        self.assertRaises(TypeError, Rhomb, [12], 1)
        self.assertRaises(TypeError, Rhomb, True, False)
        self.assertRaises(TypeError, Rhomb, {12}, {'five'})


class Test_Triangle(unittest.TestCase):

    def test_area(self):
        self.assertEqual(round(Triangle(2, 2, 3).area(), 2),  round(1.984313483298443, 2))
        self.assertEqual(round(Triangle(1, 1, 1).area(), 2), round(0.4330127018922193, 2))
        self.assertEqual(Triangle(0, 0, 0).area(), 0)
        self.assertEqual(round(Triangle(2.5, 3.5, 4).area(), 2), round(4.330127018922194, 2))

    def test_perimeter(self):
        self.assertEqual(Triangle(2, 2, 3).perimeter(), 7)
        self.assertEqual(Triangle(1, 1, 1).perimeter(), 3)
        self.assertEqual(Triangle(0, 0, 0).perimeter(), 0)
        self.assertEqual(Triangle(2.5, 3.5, 4).perimeter(), 10)

    def test_high(self):
        self.assertEqual(round(Triangle(2, 2, 3).high(1), 2), round(1.98, 2))
        self.assertEqual(round(Triangle(1, 1, 1).high(1), 2), round(0.87, 2))
        self.assertEqual(Square(0).diagonal(), 0)
        self.assertEqual(round(Triangle(2.5, 3.5, 4).high(1), 2), round(3.46, 2))

    def test_values(self):
        self.assertRaises(ValueError, Triangle, -1, -2, 2)
        self.assertRaises(ValueError, Triangle, 10, 3, -5)

    def test_type(self):
        self.assertRaises(TypeError, Triangle, '21', '21', '21')
        self.assertRaises(TypeError, Triangle, [12], '21', '21')
        self.assertRaises(TypeError, Triangle, True, False, 2)
        self.assertRaises(TypeError, Triangle, {12}, '21', '21')


class Test_Trapezoid(unittest.TestCase):

    def test_area(self):
        self.assertEqual(round(Trapezoid(4, 2, 2, 2).area(), 2), round(5.1962, 2))
        self.assertEqual(round(Trapezoid(2, 1, 1, 1).area(), 2), round(1.299, 2))
        self.assertEqual(round(Trapezoid(2.5, 1.5, 1, 1.3).area(), 2), round(1.9758, 2))

    def test_perimeter(self):
        self.assertEqual(Trapezoid(4, 2, 2, 2).perimeter(), 10)
        self.assertEqual(Trapezoid(2, 1, 1, 1).perimeter(), 5)
        self.assertEqual(Trapezoid(0, 0, 0, 0).perimeter(), 0)
        self.assertEqual(Trapezoid(2.5, 1.5, 1, 1.3).perimeter(), 6.3)

    def test_values(self):
        self.assertRaises(ValueError, Trapezoid, -5, -2, 5, 4)
        self.assertRaises(ValueError, Trapezoid, 10, 5, 5, -4)


    def test_type(self):
        self.assertRaises(TypeError, Trapezoid, '21', '21', '21', '21')
        self.assertRaises(TypeError, Trapezoid, [12], [123], ['five'], 2)
        self.assertRaises(TypeError, Trapezoid, 4, False, 4, True)
        self.assertRaises(TypeError, Trapezoid, {12}, False, ['five'], 2)
