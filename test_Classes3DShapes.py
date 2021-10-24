from Classes3DShapes import Sphere, Cone, Cylinder, Tetrahedron, Parallelepiped, Cube
import unittest
from math import pi


class Test_Cube(unittest.TestCase):
    """ Юнит тесты для класс квадрат """
    def test_area(self):
        """ Проверка вычисления площади """
        self.assertEqual(Cube(2).area(), 24)
        self.assertEqual(Cube(1).area(), 6)
        self.assertEqual(Cube(0).area(), 0)
        self.assertEqual(Cube(2.5).area(), 37.5)

    def test_radius_into_sphere(self):
        """ Проверка вычисления периметра """
        self.assertEqual(round(Cube(2).radius_into_sphere(), 2), round(1, 2))
        self.assertEqual(round(Cube(1).radius_into_sphere(), 2), round(0.5, 2))
        self.assertEqual(Cube(0).radius_into_sphere(), 0)
        self.assertEqual(round(Cube(2.5).radius_into_sphere(), 2), round(1.25, 2))

    def test_values(self):
        """ Проверка значений """
        self.assertRaises(ValueError, Cube, -1)
        self.assertRaises(ValueError, Cube, -10)

    def test_type(self):
        """ Проверка типов значений """
        self.assertRaises(TypeError, Cube, '21')
        self.assertRaises(TypeError, Cube, [12])
        self.assertRaises(TypeError, Cube, True)
        self.assertRaises(TypeError, Cube, {12})


class Test_Parallelepiped(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Parallelepiped(2, 1, 2).area(), 16)
        self.assertEqual(Parallelepiped(1, 1, 1).area(), 6)
        self.assertEqual(Parallelepiped(0, 0, 0).area(), 0)
        self.assertEqual(Parallelepiped(2.5, 3.5, 5.5).area(), 83.5)

    def test_diagonal(self):
        self.assertEqual(round(Parallelepiped(2, 1, 2).diagonal(), 2), round(3, 2))
        self.assertEqual(round(Parallelepiped(1, 1, 1).diagonal(), 2), round(1.7320508075688772, 2))
        self.assertEqual(Parallelepiped(0, 0, 0).diagonal(), 0)
        self.assertEqual(round(Parallelepiped(2.5, 3.5, 5.5).diagonal(), 2), round(6.98212002188447, 2))

    def test_values(self):
        self.assertRaises(ValueError, Parallelepiped, -1, -2, 0)
        self.assertRaises(ValueError, Parallelepiped, 10, -3, 2)

    def test_type(self):
        self.assertRaises(TypeError, Parallelepiped, '21', '12', '21')
        self.assertRaises(TypeError, Parallelepiped, [12], [12], '21')
        self.assertRaises(TypeError, Parallelepiped, True, True, 2)
        self.assertRaises(TypeError, Parallelepiped, {12}, {'we'}, 12)


class Test_Sphere(unittest.TestCase):

    def test_area(self):
        self.assertEqual(Sphere(2).area(), 4 * pi * 2 ** 2)
        self.assertEqual(Sphere(1).area(), 4 * pi)
        self.assertEqual(Sphere(0).area(), 0)
        self.assertEqual(Sphere(2.5).area(), 4 * pi * 2.5 ** 2)

    def test_perimeter(self):
        self.assertEqual(round(Sphere(2).volume(), 2), round(33.510321638291124, 2))
        self.assertEqual(round(Sphere(1).volume(), 2), round(4.1887902047863905, 2))
        self.assertEqual(Sphere(0).volume(), 0)
        self.assertEqual(round(Sphere(2.5).volume(), 2), round(65.44984694978736, 2))

    def test_values(self):
        self.assertRaises(ValueError, Sphere, -1)
        self.assertRaises(ValueError, Sphere, -10)

    def test_type(self):
        self.assertRaises(TypeError, Sphere, '21')
        self.assertRaises(TypeError, Sphere, [12])
        self.assertRaises(TypeError, Sphere, True)
        self.assertRaises(TypeError, Sphere, {12})


