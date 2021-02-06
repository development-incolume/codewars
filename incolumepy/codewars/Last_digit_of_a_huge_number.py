#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = '@britodfbr'


def last_digit(lst: list) -> int:
    if not lst:
        return 1
    return lst.pop(0) ** last_digit(lst)


if __name__ == '__main__':
    print(last_digit([2, 2, 2]))
