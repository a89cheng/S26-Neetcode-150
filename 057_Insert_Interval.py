# Completed June, 9 2026 | 3 minutes + 30 minutes

# Method to cheese the problem using merge intervals
"""
class Solution:
   def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       first = newInterval[0]
       index = 0
       for idx in range(len(intervals)):
           if intervals[idx][0] < first:
               index = idx+1
       intervals.insert(index, newInterval)

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
"""

# A better solution that addresses the idea that the intervals are already organized
# by sorting before, merge and after the new interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        total = len(intervals)
        counter = 0

        # New interval comes later
        while counter < total and newInterval[0] > intervals[counter][1]:
            answer.append(intervals[counter])
            counter += 1

        # Some form of merge
        while counter < total and intervals[counter][0] <= newInterval[1]:
            low = min(newInterval[0], intervals[counter][0])
            high = max(newInterval[1], intervals[counter][1])
            newInterval = [low, high]
            counter += 1

        answer.append(newInterval)
        answer.extend(intervals[counter:])

        return answer