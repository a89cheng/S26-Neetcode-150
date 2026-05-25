# Completed May, 24 2026 | 29 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
   def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       def diver(node, depth):
           if not node:
               difference = depth - len(solution)
               for i in range(difference):
                   solution.append([])
               return


           left = diver(node.left, depth+1)
           right = diver(node.right, depth+1)
           solution[depth].append(node.val)


           return


       solution = []
       diver(root, 0)
       return solution

#======================================================
# ChatGPT came up with a queue version instead of a recursive version!

from collections import deque

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        q = deque([root])

        while q:
            level = []
            level_size = len(q)

            # process exactly one level
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)

                # push next level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(level)

        return result