class Test_Cylinder(unittest.TestCase):

    def test_area(self):
        self.assertEqual(round(Cylinder(2, 3).area(), 2), round(94.24777960769379, 2))
        self.assertEqual(round(Cylinder(1, 1).area(), 2), round(12.566370614359172, 2))
        self.assertEqual(Cylinder(0, 0).area(), 0)
        self.assertEqual(round(Cylinder(2.5, 3.5).area(), 2), round(131.94689145077132, 2))

    def test_area_foot(self):
        self.assertEqual(round(Cylinder(2, 3).area_foot(), 2), round(pi * 3 ** 2, 2))
        self.assertEqual(round(Cylinder(1, 1).area_foot(), 2), round(pi, 2))
        self.assertEqual(round(Cylinder(0, 0).area_foot(), 2), 0)
        self.assertEqual(round(Cylinder(2.5, 3.5).area_foot(), 2), round(3.5 ** 2 * pi, 2))

    def test_values(self):
        self.assertRaises(ValueError, Cylinder, -1, -2)
        self.assertRaises(ValueError, Cylinder, -10, -3)

    def test_type(self):
        self.assertRaises(TypeError, Cylinder, '21', 'five')
        self.assertRaises(TypeError, Cylinder, [12], 1)
        self.assertRaises(TypeError, Cylinder, True, False)
        self.assertRaises(TypeError, Cylinder, {12}, {'five'})


class Test_Cone(unittest.TestCase):

    def test_area(self):
        self.assertEqual(round(Cone(2, 2, 3).area(), 2),  round(31.41592652589793, 2))
        self.assertEqual(round(Cone(1, 1, 1).area(), 2), round(6.283185305179586, 2))
        self.assertEqual(Cone(0, 0, 0).area(), 0)
        self.assertEqual(round(Cone(2.5, 3.5, 4).area(), 2), round(82.46680713048207, 2))

    def test_volume(self):
        self.assertEqual(round(Cone(2, 2, 3).volume(), 2), round(8.377580409572781, 2))
        self.assertEqual(round(Cone(1, 1, 1).volume(), 2), round(1.0471975511965976, 2))
        self.assertEqual(Cone(0, 0, 0).volume(), 0)
        self.assertEqual(round(Cone(2.5, 3.5, 4).volume(), 2), round(32.070425005395805, 2))

    def test_values(self):
        self.assertRaises(ValueError, Cone, -1, -2, 2)
        self.assertRaises(ValueError, Cone, 10, 3, -5)

    def test_type(self):
        self.assertRaises(TypeError, Cone, '21', '21', '21')
        self.assertRaises(TypeError, Cone, [12], '21', '21')
        self.assertRaises(TypeError, Cone, True, False, 2)
        self.assertRaises(TypeError, Cone, {12}, '21', '21')


class Test_Tetrahedron(unittest.TestCase):

    def test_area(self):
        self.assertEqual(round(Tetrahedron(2).area(), 2), round(6.928203230275509, 2))
        self.assertEqual(round(Tetrahedron(1).area(), 2), round(1.7320508075688772, 2))
        self.assertEqual(Tetrahedron(0).area(), 0)
        self.assertEqual(round(Tetrahedron(2.5).area(), 2), round(10.825317547305483, 2))

    def test_height(self):
        self.assertEqual(round(Tetrahedron(2).height(), 2), round(1.63, 2))
        self.assertEqual(round(Tetrahedron(1).height(), 2), round(0.82, 2))
        self.assertEqual(Tetrahedron(0).height(), 0)
        self.assertEqual(round(Tetrahedron(2.5).height(), 2), round(2.04, 2))

    def test_values(self):
        self.assertRaises(ValueError, Tetrahedron, -1)
        self.assertRaises(ValueError, Tetrahedron, -10)

    def test_type(self):
        self.assertRaises(TypeError, Tetrahedron, '21')
        self.assertRaises(TypeError, Tetrahedron, [12])
        self.assertRaises(TypeError, Tetrahedron, True)
        self.assertRaises(TypeError, Tetrahedron, {12})

