# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findMid(self, head): 

        slow = head
        fast = head.next

        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next

        next_ = slow.next
        slow.next = None

        return next_

    def reverse(self, head): 
        rev = None
        curr = head

        while curr: 

            next_ = curr.next
            curr.next = rev
            rev = curr 
            curr = next_

        return rev


    def reorderList(self, head: Optional[ListNode]) -> None:

        mid = self.findMid(head)

        p1 = head
        p2 = self.reverse(mid)

        while p1 and p1.next:

            p1_next, p2_next = p1.next, p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next

        if p2: 
            p1.next = p2
            




