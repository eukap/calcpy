"""
arithm.py defines the arithmetic functions that take a list with
string elements of decimal numbers and operation signs and return
a new list as a result after some processing.
"""

from decimal import Decimal, InvalidOperation, Overflow


def power(lst):
    """
    Execute all raising to a power operations
    available in the list
    """
    i = -1
    while i < len(lst) - 1:
        i += 1
        if lst[i] == '^':
            try:
                result = Decimal(lst[i - 1]) ** Decimal(lst[i + 1])
            except InvalidOperation:
                print('Error: unexpected value')
                return
            except Overflow:
                print('Error: overflow')
                return
            del lst[i - 1:i + 2]
            lst.insert(i - 1, result)
            i -= 1
    return lst


def mult_div(lst):
    """
    Execute all multiplication and division operations
    available in the list
    """
    i = -1
    while i < len(lst) - 1:
        i += 1
        try:
            if lst[i] == '*':
                result = Decimal(lst[i - 1]) * Decimal(lst[i + 1])
                del lst[i - 1:i + 2]
                lst.insert(i - 1, result)
                i -= 1
            elif lst[i] == '/':
                try:
                    result = Decimal(lst[i - 1]) / Decimal(lst[i + 1])
                except ZeroDivisionError:
                    print('Error: division by zero')
                    return
                del lst[i - 1:i + 2]
                lst.insert(i - 1, result)
                i -= 1
        except Overflow:
            print('Error: overflow')
            return
    return lst


def add_subtr(lst):
    """
    Execute all addition and subtraction operations
    available in the list
    """
    i = -1
    while i < len(lst) - 1:
        i += 1
        try:
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
        except Overflow:
            print('Error: overflow')
            return
    return lst
