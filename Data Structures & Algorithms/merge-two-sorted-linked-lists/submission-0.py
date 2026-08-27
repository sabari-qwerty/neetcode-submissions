# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyNode = ListNode()

        curr = dummyNode

        l1 = list1
        l2 = list2 


        while l1 and l2: 

            if l1.val < l2.val: 
                curr.next = l1
                curr = curr.next
                l1 = l1.next

            else: 
                curr.next = l2
                curr = curr.next
                l2 = l2.next

        while l1: 

            curr.next = l1
            curr = curr.next
            l1 = l1.next
        
        while l2: 
            curr.next = l2
            curr = curr.next
            l2 = l2.next

        return dummyNode.next

