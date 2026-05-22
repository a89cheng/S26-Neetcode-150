# Completed May, 21 2026 | 18 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def comparer(node1, node2):
            # If they're both at the end
            if not node1 and not node2:
                return True
            # If only 1 is at the end
            if (node1 and not node2) or (node2 and not node1):
                return False

            comparison_1 = comparer(node1.left, node2.left)
            comparison_2 = comparer(node1.right, node2.right)

            if comparison_1 and comparison_2 and node1.val == node2.val:
                return True
            else:
                return False

        return comparer(p, q)