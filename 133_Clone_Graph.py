# Completed June, 27 2026 | 36 minutes

"""
# Definition for a Node.
class Node:
   def __init__(self, val = 0, neighbors = None):
       self.val = val
       self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        copies = {}

        def diver(node):
            if not node:
                return None
            if node in copies:
                return copies[node]

            new_copy = Node(node.val, [])
            copies[node] = new_copy

            for next_node in node.neighbors:
                neigh = diver(next_node)
                new_copy.neighbors.append(neigh)

            return copies[node]

        return diver(node)