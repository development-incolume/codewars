# /bin/env python
# -*- encode: utf-8 -*-
import re

__author__ = '@britodfbr'


def increment_string(s: str):
    regex = r'(.+)(\d+)'
    matches = re.compile(regex).search(s)
    if matches:
        print(matches.groups())
    # base = matches.group(0)
    # number = matches.group(1) or 0
    # digits = len(number)
    # print(matches.groups(), base, number, digits)
    # strout = '{}{:0>%d}' % digits
    # num = int(number) + 1
    # result = strout.format(base, num)
    # return result
