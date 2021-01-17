# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@britodfbr'
import codecs


def rot13(entrance):
    return codecs.encode(entrance, 'rot13')
