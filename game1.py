# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:04:13 2020

@author: DonghuiSong
"""


import random
times=3
secret = random.randint(1,10)
print('i love fishc')
guess=0
print('could you guess which number:', end='')
while (guess != secret) and (times>0):
    num=input()
    guess=int(num)
    times= times-1
    if guess== secret:
        print('are you worm at my heart')
        print('there are nothing')
    else:
        if guess>secret:
            print("the number is bigger than yours")
        else:
            print("the number is smaller than yours")
        if times>0:
            print('you can try again', end='')
        else: 
            print('no chance')
print('game over' )