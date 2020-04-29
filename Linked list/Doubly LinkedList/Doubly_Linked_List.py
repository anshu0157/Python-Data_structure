# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:20:27 2020

@author: anshu
"""


#creating node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

#creating doubly linkedlist class
class Doubly_llst:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head==None:
            new_node.prev=None
            self.head=new_node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur
            new_node.next=None
            
            
    def preappend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.prev=None
            self.head=new_node
        else:
            self.head.prev=new_node
            new_node.next=self.head
            new_node.prev=None
            self.head=new_node
            
    def add_nodeafter(self,item,data):
        new_node=Node(data)
        cur=self.head
        while cur:
            if cur.next==None and cur.data==item:
                self.append(data)
                return
            elif cur.data == item:
                temp=cur.next
                new_node.next=temp
                new_node.prev=cur
                cur.next=new_node
                temp.prev=new_node
                return
            cur=cur.next
    def add_nodebefore(self,item,data):
        new_node=Node(data)
        cur=self.head
        while cur:
            if cur==self.head and cur.data==item:
                self.preappend(data)
                return
            elif cur.data == item:
                temp=cur.prev
                new_node.next=cur
                temp.next=new_node
                new_node.prev=temp
                cur.prev=new_node
                return
            cur=cur.next
    def delete_node(self,item):
        #case1:linkedlist is empty
        if not self.head:
            print('Doubly linkedlist is empty')
            return
       
        cur=self.head
        while cur:
            if cur.data==item and cur==self.head:
                 #case2:The only node is availabele in linkedlist
                 if not cur.next:
                     print(f'deleted element from list is {cur.data}\nNOW LINKEDLIST IS EMPTY ENTER NEXT NODE')
                     cur=None
                     self.head=None
                     return
                 #case3:deletion of head node if there is next node available 
                 else:
                     temp=cur.next
                     temp.prev=None
                     self.head=temp
                     print(f'deleted element from list is {cur.data}')
                     cur=None
                     return
                
            #case4:deletion of node inside the linkedlist
            elif cur.next !=None and cur.data==item:
                temp=cur.next
                temp1=cur.prev
                temp1.next=temp
                temp.prev=temp1
                print(f'The deleted element will be {cur.data}')
                cur=None
                return
            #case5:deletion of last node
            elif cur.next==None and cur.data==item:
                temp=cur.prev
                temp.next=None
                print(f'The deleted element will be {cur.data}')
                cur=None
                return
            cur=cur.next
        #case6:if deletion element not found
        if not cur:
            print('deletion element not found')
            
            
    def reverse_node(self):
        
        temp=None
        cur=self.head
        while cur:
            temp=cur.prev
            cur.prev=cur.next
            cur.next=temp
            cur=cur.prev
        if temp:
            self.head=temp.prev
        
            
            
        
            
    def print_llst(self):
        cur=self.head
        while cur !=None:
            #rint(f'previous node address {cur.prev} \ncurrent node address {cur} data: {cur.data}\nnext node address{cur.next}')
            print(cur.data,end=' ')
            if cur.next == None:
                break
            cur=cur.next
        print()
    '''print('printing data from backward')
        while cur:
            print(cur.data,end=' ')
            #print(f'previous node address {cur.prev} \ncurrent node address {cur} data: {cur.data}\nnext node address{cur.next}')
            cur=cur.prev
        print()'''

D=Doubly_llst()

D.append(79)
D.append(23)
D.append(34)
D.append(78)
D.append(90)
D.preappend(20)
D.add_nodeafter(79,40)
D.add_nodeafter(90,'Anshu')
D.add_nodeafter(23,'RAJPUTANA')
D.add_nodebefore(90, 'SINGH')
D.append(45)
D.append(67)
D.print_llst()
#deleting node
#D.delete_node(45)
#D.print_llst()
D.reverse_node()
D.print_llst()