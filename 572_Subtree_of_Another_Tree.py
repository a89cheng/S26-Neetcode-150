# Completed May, 22 2026 | 33 minutes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def scanner(node1, node2):
            # If they're both at the end
            if not node1 and not node2:
                return True
            # If only 1 is at the end
            if (node1 and not node2) or (node2 and not node1):
                return False
            # Check the node immediately
            if node1.val != node2.val:
                return False

            comparison_1 = scanner(node1.left, node2.left)
            comparison_2 = scanner(node1.right, node2.right)

            if comparison_1 and comparison_2:
                return True
            else:
                return False

        def locater(node1, subRoot):
            if not node1:
                return False

            check = scanner(node1, subRoot)
            left_p = locater(node1.left, subRoot)
            right_p = locater(node1.right, subRoot)

            if left_p or right_p or check:
                return True
            return False

        return locater(root, subRoot)