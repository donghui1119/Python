# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 21:08:27 2020

@author: DonghuiSong
"""


# 密码安全性检查代码
#
# 低级密码要求：
#   1. 密码由单纯的数字或字母组成
#   2. 密码长度小于等于8位
#
# 中级密码要求：
#   1. 密码必须由数字、字母或特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）任意两种组合
#   2. 密码长度不能低于8位
#
# 高级密码要求：
#   1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#   2. 密码只能由字母开头
#   3. 密码长度不能低于16位

symbols = r'"~!@#$%^&*()_=-/,.?<>;:[]{}|\"'
chart='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbs='0123456789'
password=input('please input the password:')
length=len(password)
while (password.isspace() or length==0):
    password=input('the password is space,please reinput')
    length=len(password)
if length<=8:
     flag_len=1
elif 8<length<16:
     flag_len=2
else:
     flag_len=3
         
flag_count=0

for each in password:
    if each in symbols:
        flag_count+=1
        break
for each in password:
    if each in numbs:
        flag_count+=1
        break
for each in password:
    if each in chart:
        flag_count+=1
        break
        
while 1:
   print('password level:', end='')  
   if flag_len==1 or flag_count==1:
     print("low")
   elif flag_len==3  and flag_count==3 and (password[0]in chart):
     print('high')
     break
   else:
    print('medium')
    
   print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
   break

     
        

         
        
    
    
