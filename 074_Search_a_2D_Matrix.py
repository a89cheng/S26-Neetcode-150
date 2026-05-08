# Completed May, 7 2026 | 9 minutes

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        for x in range(len(matrix)):
            if target <= matrix[x][-1]:
                row = x
                break

        if row < 0:
            return False

        row = matrix[row]
        left = 0
        right = len(row) - 1

        while left != right:
            mid = (left + right) // 2

            if target <= row[mid]:
                right = mid
            else:
                left = mid + 1

        if row[left] == target:
            return True
        else:
            return False