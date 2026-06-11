# Completed June, 9 2026 | 10 minutes

class Solution:
   def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       intervals.sort()
       answer = []

       # Represents a set of time
       previous = intervals[0]

       for pair in range(1,len(intervals)):
           if intervals[pair][0] <= previous[1]:
               previous = [previous[0], max(intervals[pair][1], previous[1])]
           else:
               answer.append(previous)
               previous = intervals[pair]
       answer.append(previous)

       return answer