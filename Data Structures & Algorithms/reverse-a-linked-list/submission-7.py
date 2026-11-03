# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        
        reverse = None

        while curr: 

            next_ = curr.next
            curr.next = reverse
            reverse = curr
            curr = next_

        return reverse