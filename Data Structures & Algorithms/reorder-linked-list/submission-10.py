# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def findMid(self, head): 

        slow = head
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next
            fast = fast.next.next

        next_ = slow.next

        slow.next = None

        return next_ 


    def reverse(self, head): 

        curr = head
        rev = None 

        while curr: 

            next_ = curr.next
            curr.next = rev
            rev = curr
            curr = next_

        return rev

    def marge(self, p1, p2):

        while p2: 

            temp1, temp2 = p1.next, p2.next

            p1.next = p2 
            p2.next = temp1 

            p1 = temp1 
            p2 = temp2 


        


    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next: return 

        mid = self.findMid(head)
        reverse = self.reverse(mid)

        self.marge(head, reverse)

        



        