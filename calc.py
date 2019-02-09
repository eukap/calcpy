"""
calc.py is a simple text-based calculator.

Supported operations:
  - addition ('+')
  - subtraction ('-')
  - multiplication ('*')
  - division ('/')
  - raising to a power ('^')

The tabulation key, parentheses and more than 1 space in a row
between symbols are not supported.
"""

from decimal import Decimal

from arithm import power, mult_div, add_subtr


print('**Press <Ctrl+C> to exit**', end='\n\n')

while True:

    sign = ('+', '-', '*', '/', '^')
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

    s0 = s0.strip()

    if '\t' in s0:
        print('Tabulation is not supported')
        continue

    s0 = s0.replace(',', '.')

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

    # Process mathematical signs at the begining and end of the string 
    if s0[0] in sign[2:] or s0[-1] in sign:
        print('Incorrect expression')
        continue
    elif s0[0] in sign[:2]:
        if len(s0) > 1 and s0[1] in sign:
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
        elif x == '.':
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

    # Create the 1st list of strings with numbers only
    buf1 = ''
    for i in range(len(s)):
        if s[i] == '+' or s[i] in sign[2:]:
            buf1 += ' '
        elif s[i] == '-' and s[i - 1] not in sign:
                buf1 += ' '
        else:
            buf1 += s[i]

    if buf1[0] == ' ':
        buf1 = s[0] + buf1[1:]

    buf1 = buf1.split()

    try:
        for x in buf1:
            Decimal(x)
    except:
        print('Incorrect expression')
        continue

    # Create the 2nd list of strings with signs only
    buf2 = ''
    for i in range(len(s)):
        if s[i].isdigit() or s[i] == '.':
            buf2 += ' '
        elif s[i] == '-' and s[i -1] in sign:
            buf2 += ' '
        else:
            buf2 += s[i]

    if s[0] in sign:
        buf2 = buf2[1:]

    buf2 = buf2.split()

    # Combine the lists according to the original string 
    I = iter(buf1)
    for i in range(0, (len(buf1) + (len(buf2))), 2):
        buf2.insert(i, next(I))

    buf = buf2

    if '^' in buf:
        buf = power(buf)
        if buf is None:
            continue

    if '*' in buf or '/' in buf:
        buf = mult_div(buf)
        if buf is None:
            continue

    if '+' in buf or '-' in buf:
        buf = add_subtr(buf)

    result = (str(buf[0])).rstrip('.0')

    print(result)
    continue
