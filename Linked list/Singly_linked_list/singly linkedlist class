#creating Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

#creating linkedlist
class Linkedlist:
    def __init__(self):
        self.head=None
    
    #appending the value at last
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node
    
    #inserting value at the begining
    def preappend(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    #inserting the value at given position
    def insert_into(self,prev_node,data):
        new_node=Node(data)
        if not self.head:
            print("Linked list is empty")
            return
        curnt_node=self.head
        while curnt_node.next:
            if curnt_node.data==prev_node:
                new_node.next=curnt_node.next
                curnt_node.next=new_node
                return
            else:
                curnt_node=curnt_node.next
    
    
    #printing the position 
    def position(self,item):
        pos=0
        if not self.head:
            print('Linkedlist is empty')
            return
        curnt_node=self.head
        while curnt_node:
            if curnt_node.data== item:
                print(f'Position of {item}:{pos}')
                break
            else:
                pos+=1
                curnt_node=curnt_node.next
        
    
    #deletion by value
    def deletion(self,item):
        curnt_node=self.head
        if curnt_node and curnt_node.data == item:
            self.head=curnt_node.next
            print(f'deleted element is {curnt_node}')
            curnt_node=None
            return
        prev=None
        while curnt_node and curnt_node.data !=item:
            prev=curnt_node
            curnt_node=curnt_node.next
        if curnt_node is None:
            print(f'Element not found in list for deletion')
            return
        prev.next=curnt_node.next
        print(f'deleted element is {curnt_node.data}')
        curnt_node=None
        
    #deletion by position
    def delete_by_pos(self,pos):
        if self.head !=None:
            curnt_node=self.head
            if pos==0:
                self.head=curnt_node.next
                print(f'deleted element is {curnt_node.data} at position {pos}')
                curnt_node=None
                return
            
            prev=None
            count=0
            while curnt_node and count != pos:
                prev=curnt_node
                curnt_node=curnt_node.next
                count+=1
            if curnt_node is None:
                print('position not found in list')
                return
            prev.next=curnt_node.next
            print(f'deleted element is {curnt_node.data} at position {count}')
            curnt_node=None
    
    #calculating length of linkedlist iteratively
    def length_iter(self):
        count=0
        curnt_node=self.head
        while curnt_node:
            curnt_node=curnt_node.next
            count+=1
        return count
    
    #calculating length recursively
    def length_rec(self,node):
        if node is None:
            return 0
        return 1+self.length_rec(node.next)
    
    #swapping of given two node
    def swap(self,item_1,item_2):
        if item_1 == item_2:
            return
        prev_1=None
        curr_1=self.head
        while curr_1 and curr_1.data != item_1:
            prev_1=curr_1
            curr_1=curr_1.next
        prev_2=None
        curr_2=self.head
        while curr_2 and curr_2.data !=item_2:
            prev_2=curr_2
            curr_2=curr_2.next
        
        if not curr_1 or not curr_2:#if curr_1 or curr_2 is not found
            return
 
        if prev_1:                           #if previous node 1 found
            prev_1.next=curr_2      #previous node 1 next element be curr_2(2nd item)
        else:                                #if previous node 1 not found
            self.head=curr_2        #current node 2 will be the head
            
        if prev_2:                           #if previous node 2 found
            prev_2.next=curr_1      #previous node 2  next element will be assign to current node 1
        else:                                #if previous node 2 not found
            self.head=curr_1        #current node 1 will be head
            
        curr_1.next,curr_2.next=curr_2.next,curr_1.next    #now next element will be swapped
    
    
    #reverse the linked list
    def reverse(self):
        prev=None
        currnt_node=self.head
        while currnt_node:
            nxt=currnt_node.next
            currnt_node.next=prev
            prev=currnt_node
            currnt_node=nxt
        self.head=prev
        
    #merging two sorted list
    def merge(self,llist):
        p=self.head
        q=llist.head
        s=None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data<=q.data:
                s=p
                p=s.next
            else:
                s=q
                q=s.next
            new_head = s
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
    
    #removing duplicates in linkedlist
    def remove_dup(self):
        prev=None
        cur=self.head
        dup_val=[]
        while cur:
            if cur.data in dup_val:
                #removing node
                prev.next=cur.next
                cur=None
            else:
                dup_val.append(cur.data)
                prev=cur
            cur=prev.next
    #print the nth node from last
    def nth_last_node(self,n):
        cur=self.head
        total_l=self.length_iter()
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
    #printing list
    def print_list(self):
        curnt_node=self.head
        while curnt_node != None:
            print(curnt_node.data,end=' ')
            curnt_node=curnt_node.next
        print()
        
        
        
l=Linkedlist()
l.append(67)
l.append(89)
l.append(78)
l.append(90)
l.append(60)
l.preappend(92)
l.print_list()
