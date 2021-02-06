#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'
import math


def pow_list(lst: list) -> int:
    if not lst:
        return 1
    return lst.pop(0) ** pow_list(lst)


def pow_lst(lst: list) -> int:
    if not lst:
        return 1
    return pow(lst.pop(0), pow_lst(lst))


def last_digit(lst: list) -> int:
    n = str(pow_lst(lst))
    print(n)
    return int(n[-1])


if __name__ == '__main__':
    # print(pow_list([2, 2]))
    # print(pow_lst([2, 2]))
    print(last_digit([0, 0]))
    print(last_digit([2, 2, 2, 2]))
    print(last_digit([6, 21]))
    print(last_digit([7, 6, 21]))
