# Решение ОЗК для любого двухзвенного робота.
# Создано для работы с ПО "Моделирование роботов"

import math

DECIMAL_PLACES = 2  # Количество знаков после запятой в выходных данных.
DEFAULT_MODE = False  # Режим работы, True - с координатами по умолчанию.
# Задаём координаты по умолчанию, их количество и смещение для них.
DEFAULT_COORD = ((0.2, 0.4), (0.2, 0.6), (0.4, 0.8), (0.6, 0.8),
                 (0.8, 0.6), (0.5, 0.5), (0.8, 0.4), (0.6, 0.2),
                 (0.2, 0.4))
num = 9
DELTA = (0, 0)
OFFSET_COORD = [[xy + d for xy, d in zip(DEFAULT_COORD[i], DELTA)] for el, i in
                zip(DEFAULT_COORD, range(len(DEFAULT_COORD)))]
# Задаём кортеж типов роботов и словарь, в котором хранятся поля класса
# Coordinates() по соответствующим типам роботов.
ROBOT_TYPE = ('ДЕКАРТ', 'КОЛЕР', 'ЦИЛИНДР', 'СКАРА')
robot_point = {robot: [] for robot in ROBOT_TYPE}
# Задаём длины (м) линейных звеньев робота цилиндра и колера соответственно.
A_LEN_CYLIN = 0.3
A_LEN_COLOR = 0.9
# Задаём длины (м) первого и второго звена робота скара и определяем
# ориентацию его манипулятора: -1 - левая, 1 - правая.
A1_LEN_SCARA = 0.4
A2_LEN_SCARA = 0.8
ARM = 1


class Coordinates():
    def __init__(self, type, name, x=0.0, y=0.0):
        self.type = type
        self.name = name
        self.x = x
        self.y = y
        self.q1 = None
        self.q2 = None
        self.calculaion_generalized_coordinates()

    def calculaion_generalized_coordinates(self):
        if self.type == ROBOT_TYPE[3]:
            a = math.atan(self.y / self.x)
            r = (self.x ** 2 + self.y ** 2) ** (1 / 2)
            g1 = math.acos(
                (A1_LEN_SCARA ** 2 + r ** 2 - A2_LEN_SCARA ** 2) / (
                        2 * A1_LEN_SCARA * r))
            g2 = math.asin(
                (math.sin(g1) * A1_LEN_SCARA) / (A2_LEN_SCARA))
            self.q1 = (-math.pi) / 2 + a * ARM
            self.q2 = (g1 + g2) * ARM
        elif self.type == ROBOT_TYPE[2]:
            self.q1 = -math.atan(self.x / self.y)
            self.q2 = ((self.y) ** 2 + (self.x) ** 2) ** (1 / 2) - A_LEN_CYLIN
        elif self.type == ROBOT_TYPE[1]:
            self.q1 = self.y - (A_LEN_COLOR ** 2 - self.x ** 2) ** (1 / 2)
            self.q2 = -math.asin(self.x / A_LEN_COLOR)
        elif self.type == ROBOT_TYPE[0]:
            self.q1 = self.x
            self.q2 = self.y
        else:
            self.q1 = None
            self.q2 = None

        self.q1 = self.to_fixed(self.q1, DECIMAL_PLACES)
        self.q2 = self.to_fixed(self.q2, DECIMAL_PLACES)

    def to_fixed(self, value, digits=2):
        return value if value is None else f"{value:.{digits}f}"

    def print_point(self):
        print('{}, {}: x = {}, y = {}'.format(self.type, self.name, self.x,
                                              self.y))

    def print_generalized_coordinates(self):  # вывод обощённых координат точки
        print('{}, {}: q1 = {}, q2 = {}'.format(self.type, self.name, self.q1,
                                                self.q2))

    def print_info(self):
        print('{}, {}: x = {}, y = {}, q1 = {}, q2 = {}'.format(self.type,
                                                                self.name,
                                                                self.x, self.y,
                                                                self.q1,
                                                                self.q2))


if DEFAULT_MODE:
    for robot in ROBOT_TYPE:
        for i in range(1, 1 + len(OFFSET_COORD)):
            name = 'point_' + str(i)
            current_point = Coordinates(robot, name, OFFSET_COORD[i - 1][0],
                                        OFFSET_COORD[i - 1][1])
            robot_point[robot].append(current_point)
else:
    input_text = 'Введите количество точек: '
    while True:
        try:
            num = int(input(input_text))
        except ValueError:
            input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
        else:
            if num < 1:
                input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
            else:
                break

    for i in range(1, num + 1):
        if i != 3:
            input_text = 'Введите координаты ' + str(
                i) + '-ой точки x, y через пробел: '
        else:
            input_text = 'Введите координаты ' + str(
                i) + '-eй точки x, y через пробел: '
        while True:
            try:
                x, y = map(float, input(input_text).split(' '))
            except ValueError:
                if i != 3:
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ой точки x, y через пробел: '
                else:
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ей точки x, y через пробел: '
            else:
                break
        name = 'point_' + str(i)
        for robot in ROBOT_TYPE:
            current_point = Coordinates(robot, name, x, y)
            robot_point[robot].append(current_point)
print('\n', end='')
for robot in ROBOT_TYPE:
    print('\n', end='')
    for i in range(num):
        robot_point[robot][i].print_generalized_coordinates()
