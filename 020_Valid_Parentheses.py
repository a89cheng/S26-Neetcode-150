# Completed May, 4 2026 | 21 minutes

class Solution:
    def isValid(self, s: str) -> bool:
        #Key use of mapping
        symbols = {"(": ")", "{": "}", "[": "]"}
        recent_o = []

        for symbol in s:
            if symbol in symbols:
                recent_o.append(symbol)
            else:  # therefore a closer
                if (not recent_o or
                        symbols[recent_o[-1]] != symbol
                ):
                    return False
                recent_o.pop()

        if len(recent_o) != 0:
            return False
        return True