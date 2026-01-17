# 79 – Word Search

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/word-search/

---

## Problem Summary
Given a 2D board and a word, find if the word exists in the grid. The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

---

## Key Insight
- We can use DFS backtracking to explore all possible paths in the grid, which will guarantee that we find the word if it exists.
- We need to keep track of visited cells to avoid revisiting them in the same path.
- We should start the search from every cell in the grid since the starting point of the word is not predetermined.
- We can optimize the search by backtracking when a mismatch occurs
- We can optimize the search to not exceed a path longer than the word length.

---

## Approach
1. Define a recursive DFS function that takes the current position in the grid, the substring formed, and a set of used positions.
2. In the DFS function:
    - Check if the current position in the grid matches the next character in the word. If not, return False.
    - Add the current character to the substring and mark the position as used.
    - If the substring matches the word, return True.
    - Explore all four possible directions (up, down, left, right) from the current position.
        - For each valid move, recursively call the DFS function, and return True if any call returns True.
    - Backtrack by removing the current position from the used set and removing the last character from the substring.
3. Iterate through each cell in the grid and initiate the DFS from that cell.
4. If any DFS call returns True, return True. If all calls return False, return False.

---

## Why This Works
- The DFS explores all possible word-length-paths in the grid, ensuring that we do not miss any potential matches for the word.
- When a solution path is found, we short-circuit and return True immediately to propagate upwards.
- By making sure a cell matches the target character before proceeding, we avoid unnecessary exploration of invalid paths.
    - Combined with the check if the substring equals the word, this also prevents exploring paths longer than the word length.

---

## Edge Cases
- Smallest board size (1x6) with a matching word.
- Word not present in the board.
- Word uses all cells in the board.

---

## Time & Space Complexity
- Time: O(m * n * 4^L), where m and n are the dimensions of the board and L is the length of the word.
    - We perform DFS on each cell, which contributes the m*n factor.
    - For each cell, we expand in 4 directions for each character in the word, leading to the 4^L factor.
- Space: O(L), where L is the length of the word.
    - The recursion stack can go as deep as the length of the word.
    - The same goes for the substring and used set.

---

## Common Mistakes
- Forgetting to run DFS from every cell in the grid.
- Not properly backtracking by removing the current cell from the used set and the last character from the substring.
- Off by one errors when checking character matches.
- Incorrectly calling DFS before the current cell is added to the substring and used set, leading to reusing cells.

---

## Alternative Solutions
- Iterative DFS using a stack instead of recursion.
    - Break from loop when word is found, or set a flag variable
- Iterative BFS using a queue, exploring a radius of the word length from each starting cell
    - Break from loop when word is found, or set a flag variable, as above