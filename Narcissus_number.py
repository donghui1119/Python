# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:59:15 2020

@author: DonghuiSong
"""


for i in range (100,1000):
    sum=0
    number=i
    while number:
        sum=sum+(number%10)**3
        number//=10
        if sum==i:
            print(i)