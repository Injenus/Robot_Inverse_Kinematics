# IKP solution for any two-link robot.
# Designed to work with "Моделирование роботов" software.
import math

# The number of decimal places in the output.
DECIMAL_PLACES = 2
# Operating mode, "True" - default coordinates, "False" - input data.
DEFAULT_MODE = True
# Set default coordinates, number and set offset.
DEFAULT_COORD = ((0.2, 0.4), (0.2, 0.6), (0.4, 0.8), (0.6, 0.8),
                 (0.8, 0.6), (0.5, 0.5), (0.8, 0.4), (0.6, 0.2),
                 (0.2, 0.4))
num = 9
DELTA = (0, 0)
OFFSET_COORD = [[xy + d for xy, d in zip(DEFAULT_COORD[i], DELTA)] for el, i in
                zip(DEFAULT_COORD, range(len(DEFAULT_COORD)))]
# Set tuple of types of robots and dictionary to store variable members
# of class Coordinates() sorted by type of robot.
ROBOT_TYPE = ('ДЕКАРТ', 'КОЛЕР', 'ЦИЛИНДР', 'СКАРА')
robot_point = {robot: [] for robot in ROBOT_TYPE}
# Set lengths (m) of linear links of Cylinder and Color robots respectively.
A_LEN_CYLIN = 0.3
A_LEN_COLOR = 0.9
# Set lengths (m) first and second link of Scara robot and
# spatial orientation of manipulator: -1 - left, 1 - right.
A1_LEN_SCARA = 0.4
A2_LEN_SCARA = 0.8
ARM = 1


# The function of rounding a real number to a specified number of
# decimal places.
def to_fixed(value, digits=2):
    return value if value is None else f"{value:.{digits}f}"


class Coordinates():
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
        self.q1 = to_fixed(self.q1, DECIMAL_PLACES)
        self.q2 = to_fixed(self.q2, DECIMAL_PLACES)

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

        print('{}, {}: q1 = {}, q2 = {}'.format(self.type, self.name, self.q1,
                                                self.q2))

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
# Print generalized coordinates of each point for each type of robot.
print('\n', end='')
for robot in ROBOT_TYPE:
    print('\n', end='')
    for i in range(num):
        robot_point[robot][i].print_generalized_coordinates()
