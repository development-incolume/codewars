#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'


def pow_list(lst: list) -> int:
    if not lst:
        return 1
    return lst.pop(0) ** last_digit(lst)


def last_digit(lst: list) -> int:
    n = str(pow_list(lst))
    return int(n[-1])


if __name__ == '__main__':
    print(last_digit([2, 2, 2, 2]))
    print(last_digit([0, 0]))
    print(pow_list([7, 6, 21]))
