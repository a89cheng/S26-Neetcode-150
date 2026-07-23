# Completed July 21, 2026 | 90 minutes

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Guideline: use index as a reference to which node.
        n = len(points)

        distances = [float("inf")] * n
        distances[0] = 0

        added = [False] * n

        for times in range(n):
            # 1. Select the shortest node to the bunch (O(n))

            curr = float("inf")

            for idx in range(n):
                if not added[idx] and (curr > distances[idx]):
                    curr = distances[idx]
                    node = idx

            # 2. After selection, mark it down
            added[node] = True

            # 3. Update all distances
            for i in range(n):
                if added[i]:
                    continue

                distance = (
                        abs(points[node][0] - points[i][0]) +
                        abs(points[node][1] - points[i][1])
                )

                if distance < distances[i]:
                    distances[i] = distance

        return sum(distances)