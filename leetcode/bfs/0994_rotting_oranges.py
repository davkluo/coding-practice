from typing import List
from collections import deque

class Solution:
    def oranges_rotting(self, grid: List[List[int]]) -> int:
        """
        Description:
        Given a 2D grid, each cell can have one of three values:
        - the value 0 representing an empty cell,
        - the value 1 representing a fresh orange, or
        - the value 2 representing a rotten orange.
        Every minute, any fresh orange that is adjacent (4-directionally) to a 
        rotten orange becomes rotten. Return the minimum number of minutes that 
        must elapse until no cell has a fresh orange, or -1 if this never 
        happens.

        Example:
        oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
        """
        
        num_fresh_remaining = 0
        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    num_fresh_remaining += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
        
        if num_fresh_remaining == 0:
            return 0
        
        time_elapsed = 0

        while queue:
            time_elapsed += 1

            for _ in range(len(queue)):
                i, j = queue.popleft()

                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for r, c in neighbors:
                    if (0 <= r < len(grid) and 0 <= c < len(grid[0]) 
                        and grid[r][c] == 1):
                        grid[r][c] = 2
                        num_fresh_remaining -= 1
                        queue.append((r, c))

                    if num_fresh_remaining == 0:
                        return time_elapsed

        return -1


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.oranges_rotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert s.oranges_rotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert s.oranges_rotting([[0,2]]) == 0
    print("All tests passed.")