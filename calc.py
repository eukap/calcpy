''' This is a simple calculator '''

import math
import decimal

s1 = ''
s2 = ''
sign = ('+', '-', '*', '/')

s = input()

for i in s:
    if (str.isdigit(i) or i in sign):
        s1 += i
    elif i == ',':
        s1 += '.'
    else:
        print('"' + i + '"', 'is not a digit!')
        break

count = -1
for i in s1:
    count += 1
    if s1[0] in sign[2:len(sign)]:
        print('Incorrect expression!')
        break
    elif s1[0] in sign[0:2]:
        if (s1[1] in sign):
            print('Incorrect expression!')
            break
    elif (s1[-1] in sign or s1[-1] == '.'):
        print('Incorrect expression!')
        break
    elif i in sign:
        if s1[count + 1] in sign[2:len(sign)]:
            print('Incorrect expression!')
            break
        elif s1[count + 1] in sign[0:2]:
            if (s1[count + 2] in sign):
                print('Incorrect expression!')
                break
    elif i == '.':
        if (s1[count + 1] in sign or s1[count + 1] == '.'):
            print('Incorrect expression!')
            break

result = decimal.Decimal(0)
# An operand is a string at first:
op = ''
count = -1
for i in s1:
    count += 1
    if s1[0] == '+':
        if (count + 1 < len(s1)):
            if (str.isdigit(s1[count + 1]) or s1[count + 1] == '.'):
                op += s1[count + 1]
                continue        
        result = result + decimal.Decimal(op)

    if s1[0] == '-':
        if (count + 1 < len(s1)):
            if (str.isdigit(s1[count + 1]) or s1[count + 1] == '.'):
                op += s1[count + 1]
                continue        
        result = result - decimal.Decimal(op)

print(result)

