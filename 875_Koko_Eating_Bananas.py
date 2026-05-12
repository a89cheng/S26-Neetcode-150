# Completed May, 11 2026 | 47 minutes

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        least = 1
        most = max(piles)
        k = most

        while least < most:
            current_k = (most + least) // 2
            req_h = 0
            for bananas in piles:
                req_h += int(math.ceil(bananas / current_k))
            if req_h <= h:
                most = current_k
                k = min(current_k, k)
            else:
                least = current_k + 1

        return k