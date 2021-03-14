# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'


def solve(s, ops):
    l = (True if x == 't' else False for x in s)
    print(s, len(s), list(l))
    return l
