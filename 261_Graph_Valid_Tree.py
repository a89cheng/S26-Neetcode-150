# Completed July, 20 2026 | 8 minutes

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [x for x in range(n)]

        count = n

        def parent(node):
            if graph[node] != node:
                graph[node] = parent(graph[node])
            return graph[node]

        for pair in edges:
            head1 = parent(pair[0])
            head2 = parent(pair[1])

            if head1 != head2:
                graph[head1] = head2
                count -= 1
            else:
                return False

        return count == 1