# Completed May, 2 2026 | 36 minutes

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        most = 0

        while left < right:
            wid = right - left
            height = min(heights[right], heights[left])
            cur = height * wid

            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1

            most = max(cur, most)

        return most