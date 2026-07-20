# Completed July, 19 2026 | 82 minutes

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        extra = []

        # So indexing becomes easier
        tree = [x for x in range(len(edges) + 1)]

        # Nodes are indexes and also nodes!
        def searcher(node):
            if tree[node] == node:
                return node

            head = searcher(tree[node])

            return head

        for pair in edges:
            head1 = searcher(pair[0])
            head2 = searcher(pair[1])
            if head1 == head2:
                extra = [pair[0], pair[1]]
            else:
                tree[head1] = head2

        return extra