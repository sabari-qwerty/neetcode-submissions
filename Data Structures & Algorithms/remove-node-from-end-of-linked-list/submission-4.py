# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0 , head)

        length = 0 

        curr = dummy.next

        while curr: 

            length += 1

            curr = curr.next

        diff = (length - n) -1

        count = 0 

        curr = dummy.next

        while curr: 

            if diff  == count: 
                curr.next = curr.next.next
            else: 
                curr = curr.next

            count += 1

        if length - n == 0: return dummy.next.next



        return dummy.next
    
    
        