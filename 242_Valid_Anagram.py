# Completed May, 25 2026 | 7.5 minutes

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        letters, matching = {}, {}

        for idx in range(len(s)):
            letters[s[idx]] = letters.get(s[idx], 0) + 1
        for idx in range(len(t)):
            matching[t[idx]] = matching.get(t[idx], 0) + 1

        return letters == matching