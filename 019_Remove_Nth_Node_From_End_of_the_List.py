# Completed May, 5 2026 | 26 minutes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode],
                         n: int) -> Optional[ListNode]:
        fixed_head = head

        for i in range(n):
            head = head.next
            if not head:
                fixed_head = fixed_head.next
                return fixed_head

        scout = head
        slow = fixed_head

        while scout:
            # Checks for if this is the one before n
            if not scout.next:
                slow.next = slow.next.next
                return fixed_head
            slow = slow.next
            scout = scout.next