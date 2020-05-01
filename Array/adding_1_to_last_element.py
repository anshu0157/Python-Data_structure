# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:04:17 2020

@author: anshu
"""

#Arbitray precision increment
#simple way in python
a=[1,4,9]
s=''.join(map(str,a))
print(int(s)+1)

#lets apply algorithm
def plus_one(A):
    A[-1]+=1
    for i in reversed(range(1,len(A))):
        if A[i] !=10:
            break
        A[i]=0
        A[i-1]+=1
    if A[0]==10:
        A[0]=1
        A.append(0)
    return A

A1=[1,2,4,9]
A2=[9,9,9,9]
print(plus_one(A1))
print(plus_one(A2))