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

        prev = None
        curr = head

        while curr: 

            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_
        
        return prev 


    

    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next: return 

        p2 = self.reverse(self.findMid(head))
        p1 = head

        while p1 and p1.next: 
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next


            p1 = p1_next
            p2 = p2_next

        p1.next = p2
