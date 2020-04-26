# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 22:57:34 2020

@author: anshu
"""

#Linkedlist class
#Singley Linkedlist

#creating Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating singly linkedlist class
class Linkedlist:
    #creating head constructor
    def __init__(self):
        self.head=None
    #creating methods
    #appending data into the list
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    #pre append the value
    def preappend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    #inserting value in b/w linked list
    def insert_into(self,prev_n,data):
        new_node=Node(data)
        if not self.head:
            return f'Linked list is empty'
        current_node=self.head
        while current_node:
            if current_node.data==prev_n:
                new_node.next=current_node.next
                current_node.next=new_node
                return
            else:
                current_node=current_node.next
    #deletion element by value
    def deletion(self,item):
        if self.head:
            prev_node=None
            current_node=self.head
            while current_node and current_node.data !=item:
                prev_node=current_node
                current_node=current_node.next
            if not current_node:
                return 'no elements found for deletion'
            prev_node.next=current_node.next
            print(f'deleted element is {current_node.data}')
            current_node=None
    #deletion by position
    def delete_pos(self,position):
        if self.head:
            current_node=self.head
            if position==0:
                self.head=current_node.next
                print(f'The deleted element {current_node.data} at position {position}')
            count=0
            prev_node=None
            while current_node and count !=position:
                prev_node=current_node
                current_node=current_node.next
                count+=1
            if not current_node:
                print(f'The position {position} not found for deletion')
                return
            prev_node.next=current_node.next
            print(f'The element {current_node.data} is deleted at position {position}')
            current_node=None
    #length of linkedlist by two method
    def length(self,method=1):
        '''method 1 for iterative approach (TYPE 1)
           method 2 for recursive approach (TYPE 2)'''
        #print(self.length.__doc__)
        if method==1:
            current_node=self.head
            count=0
            while current_node:
                current_node=current_node.next
                count+=1
            print(f'The length of linkedlist is {count}')
            return
    '''    elif method==2:
            current_node=self.head
            if not current_node:
                return 0
            return 1+self.length(current_node.next)'''

    #swaping element in linked list
    def swap_l(self,item1,item2):
        if item1==item2:
            return
        prev1=None
        current_node1=self.head
        while current_node1 and current_node1.data !=item1:
            prev1=current_node1
            current_node1=current_node1.next
        prev2=None
        current_node2=self.head
        while current_node2 and current_node2.data != item2:
            prev2=current_node2
            current_node2=current_node2.next
        if not current_node1 or not current_node2:
            print(f"items doesn't match with linkedlist data")
            return
        if prev1:
            prev1.next=current_node2
        else:
            self.head=current_node2
        if prev2:
            prev2.next=current_node1
        else:
            self.head=current_node1
        current_node1.next,current_node2.next=current_node2.next,current_node1.next


    #reverse the Linkedlist
    def reverse(self):
        print('The reverse of linkedlist:',end=' ')
        prev=None
        current_node=self.head
        while current_node:
            temp=current_node.next
            current_node.next=prev
            prev=current_node
            current_node=temp
        self.head=prev

    #removing duplicate elements
    def remove_dup(self):
        current_node=self.head
        prev=None
        duplicate= []
        while current_node:
            if current_node.data in duplicate:
                prev.next=current_node.next
                current_node=None
            else:
                duplicate.append(current_node.data)
                prev=current_node
            current_node=prev.next
    
    #merging two sorted linkedlist
    def merge(self,llist):
        p=self.head
        q=llist.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head=s
        while p and q:
            if p.data <=q.data:
                s.next=p
                s=p
                p=s.next
            else:
                s.next=q
                s=q
                q=s.next
        if not p:
            s.next=q
        if not q:
            s.next=p
        return new_head
    

    #print the nth node from last
    def nth_last_node(self,n):
        cur=self.head
        total_l=self.length() #another class method that count the length of the linkedlist
        while cur:
            if total_l ==n:
                return cur.data
            total_l -=1
            cur=cur.next
        if not cur:
            return f'{str(n)} is out of list'

    #count occurences
    def count(self,item):
        count=0
        cur=self.head
        while cur:
            if cur.data == item:
                count+=1
            cur=cur.next
        return count
    
    #rotate the node
    def rotate(self,k):
        if self.head and self.head.next:
            p=self.head
            q=self.head
            prev=None
            count=0
            while p and count<k:
                prev=p
                p=p.next
                q=q.next
                count+=1
            p=prev
            while q:
                prev=q
                q=q.next
            q=prev
            q.next=self.head
            self.head=p.next
            p.next=None

    #is palindrome using string
    def is_palindrome(self,method):
        if method==1:
            s=''
            p=self.head
            while p:
                s+=p.data
                p=p.next
            return s==s[::-1]
        elif method==2:
            l=[]
            p=self.head
            while p:
                l.append(p.data)
                p=p.next
            p=self.head
            while p:
                data=s.pop()
                if p.data != data:
                    return False
                p=p.next
            return True
        

    def move_tail_to_head(self):
        if self.head:
            p=self.head
            prev=None
            while p.next:
                prev=p
                p=p.next
            p.next=self.head
            self.head=p
            prev.next=None
    
    def print_l(self):
        if not self.head:
            return f'Linkedlist is empty'
        current_node=self.head
        while current_node:
            #print(f'{current_node.data} is at position {current_node}')
            print(current_node.data,end=' ')
            current_node=current_node.next
        print()

'''CALLING LINKEDLIST CLASS'''
l=Linkedlist()
l.append(1)
l.append(3)
l.append(5)
l.preappend(0)
l.append(7)
l.print_l()
l.insert_into(7, 9)
l.print_l()
#l.deletion(34)
l.print_l()
#l.delete_pos(3)
l.print_l()
l.length()
#l.swap_l(78, 23)
l.print_l()
#reversing of linked list
l.reverse()
l.print_l()

l.append(78)
l.preappend(90)
#removing duplicate
l.remove_dup()
l.print_l()
            
#2nd linkedlist
llist=Linkedlist()
llist.append(2)
llist.append(4)
llist.append(6)
llist.append(8)
llist.append(10)
llist.append(12)
llist.append(14)
llist.append(15)
llist.append(90)
llist.append(98)
llist.print_l()

#merging linkedlist
l.merge(llist)
l.print_l()
        
