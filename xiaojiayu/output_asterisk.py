# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:13:11 2020

@author: DonghuiSong
"""


number=input("please input a number:")
number=int(number)
while number:
    i=number-1#number of space
    while i:
        print(' ', end='')#末尾不换行，加空格
        i=i-1
    j=number #number of asterisk
    while j:
        print('*',end='')#
        j=j-1
    print()
    number=number-1
