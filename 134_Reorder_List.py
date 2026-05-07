# Completed May, 6 2026 | 102 minutes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def reorderList(self, head: Optional[ListNode]) -> None:
       """
       Do not return anything, modify head in-place instead.
       """
       mod_head = head
       counter = 1

       #Record the number of nodes
       while mod_head.next:
           mod_head = mod_head.next
           counter += 1

       mod_head = second_half = head

       #Find the start of the second half
       for mid in range((counter) // 2 - 1):
           second_half = second_half.next

       end_first = second_half
       second_half = second_half.next
       end_first.next = None

       #Reverse the 2nd part
       former = None
       node_next = second_half
       while node_next:
           node_next = second_half.next
           second_half.next = former
           former = second_half
           second_half = node_next

       second_half = former

       #Merge the 2 lists
       for idx in range(counter // 2):
           first_next = mod_head.next
           second_next = second_half.next

           mod_head.next = second_half
           second_half.next = first_next

           last_node = second_half
           mod_head = first_next
           second_half = second_next

           if not first_next and counter % 2:
               last_node.next = second_half