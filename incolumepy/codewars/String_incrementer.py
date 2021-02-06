# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import re


def increment_string(s: str):
    if not s:
        return "1"
    elif s.isdigit():
        digits = len(s)
        strout = '{:0>%d}' % digits
        return strout.format(f"{int(s) + 1}")
    regex = r'(.+[^\d])(\d+)?$'
    matches = re.compile(regex).search(s)
    print(f'1.. {s}:{matches}')
    base = matches.group(1) or ''
    number = matches.group(2) or '0'
    digits = len(number)
    print(f'2.. {s}: {base}, {matches}, {number}, {digits}')
    strout = '{}{:0>%d}' % digits
    num = int(number) + 1
    result = strout.format(base, num)
    print(f'3.. {result}')
    return result


if __name__ == '__main__':
    print(increment_string('asdfg01'))
    print(increment_string('g.~0123456789'))
