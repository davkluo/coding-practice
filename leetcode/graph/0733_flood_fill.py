from typing import List

class Solution:
    def flood_fill(self, image: List[List[int]], 
                   sr: int, sc: int, color: int) -> List[List[int]]:
        """
        Description:
        Given a 2D array representing an image, a starting pixel (sr, sc), and a 
        new color, replace the color of the starting pixel and all adjacent 
        pixels that share its color with the new color.

        Example:
        flood_fill([[1,1,1],
                    [1,1,0],
                    [1,0,1]],
                   1, 1, 2)
        == [[2,2,2],
            [2,2,0],
            [2,0,1]]
        """

        old_color = image[sr][sc]

        if old_color == color:
            return image

        visited = set()
        stack = [(sr, sc)]

        while stack:
            r, c = stack.pop()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            image[r][c] = color

            if r > 0 and image[r-1][c] == old_color:
                stack.append((r-1, c))
            if r < len(image)-1 and image[r+1][c] == old_color:
                stack.append((r+1, c))
            if c > 0 and image [r][c-1] == old_color:
                stack.append((r, c-1))
            if c < len(image[0])-1 and image[r][c+1] == old_color:
                stack.append((r, c+1))
        
        return image


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.flood_fill([[1,1,1],
                         [1,1,0],
                         [1,0,1]],
                        1, 1, 2) == [[2,2,2],
                                     [2,2,0],
                                     [2,0,1]]
    assert s.flood_fill([[0,0,0],
                         [0,1,1]],
                        1, 1, 1) == [[0,0,0],
                                     [0,1,1]]
    assert s.flood_fill([[1]],
                        0, 0, 2) == [[2]]
    print("All tests passed.")