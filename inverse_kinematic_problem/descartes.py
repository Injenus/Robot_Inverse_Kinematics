#   двумерный робот декарт
#   q1=x
#   q2=y
while True:
    try:
        x,y=map(float, input('\nВведите координаты x, y через пробел: ').split(' '))
        print('q1 = {}\nq2 = {}'.format(x, y))
        break
    except ValueError:
        print('Неверный формат данных.')
