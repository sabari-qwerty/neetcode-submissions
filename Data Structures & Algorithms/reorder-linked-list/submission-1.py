# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dummy = ListNode(0, head)

        slow, fast = dummy.next, dummy.next

        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next

        curr = slow 
        reverse = None 

        while curr: 

            next_ = curr.next
            curr.next = reverse
            reverse = curr 
            curr = next_ 

        nHead = dummy.next
        reversed_ = reverse

        while reversed_ and reversed_.next: 
            nHead_next = nHead.next
            reversed_next = reversed_.next

            nHead.next = reversed_
            reversed_.next = nHead_next

            nHead = nHead_next
            reversed_ = reversed_next










        
            