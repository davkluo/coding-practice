from typing import List

class Solution:
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Description:
        Write an efficient algorithm that searches for a value in an m x n 
        matrix where integers in each row are sorted from left to right, and the 
        first integer of each row is greater than the last integer of the 
        previous row. Return true if the target is found in the matrix, and 
        false otherwise.

        Example:
        search_matrix([[1, 3, 5, 7],
                       [10, 11, 16, 20],
                       [23, 30, 34, 50]], 3) == True
        """

        m, n = len(matrix), len(matrix[0])
        l = 0
        r = m * n - 1

        while l <= r:
            mid = (l + r) // 2
            mid_row = mid // n
            mid_col = mid % n

            mid_val = matrix[mid_row][mid_col]
            if mid_val == target:
                return True
            elif mid_val > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.search_matrix([[1, 3, 5, 7],
                            [10, 11, 16, 20],
                            [23, 30, 34, 50]], 3) == True
    assert s.search_matrix([[1, 3, 5, 7],
                            [10, 11, 16, 20],
                            [23, 30, 34, 50]], 13) == False
    assert s.search_matrix([[1]], 1) == True
    assert s.search_matrix([[1, 2, 3, 4, 5]], 4) == True
    assert s.search_matrix([[1], [3], [5]], 2) == False
    print("All tests passed.")