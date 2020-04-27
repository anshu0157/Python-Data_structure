# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 01:30:58 2020

@author: anshu
"""


from Circular_linkedlist import Circular_llist as cl
from Singly_linkedlist import Linkedlist as sl

def is_circularlinkedlist(cllist):
     cur=cllist.head
     while cur.next:
         cur=cur.next
         if cur.next == cllist.head:
             return True
     return False

c=sl()
for i in range(int(input('enter the size of an element:'))):
    c.append(int(input('enter the element:')))
print(is_circularlinkedlist(c))