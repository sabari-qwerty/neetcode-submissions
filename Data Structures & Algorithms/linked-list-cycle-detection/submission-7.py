# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next: return False

        def check(p1, p2): 

            if p1 == p2: return True
            if not p2 or not p2.next or not p2.next.next: return False

            return check(p1.next, p2.next.next) 

        return check(head, head.next)