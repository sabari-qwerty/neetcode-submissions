# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next: return False

        def findCycle(p1, p2): 

            if not p2 or not p2.next: return False

            if p1 == p2: return True

            return findCycle(p1.next, p2.next.next)

        return findCycle(head, head.next)