# Completed July, 21 2026 | 72 minutes

class Solution:
   def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       # Node, 2nd Node, Time it takes
       # n is the number of nodes, k is the starting node


       # For the sake of a 1:1 index-list relationship
       clock = [float("inf") for x in range(n+1)]
       clock[k] = clock[0] = 0


       seen = set()


       node = 1
       for iterations in range(n):
           shortest = float("inf")


           for index in range(1, n+1):
               if index not in seen and clock[index] < shortest:
                   shortest = clock[index]
                   node = index


           seen.add(node)
           clock[node] = shortest


           for group in times:
               if group[0] not in seen:
                   continue


               if clock[group[1]] > group[2] + clock[node]:
                   clock[group[1]] = group[2] + clock[node]


       answer = max(clock[1:])


       if answer == float("inf"):
           return -1


       return answer