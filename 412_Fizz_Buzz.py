# Completed April, 21 2026 | 5 minutes

class Solution:
   def fizzBuzz(self, n: int) -> List[str]:
       output = []


       for i in range(1,n+1):
           if not(i % 15):
               word = "FizzBuzz"
           elif not(i % 3):
               word = "Fizz"
           elif not(i % 5):
               word = "Buzz"
           else:
               word = str(i)
           output.append(word)
       return output