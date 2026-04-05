class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M = len(matrix)
        N = len(matrix[0])

        if target > matrix[-1][-1] or target < matrix[0][0]: 
            return False

        low = 0
        high = M * N - 1

        while (low <= high):
            mid = (low + high) // 2
            print(mid)

            row = mid // N
            col = mid % N
            print(f"row: {mid // N}")
            print(f"col: {mid % N}")
            if target > matrix[row][col]:
                low  = mid + 1
            elif target == matrix[row][col]:
                return True
            else:
                high = mid - 1
        return False