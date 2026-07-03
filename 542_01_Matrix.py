# Completed July, 2 2026 | 45.5 minutes

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import deque

        solution = [[0] * len(mat[0]) for _ in range(len(mat))]
        queue = deque([])

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if not mat[row][col]:
                    queue.append((row, col))

        def bfs(row, col, wave):
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and (mat[row][col] == 1 and not solution[row][col]):
                queue.append((row, col))
                solution[row][col] = wave

        wave = 1
        while queue:
            itr = len(queue)
            for _ in range(itr):
                coord = queue.popleft()
                row, col = coord[0], coord[1]
                bfs(row + 1, col, wave)
                bfs(row - 1, col, wave)
                bfs(row, col + 1, wave)
                bfs(row, col - 1, wave)
            wave += 1

        return solution