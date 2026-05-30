# Completed May, 29 2026 | 11 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checker(node, minimum):
            if not node:
                return
            if node.val >= minimum:
                counter.append(0)
                minimum = node.val

            checker(node.left, minimum)
            checker(node.right, minimum)

        counter = []
        checker(root, float("-inf"))
        return len(counter)

