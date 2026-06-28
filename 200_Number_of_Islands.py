# Completed June, 27 2026 | 31 minutes

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        counter = 0

        def explorer(row, col):
            if grid[row][col] == "0":
                return
            if (row, col) not in visited:
                visited.add((row, col))
            else:
                return

            if row != 0:
                explorer(row - 1, col)
            if row != len(grid) - 1:
                explorer(row + 1, col)
            if col != 0:
                explorer(row, col - 1)
            if col != len(grid[0]) - 1:
                explorer(row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                current = grid[row][col]
                if (row, col) not in visited and current == "1":
                    explorer(row, col)
                    counter += 1

        return counter