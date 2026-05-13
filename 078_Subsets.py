# Completed May, 13 2026 | 36 minutes

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        solution = []

        def appender(nums, subset, idx):
            if idx == len(nums):
                # Key to making a copy of the list!
                copy = subset[:]
                solution.append(copy)
                return

            if idx != len(nums):
                subset.append(nums[idx])
                appender(nums, subset, idx + 1)
                subset.pop(-1)

            if idx != len(nums):
                appender(nums, subset, idx + 1)

        appender(nums, subset, 0)
        return solution