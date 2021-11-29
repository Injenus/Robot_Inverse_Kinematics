# IKP solution for any two-link robot.
# Designed to work with "Моделирование роботов" software.
import math
from tkinter import Tk, Canvas

# The number of decimal places in the output.
DECIMAL_PLACES = 2
# Operating mode, "True" - default coordinates, "False" - input data.
DEFAULT_MODE = True
# Set default coordinates, number and set offset.
DEFAULT_COORD = ((0.2, 0.4), (0.2, 0.6), (0.4, 0.8), (0.6, 0.8),
                 (0.8, 0.6), (0.5, 0.5), (0.8, 0.4), (0.6, 0.2),
                 (0.2, 0.4))
num = len(DEFAULT_COORD)
DELTA = (0, 0)
OFFSET_COORD = [[xy + d for xy, d in zip(DEFAULT_COORD[i], DELTA)] for el, i in
                zip(DEFAULT_COORD, range(len(DEFAULT_COORD)))]
scale = 1
for i in range(1, 9):
    OFFSET_COORD[i][0] = OFFSET_COORD[0][0] + scale * (
            OFFSET_COORD[i][0] - OFFSET_COORD[0][0])
    OFFSET_COORD[i][1] = OFFSET_COORD[0][1] + scale * (
            OFFSET_COORD[i][1] - OFFSET_COORD[0][1])
print('\nВы работаете с координатами: ')
for i in range(num):
    print('Point_{}: {}'.format(str(i + 1), tuple(OFFSET_COORD[i])))
# Set tuple of types of robots and dictionary to store variable members
# of class Coordinates() sorted by type of robot.
ROBOT_TYPE = ('ДЕКАРТ', 'КОЛЕР', 'ЦИЛИНДР', 'СКАРА')
robot_point = {robot: [] for robot in ROBOT_TYPE}
# Set lengths (1 = unit line in a rectangular coordinate system) of rotary
# links of Cylinder and Color robots respectively.
A_LEN_CYLIN = 0.3
A_LEN_COLOR = 0.9
# Set lengths (1 = unit line in a rectangular coordinate system) first and
# second link of Scara robot and
# spatial orientation of manipulator: -1 - left, 1 - right.
A1_LEN_SCARA = 0.7
A2_LEN_SCARA = 0.49
ARM = 1


# The function of rounding a real number to a specified number of
# decimal places.
def to_fixed(value, digits=DECIMAL_PLACES):
    return value if value is None else f"{value:.{digits}f}"


