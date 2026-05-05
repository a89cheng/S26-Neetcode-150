# Completed April, 25 2026 | 17 minutes

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                #it means the right side is sorted
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1

        return nums[right]