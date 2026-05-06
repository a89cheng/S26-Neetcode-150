# Completed May, 3 2026 | 86 minutes

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letters = {}
        have = {}
        sub = "e" * 1001
        left = 0
        formed = 0

        # Here t is dealt with (we look for these)
        for char in t:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1

        # The meat of the project
        for right in range(len(s)):
            if s[right] in letters:
                if s[right] in have:
                    have[s[right]] += 1
                else:
                    have[s[right]] = 1
                if have[s[right]] == letters[s[right]]:
                    formed += 1

            while formed == len(letters):
                if len(s[left:right + 1]) < len(sub):
                    sub = s[left:right + 1]
                if s[left] in letters:
                    have[s[left]] -= 1
                    if have[s[left]] < letters[s[left]]:
                        formed -= 1
                left += 1

        if len(sub) > 1000:
            sub = ""
        return sub