# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False

        def h(slow, fast): 

            if not fast.next or not fast.next.next: return False

            if slow == fast: return True

            return h(slow.next, fast.next.next)

        return h(head, head.next)

