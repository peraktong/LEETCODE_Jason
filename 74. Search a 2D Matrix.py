class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search
        r = len(matrix)
        if r == 0:
            return False
        c = len(matrix[0])
        left, right = 0, r * c - 1
        while left <= right:
            pivot_index = (left + right) // 2
            pivot_element = matrix[pivot_index // c][pivot_index % c]
            if target == pivot_element:
                return True
            else:
                if target < pivot_element:
                    right = pivot_index - 1
                else:
                    left = pivot_index + 1
        return False
