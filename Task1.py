'''
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет
'''
day = int(input('Введите номер дня недели от 1 до 7: '))
if 1 <= day <= 5:
    print('Это рабочий день')
elif 6 <= day <= 7:
    print('Это выходной день')
else:
    print('В неделе 7 дней, необходимо ввести день от 1 до 7')
