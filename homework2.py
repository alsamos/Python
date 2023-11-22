# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

HEX = 16

num = int(input(f'Введите целое число: '))
hex_num = hex(num)
print(f'Проверка функцией: в шестнадцатиричной системе должно получиться {hex_num=}')
hex_number: str = ''
while num > 0:
    hex_number = str(num % HEX) + hex_number
    num = num//HEX
print(f'В результате вычислений получилось число в шестнадцатиричной системе {hex_number=}')    

      


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна 
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions

import math
import fractions

frctn1 = input(f'Введите первую дробь вида a/b: ')
frctn2 = input(f'Введите вторую дробь вида c/d: ')
print()

a, b = frctn1.split('/')
c, d = frctn2.split('/')

ac = int(a) * int(c)
bd = int(b) * int(d)
nod = math.gcd(ac, bd)
if nod > 1: 
    ac = ac // nod
    bd = bd // nod
print(f'Результат вычисления произведения дробей: {a}/{b}*{c}/{d}={ac}/{bd}')

ad_bc = int(a) * int(d) + int (b) * int (c)
bd = int(b) * int(d)
nod = math.gcd(ad_bc, bd)
if nod > 1: 
    ad_bc = ad_bc // nod 
    bd = bd // nod
print(f'Результат вычисления суммы дробей: {a}/{b}+{c}/{d}={ad_bc}/{bd}')
print()

f1 = fractions.Fraction(int(a), int(b))
f2 = fractions.Fraction(int(c), int(d))
print(f'Результат проверки умножения дробей функцией: {f1 * f2}')
print(f'Результат проверки сложения дробей функцией: {f1 + f2}')

