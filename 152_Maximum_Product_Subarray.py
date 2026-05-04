# Completed April, 23 2026 | 60 minutes

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        view = set()
        left = 0
        mp = nums[left]
        p = 1

        for right in range(len(nums)):
            p *= nums[right]

            while p < mp and left < right:
                p /= nums[left]
                view.remove(nums[left])
                left+=1

            if p > mp:
                mp = p

            view.add(nums[right])
        return mp