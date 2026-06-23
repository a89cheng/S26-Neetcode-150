# Completed June, 20 2026 | 18 minutes

class Solution:
   def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       results = []
       candidates.sort()
       current = []


       def consider(start):
           # If target hit or surpassed, return
           if sum(current) == target:
               results.append(current[:])
               return
           elif sum(current) > target:
               return


           # Goal of searching every combination by idx
           for idx in range(start, len(candidates)):
               current.append(candidates[idx])
               consider(idx)
               current.pop()


       consider(0)
       return results

