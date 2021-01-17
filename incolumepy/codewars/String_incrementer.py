# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import re


def increment_string(s: str):
    if not s:
        return "1"
    elif s.isdigit():
        return f"{int(s) + 1}"
    regex = r'(.+)(\d+)$'
    matches = re.compile(regex).search(s)
    print(f'1.. {s}:{matches.groups()}, {matches.group(0)}, {matches.group(1)}, {matches.group(2)}')
    base = matches.group(1) or ""
    number = matches.group(2) or '0'
    digits = len(number)
    print(f'2.. {s}: {base}, {matches.groups()}, {number}, {digits}')
    strout = '{}{:0>%d}' % digits
    num = int(number) + 1
    result = strout.format(base, num)
    print(f'3.. {result}')
    return result


if __name__ == '__main__':
    print(increment_string('asdfg01'))
    print(increment_string('g.~0123456789'))
