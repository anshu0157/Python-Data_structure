# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 17:25:19 2020

@author: anshu
"""

#creating class Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Circular_llist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=new_node
            self.head=new_node
            return
        cur=self.head
        while cur.next != self.head:
            cur=cur.next
        cur.next=new_node
        new_node.next=self.head
    
    def preappend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        if not self.head:
            new_node.next=new_node
            self.head=new_node
            return
        cur=self.head
        while cur.next !=self.head:
            cur=cur.next
        cur.next=new_node
        self.head=new_node
    
    def remove(self,key):
        cur=self.head
        if cur.data==key:
            self.head=cur.next
            print(f'The removed element is {cur.data} at position 0')
            cur=None
            return
        count=0
        prev=None
        while cur.next and cur.data !=key:
            prev=cur
            cur=cur.next
            count+=1
        prev.next=cur.next
        print(f'The removed element is {cur.data} at position {count}')
        cur=None
        
    def __length__(self):
        cur=self.head
        count=0
        while cur:
            count+=1
            cur=cur.next
            if cur == self.head:
                break
        print(f'Length of linkedlist is {count}')
        return count
    
    def split_in2(self):
        size=self.__length__()
        if size==0:
            return
        if size==1:
            return self.head
        mid=size//2
        count=0
        prev=None
        cur=self.head
        while cur and count <mid:
            prev=cur
            cur=cur.next
            count+=1
        prev.next=self.head
        #creating instance of clinkedlist
        split=Circular_llist()
        while cur.next !=self.head:
            split.append(cur.data)
            cur=cur.next
        split.append(cur.data)
        #printing the splitted list
        self.printl()
        split.printl()
        
    
    def printl(self):
        cur=self.head
        while cur:
            #print(cur,cur.data,cur.next)
            print(cur.data,end=' ')
            cur=cur.next
            if cur ==self.head:
                break
        print()

'''        
c=Circular_llist()
c.preappend(22)
c.append(23)
c.append(90)
c.append(34)
c.preappend(87)
c.preappend(899)
c.append(78)
c.printl()
#c.remove(34)
c.printl()
c.__length__()
c.split_in2()
'''