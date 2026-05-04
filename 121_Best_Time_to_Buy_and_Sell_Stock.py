# Completed April, 21 2026 | 20 minutes

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        buy = prices[0]

        for price in prices:
            buy = min(buy, price)
            prof = max(prof, price-buy)
        return prof