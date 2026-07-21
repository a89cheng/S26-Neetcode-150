# Completed July 20, 2026 | 18 minutes

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Allow all nodes to correspond to indices
        graph = [x for x in range(n)]
        groups = n

        def leader(node):
            if graph[node] == node:
                return node

            head = leader(graph[node])

            return head

        for pair in edges:
            head1 = leader(pair[0])
            head2 = leader(pair[1])

            if head1 != head2:
                graph[head1] = head2
                groups -= 1

        return groups