# Completed April, 22 2026 | 98 minutes

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prod = 1

        # For the longest time, I forgot I could switch when to
        # update the product value inside the loop
        for left in range(0, n):
            res[left] *= prod
            prod *= nums[left]

        prod = 1

        for right in range(n - 1, -1, -1):
            res[right] *= prod
            prod *= nums[right]

        return res