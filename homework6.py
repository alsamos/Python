# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import sys
from homework6_1 import *

if __name__ == '__main__':
    print(check_date(sys.argv[1]))

# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий 
# задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били 
# друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих 
# друг друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 
# ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


def eight_queens(x, y, n) -> bool:
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True

if __name__ == '__main__':
    queens = 8
    x_list = []
    y_list = []
    for k in range(queens):
        inp_horiz, inp_vert = [int(s) for s in input(f'Введите координаты по горизонтали и вертикали {k+1}го ферзя через пробел: ').split()]
        x_list.append(inp_horiz)
        y_list.append(inp_vert)
    print(eight_queens(x_list, y_list, queens))


# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной 
# расстановки ферзей в задаче выше. Проверяйте различный случайные варианты и выведите 4 
# успешных расстановки.

import random

LOWER_LIMIT = 1
UPPER_LIMIT = 8
SUCCESS = 4
QUEENS = 8

def rand_coordinates():
    x_list = []
    y_list = []
    for _ in range(QUEENS): 
        x_list.append(random.randint(LOWER_LIMIT, UPPER_LIMIT))
        y_list.append(random.randint(LOWER_LIMIT, UPPER_LIMIT))
    for i in range(SUCCESS):  
        random.shuffle(x_list)
        random.shuffle(y_list)
        while not eight_queens(x_list, y_list, QUEENS):
            random.shuffle(x_list)
            random.shuffle(y_list)
        print(f'Успешная расстановка случайным подбором {i+1}: \n Координаты по горизонтали {x_list} \n Координаты по вертикали {y_list}')

rand_coordinates()

