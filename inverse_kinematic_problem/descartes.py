# Трёхмерный робот декарт, q1=x, q2=y, q3=z.
class Coordinates():
    def __init__(self, name, x=0, y=0,
                 z=0):  # инициализация точки, сразу вычисляем обощённые координаты
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.calculaion_generalized_coordinates()

    def calculaion_generalized_coordinates(
            self):  # вывод обощённых координат для точки
        self.q1 = self.x
        self.q2 = self.y
        self.q3 = self.z

    def print_point(self):  # печатаем координаты точки
        print(
            '{}: x = {}, y = {}, z = {}'.format(self.name, self.x, self.y,
                                                self.z))

    def print_generalized_coordinates(self):  # вывод обощённых координат точки
        print(
            '{}: q1 = {}, q2 = {}, q3 = {}'.format(self.name, self.q1, self.q2,
                                                   self.q3))


num = 0  # количество точек
point = []  # список полей класса Coordinates()
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
            i) + '-ой точки x, y, z через пробел: '
    else:
        input_text = 'Введите координаты ' + str(
            i) + '-eй точки x, y, z через пробел: '
    while True:
        try:
            x, y, z = map(float, input(input_text).split(' '))
        except ValueError:
            if i != 3:  # ради падежа (люблю падежи)
                input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                    i) + '-ой точки x, y, z через пробел: '
            else:
                input_text = 'Неверный формат. Попробуйте ещё раз ввести координаты ' + str(
                    i) + '-ей точки x, y, z через пробел: '

        else:
            break
    name = 'point_' + str(i)
    current_point = Coordinates(name, x, y, z)
    point.append(current_point)

print('\n', end='')
for i in range(num):
    point[i].print_generalized_coordinates()
