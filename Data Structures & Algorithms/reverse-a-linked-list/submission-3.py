# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        def helper(node): 

            if not node or not node.next: return node 

            next_ = helper(node.next)

            node.next.next = node
            node.next = None 

            return next_


        return helper(head)