class Coordinates:
    """Class Coordinates is used to store and edit point information.

    The main application is the calculation of the generalized coordinates of
    this robot for this point.

    Methods
    -------
    calculation_generalized_coordinates()
        Calculates the general coordinates of the links of this robot
        (of this type of robot) for this point.
    print_cartesian_coordinates()
        Print the point's own coordinates in the rectangular coordinate system.
    print_generalized_coordinates()
        Print generalized coordinates for this point of this robot.
    print_all_data()
        Print all information about the point.
    """

    def __init__(self, type, name, x=0.0, y=0.0):
        """"Initialize data.

        Keyword argument:
        type -- the type of robot - Descrartes (Декарт), Cylinder (Цилиндр),
        Color (Колер), Scara (Скара) - the point belong to
        name -- the ordinal name of the point (point_number) of this robot
        (this robot type)
        x -- X coordinate of rectangular coordinate system  of the point
        y -- Y coordinate of rectangular coordinate system  of the point
        Object variables:
        type -- the type of robot the point belong to
        name -- the ordinal name of the point of this robot (this robot type)
        x -- X coordinate of rectangular coordinate system of the point
        y -- Y coordinate of rectangular coordinate system of the point
        q1 -- the first generalized coordinate of this robot (this robot type)
        q2 -- the second generalized coordinate of this robot (this robot type)
        The function for calculating generalized coordinates is also called
        here.
        """

        self.type = type
        self.name = name
        self.x = x
        self.y = y
        self.q1 = None
        self.q2 = None
        self.calculation_generalized_coordinates()

    def calculation_generalized_coordinates(self):
        """Calculates generalized coordinates of the point depending upon the
        type of robot.
        """

        if self.type == ROBOT_TYPE[3]:
            r = (self.x ** 2 + self.y ** 2) ** (1 / 2)
            alpha = math.atan(self.y / self.x)
            beta = math.acos(
                (A1_LEN_SCARA ** 2 + r ** 2 - A2_LEN_SCARA ** 2) / (
                        2 * A1_LEN_SCARA * r))
            gamma = math.acos(
                (A1_LEN_SCARA ** 2 + A2_LEN_SCARA ** 2 - r ** 2) / (
                        2 * A1_LEN_SCARA * A2_LEN_SCARA))
            self.q1 = -math.pi / 2 + alpha + beta * ARM
            self.q2 = (- math.pi + gamma) * ARM
            self.q1 = str(to_fixed(self.q1)) + ' (' + str(
                to_fixed(math.degrees(self.q1))) + ' deg)'
            self.q2 = str(to_fixed(self.q2)) + ' (' + str(
                to_fixed(math.degrees(self.q2))) + ' deg)'
        elif self.type == ROBOT_TYPE[2]:
            self.q1 = -math.atan(self.x / self.y)
            self.q2 = (self.y ** 2 + self.x ** 2) ** (1 / 2) - A_LEN_CYLIN
            self.q1 = str(to_fixed(self.q1)) + ' (' + str(
                to_fixed(math.degrees(self.q1))) + ' deg)'
            self.q2 = to_fixed(self.q2)
        elif self.type == ROBOT_TYPE[1]:
            self.q1 = self.y - (A_LEN_COLOR ** 2 - self.x ** 2) ** (1 / 2)
            self.q2 = -math.asin(self.x / A_LEN_COLOR)
            self.q1 = to_fixed(self.q1)
            self.q2 = str(to_fixed(self.q2)) + ' (' + str(
                to_fixed(math.degrees(self.q2))) + ' deg)'
        elif self.type == ROBOT_TYPE[0]:
            self.q1 = self.x
            self.q2 = self.y
            self.q1 = to_fixed(self.q1)
            self.q2 = to_fixed(self.q2)
        else:
            self.q1 = None
            self.q2 = None

    def print_cartesian_coordinates(self):
        """Print the point's own coordinates in the rectangular coordinate
        system.

        Print type of the robot the point belong to, ordinal name of the point
        for this robot (this robot type), X coordinate of rectangular
        coordinate system  of the point and Y coordinate of rectangular
        coordinate system  of the point.
        """

        print('{}, {}: x = {}, y = {}'.format(self.type, self.name, self.x,
                                              self.y))

    def print_generalized_coordinates(self):
        """Print generalized coordinates for this point of this robot.

        Print type of the robot the point belong to, ordinal name of the point
        for this robot (this robot type), the first generalized coordinate of
        this robot (this robot type) and the second generalized coordinate of
        this robot (this robot type).
        """

        # print('{}, {}: q1 = {}, q2 = {}'.format(self.type, self.name, self.q1,
        #                                         self.q2))
        print()

    def print_all_data(self):
        """Print all information about the point.

        Print type of the robot the point belong to, ordinal name of the point
        for this robot (this robot type), X coordinate of rectangular
        coordinate system  of the point, Y coordinate of rectangular
        coordinate system  of the point, the first generalized coordinate of
        this robot (this robot type) and the second generalized coordinate of
        this robot (this robot type).
        """

        print('{}, {}: x = {}, y = {}, q1 = {}, q2 = {}'.format(self.type,
                                                                self.name,
                                                                self.x, self.y,
                                                                self.q1,
                                                                self.q2))


class Geometry:
    """An object of the class is a line segment, rectangle, oval or point with
    a non-zero radius, which has start and end coordinates.


    In the case of a line segment, the object has the start coordinates of
    the segment and the end coordinates.
    In the case of a rectangle, the object has the coordinates of
    the upper-left corner and the lower-right corner.
    In the case of an oval, the object has the coordinates of the upper left
    corner of the rectangle in which the oval is inscribed, and
    the lower-right.
    In the case of a point, the object has only initial coordinates,
    the radius is set for all objects initially.

    Methods
    ------
    scaling()
        For line segments only. Extend a segment by a specified number of
        times, relative to its beginning.
    draw()
        Draw an object with the specified outline thickness and color.
    """

    point_radius = 4

    def __init__(self, x_start, y_start, type_name='name', x_end=0.0,
                 y_end=0.0):
        self.x_start = x_start
        self.y_start = y_start
        self.x_end = x_end
        self.y_end = y_end
        self.type_name = type_name
        self.scaling(canvas_scaling_factor)

    def scaling(self, n=1.0):
        """Extend a segment n times relative to its beginning.
        """
        if self.type_name == 'segment':
            self.x_end = self.x_start + n * (self.x_end - self.x_start)
            self.y_end = self.y_start + n * (self.y_end - self.y_start)

    def draw(self, width_line=1, color='black'):
        """Draw an object with the specified thickness and color.
        """

        if self.type_name == 'segment':
            canvas.create_line(
                window_size[0] / origin_offset[0] + self.x_start,
                window_size[1] / origin_offset[1] - self.y_start,
                window_size[0] / origin_offset[0] + self.x_end,
                window_size[1] / origin_offset[1] - self.y_end,
                width=width_line,
                fill=color)
        elif self.type_name == 'point':
            canvas.create_oval(
                window_size[0] / origin_offset[
                    0] + self.x_start - self.point_radius,
                window_size[1] / origin_offset[
                    1] - self.y_start + self.point_radius,
                window_size[0] / origin_offset[
                    0] + self.x_start + self.point_radius,
                window_size[1] / origin_offset[
                    1] - self.y_start - self.point_radius, width=0, fill=color)


