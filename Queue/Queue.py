# -*- coding: utf-8 -*-
"""
Created on Fri May  1 19:21:26 2020

@author: anshu
"""
#from python inbuilt function
from collections import deque
'''
q=deque()
q.append(3)
q.append(9)
q.append(8)
q.append(78)
q.append(67)
print(q)
q.popleft()
q.pop()
print(q)
'''

#from scratch
class Queue(object):
    def __init__(self):
        self.items=[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def __len__(self):
        return len(self.items)
    def size(self):
        if self.is_empty():
            return 0
        else:
            return len(self.items)
'''
q=Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
print(q.items)
q.dequeue()
print(q.items)
print(q.size())
print(q.peek())
print(len(q))
'''