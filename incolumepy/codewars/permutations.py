# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import itertools


def permutations(string: str) -> list:
    # return itertools.combinations(string, len(string))
    return set([''.join(x) for x in itertools.permutations(string)])


def run():
    print(permutations('ab'))


if __name__ == '__main__':
    run()
