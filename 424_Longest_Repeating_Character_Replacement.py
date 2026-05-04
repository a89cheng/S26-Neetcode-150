# Completed April, 21 2026 | 31 minutes

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        seen = {}
        counter = 0
        m = 0

        for right in range(len(s)):

            if s[right] not in seen:
                seen[s[right]] = 1
            else:
                seen[s[right]] += 1

            # Messed up the subtraction order, would always be -ve
            # Also used if here instead of while for invalid check
            while sum(seen.values()) - max(seen.values()) > k:
                seen[s[left]] -= 1
                left += 1

            m = max(m, right - left + 1)
        return m

