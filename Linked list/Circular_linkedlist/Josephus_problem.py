# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 00:04:44 2020

@author: anshu
"""


#josephus problem
from Circular_linkedlist import Circular_llist as self

class josephus(self):
    self. __init__(self)
    def jremove(self,node):
        if self.head==node:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            if self.head == self.head.next:
                self.head=None
                return
            else:
                cur.next=self.head.next
                self.head=self.head.next
        else:
            cur=self.head
            prev=None
            while cur.next != self.head:
                prev=cur
                cur=cur.next
                if cur == node:
                    prev.next=cur.next
                    cur=cur.next
                
                
        
            
            
        
    def josephus_prob(self,step):
        cur=self.head
        while self.__length__() > 1:
            count=1
            while count != step:
                cur=cur.next
                count+=1
            print('Kill' + str(cur.data))
            self.jremove(cur)
            cur=cur.next
    

j=josephus()
for i in range(int(input('enter the no. of nodes you want to create:'))):
    j.append(int(input('enter the elements')))

j.josephus_prob(step=2)
j.printl()
#j.jremove(3)
#j.printl()
                

        
        