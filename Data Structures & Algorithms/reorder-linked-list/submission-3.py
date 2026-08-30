# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:


        dummy = ListNode(0, head)

        slow = dummy.next 
        fast = dummy.next

        while fast and fast.next: 

            slow = slow.next
            fast = fast.next.next

        p1 = slow
        reverse = None 

        while p1:
            next_ = p1.next
            p1.next = reverse
            reverse = p1 
            p1 = next_


        p1 = dummy.next
        p2 = reverse

        while p2 and p2.next:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next



    
