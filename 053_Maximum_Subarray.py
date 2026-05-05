# Completed April, 24 2026 | 8 minutes

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        most = nums[0]
        n = len(nums)
        if n == 1:
            return most

        s = nums[0]

        for idx in range(1,n):
            most = max(nums[idx],most + nums[idx])

            if most > s:
                s = most
        return s