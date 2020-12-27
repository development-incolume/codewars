# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'


def increment_string(s: str):
    base = ''.join(x for x in s if x.isalpha())
    number = ''.join(x for x in s if x.isdigit()) or 0
    digits = len(''.join(x for x in s if x.isdigit()))
    strout = '{}{:0>%d}' % digits
    num = int(number) + 1
    result = '{}{}'.format(base, num)
    # result = f'{base}{num:0>%d}' % digits     # Fail
    result = strout.format(base, num)

    print(f'''entrada: {base}, {number}, {digits}''')
    print(f'''saída: {base}, {num}''')
    return result
