# Completed May, 24 2026 | 21 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       from collections import deque

       if not root:
           return []

       block = deque([root])
       solution = []

       while block:
           hold = []
           nodes = len(block)
           for i in range(nodes):
               current = block.popleft()
               if current.left:
                   hold.append(current.left)
               if current.right:
                   hold.append(current.right)

           solution.append(current.val)
           block = deque(hold)

       return solution