# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


def split_the_link(link):
    way_filename, extension = link.rsplit('.', maxsplit = 1)
    way, filename = way_filename.rsplit('/', maxsplit = 1)
    result = (way, filename, extension)
    return result


print(split_the_link('https://gbcdn.mrgcdn.ru/uploads/record/296473/attachment/316c697472862075b0277cf4d6b9aff0.mp4'))


# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида “10.25%”. В результате получаем словарь 
# с именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная 
# на процент премии

import decimal


def list_of_bonuses(names: list[str], bets: list[int], rewards: list[str]) -> dict[str, decimal.Decimal]:
    result = {names: bets * decimal.Decimal(rewards[:-1]) / 100 for names, bets, rewards in zip(names, bets, rewards)}     
    return result


n = ['Alex', 'Ben', 'Chris']
b = [20000, 10000, 30000]
r = ['5.5%', '10.25%', '3.14%']
print(list_of_bonuses(n, b, r))


# Создайте функцию генератор чисел Фибоначчи 
# https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8


def fibo(n):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

number = int(input('Сколько чисел Фибоначчи вывести? '))
res = fibo(number)
for _ in range(number):
    print(next(res))
