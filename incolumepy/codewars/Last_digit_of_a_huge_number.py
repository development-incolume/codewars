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


def last_digit0(lst: list) -> int:
    n = str(pow_lst(lst))
    print(n)
    return int(n[-1])


def ldp0(lst):
    """Last digit pow"""
    if not lst:
        return 1
    return lst.pop(0) ** ldp0(lst)


def last_digit1(lst: list) -> int:
    return ldp0(lst) % 10


def ldp(lst: list) -> int:
    d = {}
    d.update({(1, x): 1 for x in range(1, 5)})
    d.update({(5, x): 5 for x in range(1, 5)})
    d.update({(6, x): 6 for x in range(1, 5)})
    d.update({(10, x): 0 for x in range(1, 5)})
    d.update({(2, 1): 2, (2, 2): 4, (2, 3): 8, (2, 4): 6})
    d.update({(3, 1): 3, (3, 2): 9, (3, 3): 7, (3, 4): 1})
    d.update({(4, 1): 4, (4, 2): 6, (4, 3): 4, (4, 4): 6})
    d.update({(7, 1): 7, (7, 2): 9, (7, 3): 3, (7, 4): 1})
    d.update({(8, 1): 8, (8, 2): 4, (8, 3): 2, (8, 4): 6})
    d.update({(9, 1): 9, (9, 2): 1, (9, 3): 9, (9, 4): 1})
    if not lst:
        return 1
    exp = lst.pop()
    base = lst.pop()
    result = d.get((base % 10, exp % 10)) ** ldp(lst)
    return result


def last_digit(lst: list) -> int:
    return ldp(lst)


if __name__ == '__main__':
    # print(pow_list([2, 2]))
    # print(pow_lst([2, 2]))
    print(last_digit([]))
    print(last_digit([0, 0]))
    # print(last_digit([2, 2, 2, 2]))
    # print(last_digit([6, 21]))
    # print(last_digit([7, 6, 21]))
