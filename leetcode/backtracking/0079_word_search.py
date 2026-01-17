from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Description:
        Given an m x n grid of characters board and a string word, return true 
        if word exists in the grid. The word can be constructed from letters of 
        sequentially adjacent cells, where adjacent cells are horizontally or 
        vertically neighboring. The same letter cell may not be used more than 
        once.

        Example:
        exist([
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ], "ABCCED") == True
        """

        m = len(board)
        n = len(board[0])
        
        def dfs(row, col, substr, used=set()):
            next_match_idx = len(substr)  
            if board[row][col] != word[next_match_idx]: # failed path
                return False         

            substr += board[row][col]
            used.add((row, col))
            if substr == word:
                return True
                        
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c = row+dr, col+dc
                if 0 <= r < m and 0 <= c < n and (r, c) not in used:
                    if dfs(r, c, substr, used):
                        return True

            used.remove((row, col))
            substr = substr[:-1]
            return False

        for row in range(m):
            for col in range(n):
                if dfs(row, col, ""):
                    return True

        return False


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "ABCCED") == True
    assert s.exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "SEE") == True
    assert s.exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "ABCB") == False
    assert s.exist([
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"]
    ], "A") == True
    assert s.exist([["y", "e", "l", "l", "o", "w"]], "yellow") == True
    print("All tests passed.")