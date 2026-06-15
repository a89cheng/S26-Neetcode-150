# Completed June 10, 2026 | 19 minutes

class Solution:
   def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
       intervals.sort()
       count = 0
       previous = 0

       for idx in range(1,len(intervals)):
           if intervals[previous][1] > intervals[idx][0]:
               if intervals[previous][1] > intervals[idx][1]:
                   previous = idx
               count += 1
           else:
               previous = idx

       return count