# Completed June, 4 2026 | 10 minutes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        n2 = ""

        while l1:
            n1 = str(l1.val) + n1
            l1 = l1.next

        while l2:
            n2 = str(l2.val) + n2
            l2 = l2.next

        tot = int(n1) + int(n2)
        rev = str(tot)[::-1]
        length = len(rev)

        first_node = ListNode()
        node = first_node

        for idx in range(length - 1):
            node.val = int(rev[idx])
            node.next = ListNode()
            node = node.next
        node.val = int(rev[-1])

        return first_node