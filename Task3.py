'''Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).'''

numberOfPlase = int(input('Введите номер плоскости: '))
print('Диапазон возможных координат точек в этой четверти: ', end='')
if numberOfPlase == 1:
    print('x > 0, y > 0')
elif numberOfPlase == 2:
    print('x > 0, y < 0')
elif numberOfPlase == 3:
    print('x < 0, y > 0')
elif numberOfPlase == 4:
    print('x < 0, y < 0')
else:
    print('некорректные данные')
