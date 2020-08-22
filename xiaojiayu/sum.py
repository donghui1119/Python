# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 00:03:39 2020

@author: DonghuiSong
"""


def sum(x):
    result=0
    for each in x:
        if (type(each)==int or type(each)==float):
            result += each
        else:
            continue
        
    return result
