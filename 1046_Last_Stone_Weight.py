# Completed June, 7 2026 | 7.5 minutes

# In fact, runs faster on Leetcode!
"""
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)

            diff = stones.pop(0) - stones.pop(0)

            if diff:
                stones.append(diff)

        if stones:
            return stones[0]
        return 0
"""

# Solution here is better in the long-term given popping from the start
# and sorting is covered by heapq!
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            diff = -s1 - -s2

            if diff:
                heapq.heappush(stones, -diff)

        if stones:
            return -stones[0]
        return 0