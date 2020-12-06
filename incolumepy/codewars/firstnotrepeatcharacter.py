# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

from collections import Counter, OrderedDict


def first_non_repeating_letter(string):
    d = OrderedDict()
    for i in string:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1

    result = [a[0] for a in d.items() if a[1] < 2]
    # print(string)
    # print(d, result)
    if not result:
        return ''
    return result[0]
