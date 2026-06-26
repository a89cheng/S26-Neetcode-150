# Completed June, 24 2026 | 48 minutes

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        coords = []
        board = []
        columns = []

        # Shouldn't be too crazy; we know each row, col can only have one... but mainly row
        def chessify(board):
            orientation = []
            for coord in board:
                orientation.append("." * coord[1] + "Q" + "." * (n - coord[1] - 1))

            return orientation

        # Check whether a square is legal for a queen
        def legality(r, c):
            for coord in board:
                if c in columns or abs(coord[0] - r) == abs(coord[1] - c):
                    return False
            return True

        # For simplicity sake, let's say top left is (0,n) or a'n'
        def diver(row):
            if len(board) == n:
                coords.append(board[:])
                return

            for col in range(n):
                if legality(row, col):
                    board.append((row, col)), columns.append(col)
                    diver(row + 1)
                    board.pop(), columns.pop()

        # Main block
        positions = []
        diver(0)
        for board in coords:
            positions.append(chessify(board))

        return positions