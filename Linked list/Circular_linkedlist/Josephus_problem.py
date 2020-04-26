# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:04:44 2020

@author: anshu
"""


#josephus problem
from Circular_linkedlist import Circular_llist as cl

class josephus(cl):
    cl. __init__(cl)
    def remove(self,node):
        cur=self.head
        if cur==node:
            self.head=cur.next
           # print(f'The removed element is {cur.data} at position 0')
            cur=None
            return
        count=0
        prev=None
        while cur.next and cur != node:
            prev=cur
            cur=cur.next
            count+=1
        prev.next=cur.next
        #print(f'The removed element is {cur.data} at position {count}')
        cur=None
    
    def josephus_prob(self,step):
        cur=self.head
        while self.__length__() >1:
            count=1
            while count != step:
                cur=cur.next
                count+=1
            print('Kill' + str(cur.data))
            self.remove(cur)
            cur=cur.next


j=josephus()
for i in range(int(input('enter the no. of nodes you want to create:'))):
    j.append(int(input('enter the elements')))

j.josephus_prob(step=3)
j.printl()
                
        
        