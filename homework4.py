# 1. Напишите функцию для транспонирования матрицы


def transpose_matrix(matrix):
    transposed_matrix = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


initial_matrix = [[1, 2, 3, 4],[10, 20, 30, 40],[100, 200, 300, 400]]
print(f'{initial_matrix=     }')
print(f'transposed_matrix = {transpose_matrix(initial_matrix)}')


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение переданного аргумента, 
# а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.


def fruits(**kwargs):
    return {value if value.__hash__ is not None else str(value):key for key, value in kwargs.items()}

print(fruits(bananas = 23, apples = (234, 345), peaches = [234, 3456, 567]))


# 3. Возьмите задачу о банкомате из семинара 2. 
# ..Напишите программу банкомат.
# ..Начальная сумма равна нулю
# ..Допустимые действия: пополнить, снять, выйти
# ..Сумма пополнения и снятия кратны 50 у.е.
# ..Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ..После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ..Нельзя снять больше, чем на счёте
# ..При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ..Любое действие выводит сумму денег
# Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_LIST_OPERATIONS = 'о'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0
list_operations = []

def rich_tax(acc, r_tax):
    p_cent = acc * r_tax
    return p_cent

def w_tax(amnt, w_p_cent):
    w_tax_size = amnt * w_p_cent
    w_tax_size = (MIN_REMOVAL if w_tax_size < MIN_REMOVAL else
                  MAX_REMOVAL if w_tax_size > MAX_REMOVAL else w_tax_size)
    return w_tax_size


while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", Снять - "{CMD_WITHDRAW}", Список операций - "{CMD_LIST_OPERATIONS}", Выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        print(f'Возьмите карту, на которой {account} у.е.')
        break
    if command == CMD_LIST_OPERATIONS:
        print(f'Список пополнений и снятий: {list_operations}')
    if account > RICHNESS_SUM:
        rtax = rich_tax(account, RICHNESS_TAX)
        print(f'Удержан налог на богатство {RICHNESS_TAX*100}% в размере {rtax} у.е.\n'
              f'Итого на карте осталось {account-rtax} у.е.')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % 50 != 0:
            amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    if command == CMD_DEPOSIT:
        account += amount
        count += 1
        list_operations.append([str(+amount)])
        print(f'Пополнение карты на {amount} у.е. \n Итого на карте {account} у.е.')
    elif command == CMD_WITHDRAW:
        wtax = w_tax(amount, WITHDRAW_PERCENT)
        if account >= amount + wtax:
            count += 1
            account -= (amount + wtax)
            list_operations.append([str(-amount)])
            print(f'Снятие с карты {amount} у.е. \n Комиссия за снятие {wtax} у.е. \n'
                  f'На карте осталось {account} у.е.')
        else:
            print(f'Недостатоно денег для выполнения операции \n'
                  f'Затребованная сумма {amount} у.е., комиссия составила {wtax} у.е. \n'
                  f'На карте {account} у.е.')
        if count and count % COUNT_OPER == 0:
            bonus_percent = account * ADD_PERCENT
            account += bonus_percent
            print(f'На счет начислено {ADD_PERCENT*100}%, составляющие {bonus_percent} у.е. \n'
                  f'Итого на карте {account} у.е.')
