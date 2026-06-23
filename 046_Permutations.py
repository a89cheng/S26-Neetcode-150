# Completed June, 20 2026 | 30 minutes

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        cur = []
        clone = nums[:]
        nums.sort()

        def creator():
            if len(cur) == len(nums):
                ans.append(cur[:])
                return

            for idx in range(0, len(clone)):
                hold = clone.pop(idx)

                cur.append(hold)

                creator()

                cur.pop()

                clone.insert(idx, hold)

        creator()
        return ans