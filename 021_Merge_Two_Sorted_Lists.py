# Completed May, 5 2026 | 28 minutes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode],
                      list2: Optional[ListNode]) -> Optional[ListNode]:

        # This part deals with empty lists
        if not list1:
            if not list2:
                return
            else:
                return list2

        if not list2:
            return list1

        # Assumes at this point neither are empty
        # Final head keeps track of the initial node
        if list1.val > list2.val:
            head = final_head = list2
            l1_next = list1
            l2_next = list2.next
        else:
            head = final_head = list1
            l1_next = list1.next
            l2_next = list2

        while True:
            if not l1_next and not l2_next:
                head.next = None
                return final_head
            elif not l1_next:
                head.next = l2_next
                return final_head
            elif not l2_next:
                head.next = l1_next
                return final_head
            else:
                if l1_next.val > l2_next.val:
                    head.next = l2_next
                    l2_next = l2_next.next
                else:
                    head.next = l1_next
                    l1_next = l1_next.next

            # Important and forgot early on
            head = head.next