# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:38:34 2020

@author: anshu
"""


from Doubly_Linked_List import Doubly_llst as dl
class pair_sum(dl):
    dl.__init__(dl)
    def sum_pair(self,sum_num):
            ls=[]
            sum_=0
            cur=self.head
            p=None
            while cur:
                p=cur.next
                while p:
                    if (cur.data + p.data) == sum_num:
                        #ls.append('(' + str(cur.data)+','+str(p.data)+')')
                        ls.append((cur.data,p.data))
                        p=p.next
                    else:
                        p=p.next
                cur=cur.next
            if not ls:
                return 'no elements are found for sum'
            else:
                return set(ls)





s=pair_sum()
for i in range(int(input('Enter size'))):
    s.append(int(input('enter elements:')))
print(s.sum_pair(5))