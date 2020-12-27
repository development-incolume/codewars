# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'

import re


def increment_string(strng) -> None:
    """
    adfafadsfasdfasdfadsf
    :param strng: String entrance
    :return: Nothing
    """
    if strng:
        base = ''.join([x for x in strng if x.isalpha()])
        try:
            seq = int(''.join([x for x in strng if x.isdigit()]))
        except ValueError:
            seq = 0
        return f'{base}{seq + 1}'
    else:
        return '1'


increment_string()
