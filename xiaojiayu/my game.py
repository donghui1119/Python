# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:20:10 2020

@author: DonghuiSong
"""


import random
secret=random.randint(1,10)
secret=int(secret)
guess=0
times=3
print('please guess')
while (guess!=secret )and (times!=0):
    num=input()
    guess=int(num)
    times=times-1
    if guess==secret:
        print('your are my friend')
    else:
        if guess<secret:
           print("smaller")
        else:
           print("bigger")

if times>0:
          print("try again")
else:
      print('game over')
    
