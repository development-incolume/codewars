# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
from functools import lru_cache
import time


def productFib(prod):
    @lru_cache(maxsize=64)
    def fib(n):
        if n < 2:
            return n
        return fib(n-1) + fib(n-2)

    # return fib(6)
    mult = 0
    v = 0
    while mult < prod:
        mult = fib(v) * fib(v+1)
        if mult == prod:
            return [fib(v), fib(v+1), True]
        v += 1
    else:
        return [fib(v-1), fib(v), False]
