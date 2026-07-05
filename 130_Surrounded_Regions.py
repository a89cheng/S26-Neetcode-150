# Completed July, 4 2026 | 54 minutes

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Within border:
        # if 0 < row < len(board)-1 and 0 < col < len(board[0])-1:

        safes = set()

        def explorer(row, col):
            # No repeats!
            if (row, col) in safes:
                return
            # Only proceed if even within the board!
            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                return
            # Only proceed if it's the same type!
            if board[row][col] != 'O':
                return

            # Add it to the connection!
            safes.add((row, col))

            # Left, Right, Up, Down
            explorer(row, col - 1)
            explorer(row, col + 1)
            explorer(row - 1, col)
            explorer(row + 1, col)

        # Explore only the crust!
        for tops in range(len(board[0])):
            explorer(0, tops)

        for bots in range(len(board[0])):
            explorer(len(board) - 1, bots)

        for left in range(1, len(board)):
            explorer(left, 0)

        for right in range(1, len(board)):
            explorer(right, len(board[0]) - 1)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) not in safes and board[row][col] != 'X':
                    board[row][col] = 'X'