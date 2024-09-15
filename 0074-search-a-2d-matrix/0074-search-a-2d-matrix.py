class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            i, j = divmod(mid,n)

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
        