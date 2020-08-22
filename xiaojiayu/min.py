# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 23:59:57 2020

@author: DonghuiSong
"""


def min(x):
    least=x[0]
    for each in x:
        if each <least:
            least=each
    return least
