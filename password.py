# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:38:51 2020

@author: DonghuiSong
"""


count=3
password='fishc.com'
while count:
    passwd=input('please input password:')
    if passwd==password:
        print('password is correct')
        break
    elif '*'in passwd:
        print('*should not in password,','you have',count,'chance', end='')
        continue
    else:
        print('the password is uncorrect')
        count-=1