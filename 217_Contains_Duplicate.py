# Completed April, 21 2026 | 5:30 minutes

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False