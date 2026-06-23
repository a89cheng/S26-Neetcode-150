# Completed June, 20 2026 | 41 minutes

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        cur = []

        def saved_state(s_idx=0):
            # Always start by saving the copy of current
            res.append(cur[:])

            for idx in range(s_idx, len(nums)):
                if idx > s_idx and nums[idx] == nums[idx - 1]:
                    continue
                cur.append(nums[idx])
                saved_state(idx + 1)
                cur.pop()

        saved_state(s_idx=0)
        return res