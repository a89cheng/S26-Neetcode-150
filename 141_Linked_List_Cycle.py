# Completed May, 5 2026 | 26 minutes

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#         self.val = x
#         self.next = None

"""The solution below is not good practice; it involves destroying node values"""
#class Solution:
#    def hasCycle(self, head: Optional[ListNode]) -> bool:

#        if not (head and head.next and head.next.next):
#            return False

#        fast = head.next.next
#        slow = head.next

#        while fast and fast.next:
#            if fast == slow:
#                 return True

#            fast = fast.next.next
#            slow = slow.next

#        return False


# Completed May, 5 2026 | 20 minutes

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not (head and head.next and head.next.next):
            return False

        fast = head.next.next
        slow = head.next

        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False
