# Completed May, 4 2026 | 36 minutes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        former = None

        while True:
            # Save the next node
            next_head = head.next

            # Set the arrow backwards
            head.next = former

            # The next arrow should point here
            former = head

            # Check if there even is a next node
            if not next_head:
                return head

            # Move on to the next node
            head = next_head

