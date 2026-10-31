# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = []

        dummy = ListNode(0)

        curr = dummy

        for ll in lists:

            while ll: 

                ans.append(ll.val)
                ll = ll.next

        ans.sort()

        for i in ans: 

            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next
