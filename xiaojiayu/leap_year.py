# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:15:55 2020

@author: DonghuiSong
"""


year1=input('please input a year:')
year=int(year1)
if (year%4==0) and (year%100!=0):
    print(year+ 'is leap year')
elif year%400==0:
    print(year1+'is leap year')
else:
    print(year1+'is normal year')
