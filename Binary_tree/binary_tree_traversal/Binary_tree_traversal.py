# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 22:05:37 2020

@author: anshu
"""
class Queue:
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
            return self.items[-1].data
    def __len__(self):
        return len(self.items)
    def size(self):
        if self.is_empty():
            return 0
        else:
            return len(self.items)

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class binary_tree:
    def __init__(self,data):
        self.root=Node(data)
        
    def traverse_tree(self,type):
        if type=='preorder':
            return self.pre_order(self.root)
        elif type == 'inorder':
            return self.in_order(self.root)
        elif type == 'postorder':
            return self.post_order(self.root)
        elif type == 'levelorder':
            return self.level_order(self.root)
        else:
            print(f'''Tree traversal type {str(type.upper())} is not supported!
                  CHECK YOUR SPELLING MISTAKE
                  please enter valid one:
                      for DFS:1.preoder
                              2.inorder
                              3.postorder
                      for BFS:4.levelorder''')
            return False
        
    #DFS traversal (depth first search)
    def pre_order(self,root,traverse=""):
        '''ROOT->LEFT->RIGHT'''
        if root:
            traverse+=str(root.data) + ' ' 
            traverse+=self.pre_order(root.left)
            traverse+=self.pre_order(root.right)
        return traverse
    def in_order(self,root,traverse=""):
        '''LEFT->ROOT->RIGHT'''
        if root:
            traverse+=self.in_order(root.left)
            traverse+=str(root.data) + ' '
            traverse+=self.in_order(root.right)
        return traverse
    
    def post_order(self,root,traverse=''):
        '''LEFT->RIGHT->ROOT'''
        if root:
            traverse+=self.post_order(root.left)
            traverse+=self.post_order(root.right)
            traverse+=str(root.data) + ' '
        return traverse
    
    #BFS traversal (breadth first search)
    def level_order(self,root,traverse=''):
        '''LEVEL BY LEVEL'''
        if not root:
            return
        q=Queue()
        q.enqueue(root)
        while len(q)>0:
            traverse+=str(q.peek()) + ' '
            node=q.dequeue()
            
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return traverse
    def reverse_level_order(self):
        a=str(self.level_order(self.root)).split()
        return ' '.join(a[::-1])   
'''
tree=binary_tree(Node(1))
tree.root=Node(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.left.right=Node(9)
print(tree.traverse_tree('levelorder'))
print(tree.reverse_level_order())
'''