''' This is a simple calculator '''

from decimal import Decimal

from arithm import mult_div, add_subtr


while True:

    sign = ('+', '-', '*', '/')
    s = ''

    try:
        s0 = input('-> ')
    except:
        print()
        break

    if not s0 or str.isspace(s0):
        continue
    elif '\t' in s0:
        print('Tabulation is not supported')
        continue

    error = False
    for i in range(len(s0)):
        if i < len(s0) - 1 and s0[i] == ' ' and s0[i + 1] == ' ':
            error = True
            break
        if (str.isdigit(s0[i]) or s0[i] == '.') and i < len(s0) - 2:
            if (s0[i + 1] == ' ' and
               (str.isdigit(s0[i + 2]) or s0[i + 2] == '.')):
                error = True
                break
    if error:
        print('Incorrect expression')
        continue

    s0 = s0.replace(' ', '')

    if s0[0] in sign[2:] or s0[-1] in sign:
        print('Incorrect expression')
        continue
    elif s0[0] in sign[:2]:
        if len(s0) > 1 and s0[1] in sign:
            print('Incorrect expression')
            continue

    signs_count = 0
    digits = error = False
    for x in s0:
        if str.isdigit(x):
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

    buf1 = ''
    for i in range(len(s)):
        if s[i] == '+' or s[i] == '*' or s[i] == '/':
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

    buf2 = ''
    for i in range(len(s)):
        if str.isdigit(s[i]) or s[i] == '.':
            buf2 += ' '
        elif s[i] == '-' and s[i -1] in sign:
            buf2 += ' '
        else:
            buf2 += s[i]

    if s[0] in sign:
        buf2 = buf2[1:]

    buf2 = buf2.split()

    I = iter(buf1)
    for i in range(0, (len(buf1) + (len(buf2))), 2):
        buf2.insert(i, next(I))

    if '*' in buf2 or '/' in buf2:
        buf2 = mult_div(buf2)
        if buf2 == False:
            continue

    if '+' in buf2 or '-' in buf2:
        buf2 = add_subtr(buf2)

    buf2 = buf2[0]

    print(buf2)
    continue

