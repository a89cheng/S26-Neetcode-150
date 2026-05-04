# Completed April, 21 2026 | 23 minutes

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_index = 0
        seen_set = set()
        max_length = 0

        #Iterate through each index right one by one
        for right_index in range(len(s)):

            while s[right_index] in seen_set:
                seen_set.remove(s[left_index])
                left_index += 1

            seen_set.add(s[right_index])
            max_length = max(max_length, right_index-left_index+1)

        return max_length