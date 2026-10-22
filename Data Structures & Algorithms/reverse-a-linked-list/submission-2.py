# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        curr = dummy.next
        
        rev = None

        while curr: 

            next_ = curr.next
            curr.next = rev
            rev = curr
            curr = next_
        

        return rev
