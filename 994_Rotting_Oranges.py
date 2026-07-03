# Completed July, 2 2026 | 27 minutes

class Solution:
   def orangesRotting(self, grid: List[List[int]]) -> int:
       from collections import deque

       rotten = deque([])
       clean = 0

       for row in range(len(grid)):
           for col in range(len(grid[0])):
               # If it's rotten, mark it
               if grid[row][col] == 2:
                   rotten.append((row,col))
               # If it's clean, count it
               elif grid[row][col] == 1:
                   clean += 1


       def checker(row,col):
           if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
               nonlocal clean
               if grid[row][col] == 1:
                   rotten.append((row,col))
                   grid[row][col] = 2
                   clean -= 1

       time = 0

       while rotten:
           itr = len(rotten)
           for times in range(itr):
               current = rotten.popleft()
               row,col = current[0],current[1]
               checker(row,col-1), checker(row,col+1), checker(row+1,col), checker(row-1,col)
           if rotten:
               time += 1

       if not clean:
           return time
       return -1