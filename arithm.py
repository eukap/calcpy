from decimal import Decimal, DivisionByZero


def mult_div(lst):
    i = -1
    while i < len(lst) - 1:
        i += 1
        if lst[i] == '*':
            result = Decimal(lst[i - 1]) * Decimal(lst[i + 1])
            del lst[i - 1:i + 2]
            lst.insert(i - 1, result)
            i -= 1
        elif lst[i] == '/':
            try:
                result = Decimal(lst[i - 1]) / Decimal(lst[i + 1])
            except DivisionByZero:
                print('Division by zero')
                return False
            del lst[i - 1:i + 2]
            lst.insert(i - 1, result)
            i -= 1
    return lst


def add_subtr(lst):
    i = -1
    while i < len(lst) - 1:
        i += 1
        if lst[i] == '+':
            result = Decimal(lst[i - 1]) + Decimal(lst[i + 1])
            del lst[i - 1:i + 2]
            lst.insert(i - 1, result)
            i -= 1
        elif lst[i] == '-':
            result = Decimal(lst[i - 1]) - Decimal(lst[i + 1])
            del lst[i - 1:i + 2]
            lst.insert(i - 1, result)
            i -= 1
    return lst
