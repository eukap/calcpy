from decimal import Decimal


def str_to_lst(string):
    """Create the list of string items from input string"""

    sign = ('+', '-', '*', '/', '^')

    # Create the 1st list of strings with numbers only
    buf1 = ''
    for i in range(len(string)):
        if string[i] == '+' or string[i] in sign[2:]:
            buf1 += ' '
        elif string[i] == '-' and string[i - 1] not in sign:
            buf1 += ' '
        else:
            buf1 += string[i]
    if buf1[0] == ' ':
        buf1 = string[0] + buf1[1:]

    buf1 = buf1.split()

    try:
        for x in buf1:
            Decimal(x)
    except:
        print('Incorrect expression')
        return

    # Create the 2nd list of strings with signs only
    buf2 = ''
    for i in range(len(string)):
        if string[i].isdigit() or string[i] == '.':
            buf2 += ' '
        elif string[i] == '-' and string[i -1] in sign:
            buf2 += ' '
        else:
            buf2 += string[i]

    if string[0] in sign:
        buf2 = buf2[1:]

    buf2 = buf2.split()

    # Combine the lists according to the input string 
    I = iter(buf1)
    for i in range(0, (len(buf1) + (len(buf2))), 2):
        buf2.insert(i, next(I))

    return buf2
