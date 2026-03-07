class Solution:
    def spiral_order(self, matrix: list[list[int]]) -> list[int]:
        """
        Description:
        Given an m x n matrix, return the elements in spiral order (clockwise).

        Example:
        spiral_order([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
        """

        traversal = []

        left = 0
        top = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1 

        while left <= right and top <= bottom:
            for j in range(left, right+1):
                traversal.append(matrix[top][j])
            top += 1

            for i in range(top, bottom+1):
                traversal.append(matrix[i][right])
            right -= 1

            if left > right or top > bottom:
                break

            for j in range(right, left-1, -1):
                traversal.append(matrix[bottom][j])
            bottom -= 1           

            for i in range(bottom, top - 1, -1):
                traversal.append(matrix[i][left])
            left += 1
        
        return traversal


if __name__ == "__main__":
    s = Solution()

    # 3x3 square matrix
    assert s.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # 3x4 wider-than-tall matrix
    assert s.spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # 4x3 taller-than-wide matrix
    assert s.spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]) == [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]

    # single row
    assert s.spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4]

    # single column
    assert s.spiral_order([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    # single element
    assert s.spiral_order([[42]]) == [42]

    # 2x2 matrix
    assert s.spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]

    print("All tests passed.")