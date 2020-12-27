# /bin/env python
# -*- encode: utf-8 -*-
import re

__author__ = '@britodfbr'


def increment_string(s: str):
    regex = r'(\w+)(\d+)'
    matches = re.compile(regex).search(s)
    if matches:
        print(matches.groups())
    base = matches.group(0) if matches else ""
    number = matches.group(1) if matches else "0"
    digits = len(number)
    print(base, number, digits)
    strout = '{}{:0>%d}' % digits
    num = int(number) + 1
    result = strout.format(base, num)
    print(result)
    # return result
