from typing import List

class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:
        """
        Description:
        Given a 2D grid map of '1's (land) and '0's (water), count the number 
        of islands. An island is formed by connecting adjacent lands 
        horizontally or vertically. You may assume all four edges of the grid 
        are surrounded by water.

        Example:
        num_islands([
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]) == 3
        """
        
        m = len(grid)
        n = len(grid[0])
        islands_count = 0

        def dfs_explore(start_row, start_col):
            stack = [(start_row, start_col)]
            while stack:
                row, col = stack.pop()
                grid[row][col] = "0"

                neighbors = ((row-1, col), (row, col-1), 
                             (row+1, col), (row, col+1))
                for nbr_row, nbr_col in neighbors:
                    if (0 <= nbr_row < m and 0 <= nbr_col < n 
                        and grid[nbr_row][nbr_col]) == "1":
                        stack.append((nbr_row, nbr_col))

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "0":
                    continue

                islands_count += 1
                dfs_explore(row, col)

        return islands_count


if __name__ == "__main__":
    s = Solution()
    assert s.num_islands([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]) == 3
    assert s.num_islands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]) == 1
    assert s.num_islands([
        ["1","0","1","0","1"],
        ["0","1","0","1","0"],
        ["1","0","1","0","1"]
    ]) == 8
    assert s.num_islands([["1"]]) == 1
    assert s.num_islands([["0"]]) == 0
    print("All tests passed.")
