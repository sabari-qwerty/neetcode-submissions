# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        length = 0 

        curr =  dummy.next

        while curr: 

            length += 1

            curr = curr.next

        if length - n == 0: return dummy.next.next


        p1 = dummy.next

        for i in range(length-1): 

            if i+1 == length - n: 
                p1.next = p1.next.next
                break

            p1 = p1.next

        return head

        


            

         
      
