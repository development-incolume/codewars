# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

from collections import Counter, OrderedDict


def first_non_repeating_letter(string):
    d = OrderedDict()
    for i in string:
        if i.lower() not in [x.lower() for x in d]:
            d[i] = 1
        else:
            try:
                d[i] += 1
            except KeyError:
                d[i.swapcase()] += 1

    result = [a[0] for a in d.items() if a[1] < 2]
    print(string)
    print(d, result)
    if not result:
        return ''
    return result[0]
