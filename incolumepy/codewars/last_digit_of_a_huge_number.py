# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import math


def last_digit(lst: list):
    if not lst:
        return 1
    result = 1
    for i in lst[::-1]:
        # print(i)
        # result = math.pow(i, result)
        result = pow(i, result)
    return result % 10


def run():
    print(last_digit([1, 2, 3]))
    print(last_digit([0, 0, 0]))
    print(last_digit([4, 3, 6]))
    print(last_digit([12, 30, 21]))


if __name__ == '__main__':
    run()
