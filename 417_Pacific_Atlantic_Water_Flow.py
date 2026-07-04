# Completed July, 3 2026 | 104 minutes

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()
        answer = []
        cols = len(heights[0])
        rows = len(heights)
        explored = set()

        def dfs(o, col, row, prev):
            # Only add to visited if valid, if not valid, don't explore
            if 0 <= row < len(heights) and 0 <= col < len(heights[0]):
                current = heights[row][col]
                if (col, row) not in explored:
                    # If the previous will be flowed to working backwards
                    if prev <= heights[row][col]:
                        explored.add((col, row))
                        if o == "p":
                            pac.add((row, col))
                        else:
                            atl.add((row, col))

                        dfs(o, col + 1, row, current)
                        dfs(o, col - 1, row, current)
                        dfs(o, col, row + 1, current)
                        dfs(o, col, row - 1, current)
            return

        for c in range(cols):
            dfs("p", c, 0, -1)

        for r in range(rows):
            dfs("p", 0, r, -1)

        explored = set()

        for c in range(cols):
            dfs("a", c, len(heights) - 1, -1)

        for r in range(rows):
            dfs("a", cols - 1, r, -1)

        for coord in pac:
            if coord in atl:
                answer.append(coord)
        answer.sort()

        return answer