# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not l1 or not l2: return l1 if l1 else l2

        if l1.val < l2.val:
           node = self.mergeTwoLists(l1.next, l2)

           l1.next  = node

           return l1

        else: 
            node = self.mergeTwoLists(l1, l2.next)

            l2.next = node
            
            return l2

        


             

            

        