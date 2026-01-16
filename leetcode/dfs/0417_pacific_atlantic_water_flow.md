# 417 – Pacific Atlantic Water Flow

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Depth-First Search (DFS)
**Secondary Patterns:** Graph Traversal, Matrix
**Link:** https://leetcode.com/problems/pacific-atlantic-water-flow/

---

## Problem Summary
Given an `m x n` matrix of non-negative integers representing the height of each unit cell in a continent, find all coordinates `(i, j)` such that water can flow from cell `(i, j)` to both the Pacific and Atlantic oceans. Water can only flow from a cell to its neighboring cells (up, down, left, right) if the neighboring cell's height is less than or equal to the current cell's height.

---

## Key Insight
- This is a connectivity problem with the modification that water can only flow from higher to lower or equal heights.
- Connectivity problems can be solved using graph traversal techniques like DFS or BFS.
- For each cell, we essentially do two traversals: one to check if it can reach the Pacific Ocean and another for the Atlantic Ocean.
    - This can be tallied up in a counter matrix.

---

## Approach
1. Initialize a counter matrix to keep track of how many oceans each cell can reach.
2. Define a DFS function:
    - Takes the current cell's coordinates and a visited set.
    - Marks the cell as visited and increments its count in the counter matrix.
    - Recursively calls DFS on neighboring cells that are within bounds and have heights greater than or equal to the current cell's height (because we are checking connectivity from the opposite direction of water flow).
3. Perform DFS from all cells adjacent to the Pacific Ocean (top row and left column) and mark reachable cells. Use a pacific_visited set to avoid revisiting cells.
4. Perform DFS from all cells adjacent to the Atlantic Ocean (bottom row and right column) and mark reachable cells. Use an atlantic_visited set to avoid revisiting cells.
5. Finally, collect all cells that can reach both oceans (i.e., have a count of 2 in the counter matrix).
6. Return the list of such cells.

---

## Why This Works
- DFS from each ocean's edge checks for connectivity to an ocean following the water flow rules.
- A counter value of 2 indicates that a cell can reach both oceans.

---

## Edge Cases
- Single row or single column matrices.
- Single cell matrix.
- Valley where inner cells are lower than surrounding cells.

---

## Time & Space Complexity
- Time: O(mn) – Each cell is processed a constant number of times.
- Space: O(mn) – For the visited sets and the counter matrix.
    - Recursion stack can go up to O(mn) in the worst case.

---

## Common Mistakes
- Forgetting to check bounds when accessing neighboring cells.
- Not using a visited set, leading to infinite recursion or excessive processing.
- Misinterpreting the flow direction (should check for heights greater than or equal to the current cell).
- Using an if-elif structure instead of separate if statements for exploring each direction in DFS, which can lead to missing valid paths.

---

## Alternative Solutions
- BFS can also be used with a queue instead of recursion.
- DFS can be implemented iteratively using a stack.