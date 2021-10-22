from Classes2DShapes import Square, Rectangle, Circle, Triangle, Trapezoid, Rhomb, Shape
from Classes3DShapes import Sphere, Cone, Cylinder, Tetrahedron, Parallelepiped, Cube


def main_menu() -> None:
    """ Вывод главного меню """
    print('1: Плоские фигуры\n'
          '2: Объемные фигуры\n'
          '3: Выход\n'
          f'Общее количество просмотренных фигур {Shape.count_shapes()}')


def next_menu(shapes: list) -> None:
    """ Вывод меню с фигурами """
    print('Выберите фигуру:')
    for i in shapes:
        print(i)


def check_value(values: list) -> bool:
    """ Проверка введеный пользователем значений. Вернет:
        True - если значений больше нуля
        False - если есть значения меньше нуля или равны ему"""
    for value in values:
        if value <= 0:
            return False
    return True


def print_info(shape: Shape) -> None:
    shape.show_info()


def create_2d_shape(index: str) -> None:
    """ Калькулятор плоских фигур """
    if index == '1':
        """Circle"""
        while True:
            radius = float(input('Введите значение радиуса окружности: '))
            if not check_value([radius]):
                continue
            print_info(Circle(radius))
            break
    elif index == '2':
        """Rectangle"""
        while True:
            length = float(input('Введите значение длины прямоугльника: '))
            width = float(input('Введите значение ширины прямоугльника: '))
            if not check_value([width, length]):
                continue
            print_info(Rectangle(width, length))
            break
    elif index == '3':
        """Triangle"""
        while True:
            side1 = float(input('Введите значение первой стороны треугольника: '))
            side2 = float(input('Введите значение второй стороны треугольника: '))
            side3 = float(input('Введите значение трертьей стороны треугольника: '))
            if not check_value([side1, side2, side3]):
                continue
            if (side1 + side2 > side3) or (side1 + side3 > side2) or (side2 + side3 > side1):
                print("Неверный значения сторон треугольника!")
                continue
            print_info(Triangle(side1, side2, side3))
            break
    elif index == '4':
        """Square"""
        while True:
            side = float(input('Введите значение длины стороны квадрата: '))
            if not check_value([side]):
                continue
            print_info(Square(side))
            break
    elif index == '5':
        """Trapezoid"""
        while True:
            big_foot = float(input('Введите значение большогое основания трапеции: '))
            small_foot = float(input('Введите значение маленького основания трапеции: '))
            side1 = float(input('Введите значение левой сторонй трапеции: '))
            side2 = float(input('Введите значение правой стороны трапеции: '))
            if not check_value([big_foot, small_foot, side2, side1]):
                continue
            print_info(Trapezoid(big_foot, small_foot, side1, side2))
            break
    elif index == '6':
        """Rhomb"""
        while True:
            diagonal1 = float(input('Введите значение первой диагонали ромба: '))
            diagonal2 = float(input('Введите значение второй диагонали ромба: '))
            if not check_value([diagonal1, diagonal2]):
                continue
            print_info(Rhomb(diagonal1, diagonal2))
            break
    else:
        print('Такой фигуры нет')


def create_3d_shape(index: str) -> None:
    """ Калькулятор объемных фигур """
    if index == '1':
        """Sphere"""
        while True:
            radius = float(input('Введите значение радиуса сферы: '))
            if not check_value([radius]):
                continue
            print_info(Sphere(radius))
            break
    elif index == '2':
        """Parallelepiped"""
        while True:
            length = float(input('Введите значение длины параллелепипеда: '))
            width = float(input('Введите значение ширины параллелепипеда: '))
            height = float(input('Введите значение высоты параллелепипеда: '))
            if not check_value([width, length, height]):
                continue
            print_info(Parallelepiped(height, length, width))
            break
    elif index == '3':
        """Tetrahedron"""
        while True:
            side1 = float(input('Введите значение ребра тетраэдра: '))
            if not check_value([side1]):
                continue
            print_info(Tetrahedron(side1))
            break
    elif index == '4':
        """Cube"""
        while True:
            side = float(input('Введите значение длины ребра куба: '))
            if not check_value([side]):
                continue
            print_info(Cube(side))
            break
    elif index == '5':
        """Cylinder"""
        while True:
            height = float(input('Введите значение высоты цилиндра: '))
            radius = float(input('Введите значение радиуса цилиндра: '))
            if not check_value([height, radius]):
                continue
            print_info(Cylinder(height, radius))
            break
    elif index == '6':
        """Cone"""
        while True:
            height = float(input('Введите значение высоты конуса: '))
            radius = float(input('Введите значение радиуса основания: '))
            forming = float(input('Введите значение образующей конуса: '))
            if not check_value([forming, height, radius]):
                continue
            print_info(Cone(height, radius, forming))
            break
    else:
        print('Такой фигуры нет')


def main():
    _2D_SHAPES = ['1: Круг', '2: Прямоугольник', '3: Треугольник', '4: Квадрат', '5: Трапеция', '6: Ромб']
    _3D_SHAPES = ['1: Сфера', '2: Параллелепипед', '3: Тетраэдр', '4: Куб', '5: Цилиндр', '6: Конус']

    while True:
        main_menu()
        answer_user = input()

        if answer_user == '1':
            next_menu(_2D_SHAPES)
            answer_user = input()
            create_2d_shape(answer_user)
            continue
        elif answer_user == '2':
            next_menu(_3D_SHAPES)
            answer_user = input()
            create_3d_shape(answer_user)
            continue
        else:
            print('Пока!')
            exit()


if __name__ == "__main__":
    main()
