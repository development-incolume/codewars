# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

import re


def increment_string(strng):
    if strng:
        base = ''.join([x for x in strng if x.isalpha()])
        try:
            seq = int(''.join([x for x in strng if x.isdigit()]))
        except ValueError:
            seq = 0
        return f'{base}{seq + 1}'
    else:
        return '1'


