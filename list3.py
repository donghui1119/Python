# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:04:50 2020

@author: DonghuiSong
"""


list7=[]
for x in range(10):
    for y in range(10):
     if x%2==0:
         if y%2!=0:
            list7.append((x,y))