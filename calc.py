"""
calc.py is a simple text-based calculator.

Supported operations:
  - addition ('+')
  - subtraction ('-')
  - multiplication ('*')
  - division ('/')
  - raising to a power ('^')

The tabulation and more than 1 space in a row
between symbols are not supported.
"""

from proc import str_to_lst
from comp import computing


print('**Press <Ctrl+C> to exit**', end='\n\n')

while True:

    sign = ('+', '-', '*', '/', '^')
    par = ('(', ')')
    s = ''

    try:
        s0 = input('-> ')
    except KeyboardInterrupt:
        print()
        break
    except EOFError:
        print()
        break

    if not s0 or s0.isspace():
        continue
    elif s0.count('(') != s0.count(')'):
        print('Incorrect expression')
        continue

    s0 = s0.strip()

    if '\t' in s0:
        print('Tabulation is not supported')
        continue

    s0 = s0.replace(',', '.')

    if s0[0] == ')' or s0[-1] == '(':
        print('Incorrect expression')
        continue

    # Process incorrect spaces
    error = False
    for i in range(len(s0)):
        if i < len(s0) - 1 and s0[i].isspace() and s0[i + 1].isspace():
            error = True
            print('More than 1 space in a row between symbols')
            break
        elif (s0[i].isdigit() or s0[i] == '.') and i < len(s0) - 2:
            if (s0[i + 1].isspace() and
               (s0[i + 2].isdigit() or s0[i + 2] == '.')):
                error = True
                print('Incorrect expression')
                break
    if error:
        continue

    s0 = s0.replace(' ', '')

    # Process mathematical signs at the beginning and end of the string
    if s0[0] in sign[2:] or s0[-1] in sign:
        print('Incorrect expression')
        continue
    elif s0[0] in sign[:2]:
        if len(s0) > 1 and s0[1] in sign:
            print('Incorrect expression')
            continue

    # Process incorrect combinations with parentheses
    error = False
    for i in range(len(s0) - 1):
        if ((s0[i] == '(' and s0[i + 1] == ')') or
           (s0[i] == ')' and s0[i + 1] == '(')):
            error = True
            break
        elif s0[i] in sign and s0[i + 1] == ')':
            error = True
            break
        elif (s0[i].isdigit() or s0[i] == '.') and s0[i + 1] == '(':
            error = True
            break
        elif s0[i] == ')' and (s0[i + 1].isdigit() or s0[i + 1] == '.'):
            error = True
            break
    if error:
        print('Incorrect expression')
        continue

    # Process other incorrect symbols
    signs_count = 0
    digits = error = False
    for x in s0:
        if x.isdigit():
            digits = True
            s += x
        elif x in sign:
            signs_count += 1
            s += x
        elif x == '.' or x in par:
            s += x
        else:
            error = True
            break
    if error or not digits:
        print('Incorrect expression')
        continue
    elif signs_count == 0:
        print(s)
        continue
    elif signs_count == 1:
        if s[0] == '-':
            print(s)
            continue
        elif s[0] == '+':
            print(s[1:])
            continue

    # Process math signs inside the string
    error = False
    for i in range(len(s)):
        if s[i] in sign and s[i + 1] in sign:
            if s[i + 1] in sign[2:]:
                error = True
                break
            elif s[i + 2] in sign:
                error = True
                break
    if error:
        print('Incorrect expression')
        continue

    s = s.replace('++', '+')
    s = s.replace('+-', '-')
    s = s.replace('-+', '-')
    s = s.replace('--', '+')
    s = s.replace('*+', '*')
    s = s.replace('/+', '/')
    s = s.replace('^+', '^')

    # Evaluate expressions in parentheses
    error = False
    i = 0
    j = 0
    while i < len(s):
        if s[i] == '(':
            j = i
        elif s[i] == ')':
            buf = str_to_lst(s[j + 1:i])
            if buf is None:
                error = True
                break
            result = computing(buf)
            if result is None:
                error = True
                break
            if i < len(s) - 1:
                s = s[:j] + result + s[i + 1:]
                i = -1
            else:
                s = s[:j] + result
                i = -1
        i += 1
    if error:
        continue

    buf = str_to_lst(s)
    if buf is None:
        continue

    result = computing(buf)
    if result is None:
        continue

    if '.' in result:
        result = result.rstrip('0')

    if result[-1] == '.':
        result = result.rstrip('.')

    print(result)
    continue
