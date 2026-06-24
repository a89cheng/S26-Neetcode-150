# Completed June, 22 2026 | 45 minutes

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Must store the coordinates of the found letters in order
        seen = []

        rows = len(board)
        cols = len(board[0])

        def searcher(s_row, s_col):
            found = None

            if board[s_row][s_col] == word[len(seen)]:
                seen.append((s_row, s_col))
            else:
                return

            if len(seen) == len(word):
                return True

            # Above
            if s_row != 0 and (s_row - 1, s_col) not in seen:
                found = searcher(s_row - 1, s_col)
            # Below
            if s_row + 1 != len(board) and not found and (s_row + 1, s_col) not in seen:
                found = searcher(s_row + 1, s_col)
            # Left
            if s_col != 0 and not found and (s_row, s_col - 1) not in seen:
                found = searcher(s_row, s_col - 1)
            # Right
            if s_col + 1 != len(board[0]) and not found and (s_row, s_col + 1) not in seen:
                found = searcher(s_row, s_col + 1)
            if not found:
                seen.pop()

            return found

        for row in range(rows):
            for col in range(cols):
                # If the current letter matches the first letter...
                if board[row][col] == word[len(seen)]:
                    result = searcher(row, col)
                    if result:
                        return True

        return False