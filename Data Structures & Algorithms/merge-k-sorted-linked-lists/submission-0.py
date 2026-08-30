# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ans = []


        for i in lists:

            curr = i

            while curr:

                ans.append(curr.val)

                curr = curr.next

        sorted_list = sorted(ans)

        dummy = ListNode(0)

        curr = dummy

        for i in sorted_list:

            curr.next = ListNode(i)
            curr = curr.next

        return dummy.next

