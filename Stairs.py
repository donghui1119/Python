# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 23:03:06 2020

@author: DonghuiSong
"""


i=7
while i<10000:
     if (i%2==1) and (i%3==2) and (i%5==4) and (i%6==5) and (i%7==0):
         print(i)
         i+=1
     else:
      i+=1
    
        