# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head: return head
        if not head.next: return head.next

        dummy = ListNode(0, head)
        p2 = head
        p1 = dummy
    

        while n > 0:
            p2 = p2.next 
            n -= 1

        while p2: 
            p2 = p2.next

            p1 = p1.next

        p1.next = p1.next.next

        return dummy.next

