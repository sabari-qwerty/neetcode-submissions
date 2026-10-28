# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        values = []

        for ll in lists: 

            while ll: 

                values.append(ll.val)

                ll = ll.next

        values.sort()

        dummy = ListNode(0)

        curr = dummy

        for i in values:

            curr.next = ListNode(i)

            curr = curr.next

        return dummy.next