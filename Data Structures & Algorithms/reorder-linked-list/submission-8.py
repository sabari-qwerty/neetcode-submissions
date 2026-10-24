from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitInHalf(self, head: ListNode) -> Optional[ListNode]:
        """Severs the list in two and returns the head of the second half.
        On odd lengths the second half gets the extra node."""
        slow, fast = head, head.next

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        second = slow.next
        slow.next = None
        return second

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        second = self.reverseList(self.splitInHalf(head))
        p1 = head

        while p1.next:
            temp1, temp2 = p1.next, second.next

            p1.next = second
            second.next = temp1

            p1 = temp1
            second = temp2

        p1.next = second