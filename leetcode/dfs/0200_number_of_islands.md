# 200 – Number of Islands

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Depth-First Search (DFS)
**Secondary Patterns:** Graph Traversal
**Link:** https://leetcode.com/problems/number-of-islands/

---

## Problem Summary
Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

---

## Key Insight
- Islands can be identified using DFS by exploring all connected '1's from a starting point.
- We can avoid counting the same island twice by marking visited land cells as '0' (water) during the DFS traversal.

---

## Approach
1. Initialize a counter for islands.
2. Iterate through each cell in the grid.
3. Define a DFS function that marks all connected '1's as '0's. We can use either recursion or a stack but I chose a stack.
4. When a '1' (land) is found, increment the island counter and initiate a DFS to mark all connected '1's as '0's (visited).
5. Continue until all cells have been processed.
6. Return the island counter.

---

## Why This Works
- The DFS ensures that all parts of an island are explored and marked, preventing double counting.
- The DFS traverses only the land cells connected to the starting cell, effectively isolating each island.
- Iterating through the entire grid ensures every island is found, and visited islands are not revisited.

---

## Edge Cases
- Single cell grid (either '0' or '1').
- Grid with no land ('0's only).
- Grid with all land ('1's only).
- Grid with multiple disconnected islands.

---

## Time & Space Complexity
- Time: O(M * N), where M is the number of rows and N is the number of columns in the grid. 
    - Each cell is visited at most twice (during the grid scan and during DFS).
- Space: O(M * N) in the worst case for the stack in DFS (if the grid is filled with land).

---

## Common Mistakes
- This problem uses strings ('1' and '0') instead of integers (1 and 0). Ensure to handle the data types correctly.
- Forgetting to mark visited cells, leading to overcounting islands.
- Forgetting to check boundary conditions during DFS traversal.

---

## Alternative Solutions
- Breadth-First Search (BFS) can also be used instead of DFS to explore connected land cells, but a queue would be used instead of a stack.