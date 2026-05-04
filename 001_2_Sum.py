# Completed April, 20 2026 | 10 minutes

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, val in enumerate(nums):
            remainder  = target - val
            if remainder in seen:
                return [seen[remainder],idx]
            #Hashmap of value to index...
            seen[val] = idx