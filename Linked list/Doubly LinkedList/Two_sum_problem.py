# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:30:54 2020

@author: anshu
"""

#first approach of time complexity O(n^2) and space complexity O(1)
def two_sum(A,sum_):
    a=len(A)
    for i in range(a-1):
        for j in range(i+1,a):
            if A[i]+A[j]==sum_:
                print(A[i],A[j])
                return True
    return False

#2nd approach of time complexity O(n) and space complexity O(1)
def two_sum2(A,sum_):
    i=0
    j=len(A)-1
    while i <j:
        if A[i] +A[j] == sum_:
            print(A[i],A[j])
            return True
        elif A[i] + A[j] <sum_:
            i+=1
        else:
            j-=1
    return False

a1=[1,2,3,5,22,6,7]
a2=[2,3,5,6,2,9,8,7]
print(two_sum(a1,28))
print(two_sum2(a1,28))