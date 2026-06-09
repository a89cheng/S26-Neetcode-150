# Completed June, 4 2026 | 7 minutes

class Solution:
   def isPalindrome(self, s: str) -> bool:
       construct = ""

       for idx in range(len(s) ):
           if s[idx].isalnum():
               construct = construct + s[idx]

       construct = construct.lower()

       return construct == construct[::-1]