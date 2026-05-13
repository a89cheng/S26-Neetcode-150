# Completed May 13, 2026 | 28 minutes

class Solution:
   def dailyTemperatures(self, temperatures:
           List[int]) -> List[int]:
       stack = [0]
       #Smart way of initializing with 0s
       results = [0] * len(temperatures)

       #Interesting way of storing indices instead of temps
       for day in range(1,len(temperatures)):
           if stack:
               while temperatures[day] > temperatures[stack[-1]]:
                   results[stack[-1]] = day - stack[-1]
                   stack.pop(-1)
                   if not stack:
                       break

           stack.append(day)

       return results