# In the case of the default operating mode, objects of the class Coordinates()
# are formed on the basis of the built-in dataset.
# In the case of the mode of operation by input data, you first need to enter
# the number of points until the entered value is a natural number.
# The user then enters the coordinates of each point in a rectangular
# coordinate system until the entered values are valid numbers.
# Finally, based on the entered data, objects of the class Coordinates()
# are formed.
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
                input_text = 'Вы ввели не натуральное число. \
                Попробуйте снова: '
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
                    input_text = 'Неверный формат. \
                    Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ой точки x, y через пробел: '
                else:
                    input_text = 'Неверный формат. \
                    Попробуйте ещё раз ввести координаты ' + str(
                        i) + '-ей точки x, y через пробел: '
            else:
                break
        name = 'point_' + str(i)
        for robot in ROBOT_TYPE:
            current_point = Coordinates(robot, name, x, y)
            robot_point[robot].append(current_point)
# Printing generalized coordinates of each point for each type of robot.
for robot in ROBOT_TYPE:
    print('\n', end='')
    for i in range(num):
        robot_point[robot][i].print_generalized_coordinates()
# Setting the window for drawing. Adjust its size. Drawing coordinate axes and
# a grid.
window = Tk()
window.title('Результат построения роботом Скара')
window_size = (500, 400)
origin_offset = (3, 1.5)
canvas = Canvas(window, width=window_size[0], height=window_size[1],
                bg="white",
                cursor="pencil")
canvas.pack()
canvas_scaling_factor = 200
x_origin = Geometry(-500, 0, 'segment', 500, 0)
x_origin.draw(5, 'gray')
y_origin = Geometry(0, -500, 'segment', 0, 500)
y_origin.draw(5, 'gray')
for i in range(-window_size[1], window_size[1], 4):
    grid_horizontal = Geometry(-window_size[0], i * 10, 'segment',
                               window_size[0], i * 10)
    grid_horizontal.draw(color='gray')
for i in range(-window_size[0], window_size[0], 4):
    grid_vertical = Geometry(i * 10, -window_size[1], 'segment', i * 10,
                             window_size[0])
    grid_vertical.draw(color='gray')
# Drawing the links of the robot and the points of the contour.
graphic = {robot: [[] for i in range(num)] for robot in ROBOT_TYPE}
for i in range(num):
    a1 = Geometry(0, 0, 'segment', (-1) * A1_LEN_SCARA * math.sin(
        float(robot_point['СКАРА'][i].q1.split(' ')[0])),
                  A1_LEN_SCARA * math.cos(
                      float(robot_point['СКАРА'][i].q1.split(' ')[0])))
    graphic['СКАРА'][i].append(a1)
    a1.draw()
    a2 = Geometry(a1.x_end, a1.y_end, 'segment',
                  a1.x_end - A2_LEN_SCARA * math.sin(
                      float(robot_point['СКАРА'][i].q1.split(' ')[0]) + float(
                          robot_point['СКАРА'][i].q2.split(' ')[0])),
                  (a1.y_end + A2_LEN_SCARA * math.cos(
                      float(robot_point['СКАРА'][i].q1.split(' ')[0]) + float(
                          robot_point['СКАРА'][i].q2.split(' ')[0]))))
    graphic['СКАРА'][i].append(a2)
    a2.draw()
    contour_point = Geometry(a2.x_end, a2.y_end, 'point')
    graphic['СКАРА'][i].append(contour_point)
    contour_point.draw(color='red')
# Drawing the connecting lines of a path.
for i in range(1, num):
    line = Geometry(graphic['СКАРА'][i - 1][2].x_start,
                    graphic['СКАРА'][i - 1][2].y_start, 'segment',
                    graphic['СКАРА'][i][2].x_start,
                    graphic['СКАРА'][i][2].y_start)
    line.scaling(1 / canvas_scaling_factor)
    line.draw(3, 'green')

window.mainloop()
