# Completed June, 27 2026 | 25 minutes

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        most = 0
        visited = set()

        def mapper(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or (grid[row][col] == 0 or (row, col) in visited):
                return 0

            left = right = up = down = 0
            visited.add((row, col))

            left = mapper(row - 1, col)
            right = mapper(row + 1, col)
            down = mapper(row, col + 1)
            up = mapper(row, col - 1)

            return 1 + left + right + up + down

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    area = mapper(row, col)
                    most = max(most, area)

        return most