# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import re


def increment_string(s: str):
    regex = r'([a-z\W]+)(\d+)'
    matches = re.compile(regex).search(s)

    print(f'{s}:{matches.groups()}, {matches.group(0)}, {matches.group(1)}, {matches.group(2)}')
    base = matches.group(1)
    number = matches.group(2)
    digits = len(number)
    print(f'{s}: {base}, {matches.groups()}, {number}, {digits}')
    strout = '{}{:0>%d}' % digits
    num = int(number) + 1
    result = strout.format(base, num)
    print(result)
    return result


if __name__ == '__main__':
    print(increment_string('asdfg01'))
    print(increment_string('g.~1234567890'))
