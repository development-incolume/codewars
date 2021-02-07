# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
from functools import lru_cache
import time


@lru_cache(maxsize=64)
def fib(n):
    # 1, 1, 2, 3, 5, ..
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)


@lru_cache(64)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def productFib(prod):
    mult = 0
    v = 0
    while mult < prod:
        mult = fibonacci(v) * fibonacci(v+1)
        if mult == prod:
            return [fibonacci(v), fibonacci(v+1), True]
        v += 1
    else:
        return [fibonacci(v-1), fibonacci(v), False]
