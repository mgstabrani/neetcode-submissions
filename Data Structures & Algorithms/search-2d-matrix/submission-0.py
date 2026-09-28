class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                r = len(matrix[i]) - 1
                l = 0

                while r >= l:
                    c = l + ((r - l) // 2)
                    if matrix[i][c] == target:
                        return True
                    elif matrix[i][c] > target:
                        r = c - 1
                    else:
                        l = c + 1
                    
            else:
                continue
        return False