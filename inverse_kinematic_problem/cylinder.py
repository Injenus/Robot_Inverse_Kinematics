# Цилиндр, 2 звена
import math

A1_LENGTH = 0.3 # Длина линейного (первого) звена

default_mode = True  # определяем, работаем ли врежиме по умолчанию
default_coordinates = [[0.2, 0.4], [0.2, 0.6], [0.4, 0.8], [0.6, 0.8],
                       [0.8, 0.6], [0.5, 0.5], [0.8, 0.4], [0.6, 0.2],
                       [0.2, 0.4]]
delta_x = 0  # смещение по х для коррекции положения
delta_y = 0  # смещение по у для коррекции положения
for i in range(len(default_coordinates)):
    default_coordinates[i][0] += delta_x
    default_coordinates[i][1] += delta_y

class Coordinates():
    def __init__(self, name, x=0.0, y=0.0,
                 z=0.0):  # инициализация точки, сразу вычисляем обощённые координаты
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.calculaion_generalized_coordinates()

    def calculaion_generalized_coordinates(
            self):  # вывод обощённых координат для точки
        self.q1 = round(-math.atan(self.x / self.y), 3)
        self.q2 = round(((self.y) ** 2 + (self.x) ** 2) ** (1 / 2) - A1_LENGTH,3)
        self.q3 = None

    def print_point(self):  # печатаем координаты точки
        print(
            '{}: x = {}, y = {}, z = {}'.format(self.name, self.x, self.y,
                                                self.z))

    def print_generalized_coordinates(self):  # вывод обощённых координат точки
        print(
            '{}: q1 = {}, q2 = {}, q3 = {}'.format(self.name, self.q1, self.q2,
                                                   self.q3))
point = []  # список полей класса Coordinates()

if not default_mode:
    num = 0  # количество точек
    input_text = 'Введите количество точек: '
    while True:  # требуем ввод натурального числа
        try:
            num = int(input(input_text))
        except ValueError:
            input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
        else:
            if num < 1:
                input_text = 'Вы ввели не натуральное число. Попробуйте снова: '
            else:
                break

    for i in range(1,
                   num + 1):  # заполняем список точек полями класса Coordinates()
        if i != 3:  # ради падежа (люблю падежи)
            input_text = 'Введите координаты ' + str(
                i) + '-ой точки x, y через пробел: '
        else:
            input_text = 'Введите координаты ' + str(
                i) + '-eй точки x, y через пробел: '
        while True:
            try:
                x, y = map(float, input(input_text).split(' '))
            except ValueError:
                if i != 3:  # ради падежа (люблю падежи)
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ой точки x, y через пробел: '
                else:
                    input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ей точки x, y через пробел: '
            else:
                break
        name = 'point_' + str(i)
        current_point = Coordinates(name, x, y)
        point.append(current_point)
else:
    for i in range(1, len(default_coordinates) + 1):
        name = 'point_' + str(i)
        current_point = Coordinates(name, default_coordinates[i - 1][0],
                                    default_coordinates[i - 1][1])
        point.append(current_point)
print('\n', end='')
for i in range(len(default_coordinates)):
    point[i].print_generalized_coordinates()
