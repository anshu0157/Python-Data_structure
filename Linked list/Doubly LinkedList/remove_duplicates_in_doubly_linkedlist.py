# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 14:06:34 2020

@author: anshu
"""


from Doubly_Linked_List import Doubly_llst as dl
class remove_duplicate(dl):
    dl.__init__(dl)
    def remove_dup(self):
        cur=self.head
        duplicates=[]
        deleted_value=[]
        while cur:
            if cur.data in duplicates:
                deleted_value.append(cur.data)
                self.delete_node(cur.data)
                
                cur=cur.next
            else:
                duplicates.append(cur.data)
                cur=cur.next
        print(f'The duplicate elements are:{deleted_value}')
                
r=remove_duplicate()
for i in range(int(input('enter size of linkedlist'))):
    r.append(int(input('enter elements')))
r.print_llst()
r.remove_dup()
r.print_llst()