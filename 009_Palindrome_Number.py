# Completed June, 3 2026 | 3 minutes

class Solution:
   def isPalindrome(self, x: int) -> bool:
       x_str = str(x)
       f = len(x_str) - 1
       f_clone = f


       for idx in range(f_clone):
           if x_str[idx] != x_str[f-idx]:
               return False

       return True