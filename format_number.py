# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 22:03:03 2020

@author: DonghuiSong
"""

m=True

while m:
    numb=input('please input a number:(quit while it is Q )')
    if numb!='p':
       numb=int(numb)  
       print('十进制->十六进制：%d->%x' %(numb,numb))
       print('十进制->八进制：%d->%o' %(numb,numb))
       print('十进制->二进制：%d->' % numb,bin(numb))
    else:
       m=False