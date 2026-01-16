from typing import List

class Solution:
    def pacific_atlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Description:
        Given an m x n matrix of non-negative integers representing the height 
        of each unit cell in a continent, the "Pacific ocean" touches the left 
        and top edges of the matrix and the "Atlantic ocean" touches the right 
        and bottom edges. Water can only flow in four directions (up, down, 
        left, or right) from a cell to another one with height equal or lower.
        Return a list of grid coordinates where water can flow to both the 
        Pacific and Atlantic ocean.

        Example:
        pacific_atlantic([[1,2,2,3,5],
                          [3,2,3,4,4],
                          [2,4,5,3,1],
                          [6,7,1,4,5],
                          [5,1,1,2,4]]
        ) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        """
        
        m = len(heights)
        n = len(heights[0])

        flows_counter = [[0 for _col in range(n)] for _row in range(m)]

        pacific_visited = set()
        atlantic_visited = set()

        def dfs(row, col, visited):
            if (row, col) in visited:
                return
                        
            visited.add((row, col))
            flows_counter[row][col] += 1
            height = heights[row][col]

            if (row-1) >= 0 and heights[row-1][col] >= height: # north
                dfs(row-1, col, visited)
            if (row+1) < m and heights[row+1][col] >= height: # south
                dfs(row+1, col, visited)
            if (col-1) >= 0 and heights[row][col-1] >= height: # west
                dfs(row, col-1, visited)
            if (col+1) < n and heights[row][col+1] >= height: # east
                dfs(row, col+1, visited)
        
        for row in range(m):
            dfs(row, 0, pacific_visited) # left edge, pacific
            dfs(row, n-1, atlantic_visited) # right edge, atlantic
        for col in range(n):
            dfs(0, col, pacific_visited) # top edge, pacific
            dfs(m-1, col, atlantic_visited) # bottom edge, atlantic
        
        flows_into_both = []
        for row in range(m):
            for col in range(n):
                if flows_counter[row][col] == 2:
                    flows_into_both.append([row, col])

        return flows_into_both


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.pacific_atlantic([[1,2,2,3,5],
                               [3,2,3,4,4],
                               [2,4,5,3,1],
                               [6,7,1,4,5],
                               [5,1,1,2,4]]
    ) == [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    assert s.pacific_atlantic([[2,1],
                               [1,2]]
    ) == [[0,0],[0,1],[1,0],[1,1]]
    assert s.pacific_atlantic([[10,10,10],
                               [10,1,10],
                               [10,10,10]]
    ) == [[0,0],[0,1],[0,2],[1,0],[1,2],[2,0],[2,1],[2,2]]
    assert s.pacific_atlantic([[1]]) == [[0,0]]
    print("All tests passed.")