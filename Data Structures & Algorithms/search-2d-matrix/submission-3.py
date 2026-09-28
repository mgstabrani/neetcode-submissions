class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = m*n - 1
        while r >= l:
            c = l + ((r - l) // 2)
            row = c // n
            col = c % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = c - 1
            else:
                l = c + 1
        return False