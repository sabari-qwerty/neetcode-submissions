# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head or not head.next: return False


        def helper(slow, fast): 

            if not fast or not fast.next: return False

            if slow == fast: return True 

            return helper(slow.next, fast.next.next)

        return helper(head, head.next)

            

