class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #m = len(matrix), # no of rows in matrix
        #n = len(matrix[0]) #no of cols
        m, n = len(matrix), len(matrix[0])

        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            num = matrix[row][col]
            
            if num == target:
                return True
            
            if num < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False