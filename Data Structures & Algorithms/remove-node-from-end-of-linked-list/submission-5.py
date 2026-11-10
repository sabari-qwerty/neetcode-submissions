# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head: return None

        if not head.next: return head.next


        dummy = ListNode(0, head)

        p1 = dummy
        p2 = head

        while n > 0: 
            n -= 1 
            p2 = p2.next 

        
        while p2: 

            p1 = p1.next 
            p2 = p2.next

        p1.next = p1.next.next

        return dummy.next

        