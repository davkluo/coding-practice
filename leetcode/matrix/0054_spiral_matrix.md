# 54 – Spiral Matrix

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Matrix / Shrinking Boundaries
**Link:** https://leetcode.com/problems/spiral-matrix/

---

## Problem Summary

Given an m x n matrix, return all elements in clockwise spiral order.

---

## Key Insight

- Maintain four boundary pointers (`left`, `right`, `top`, `bottom`) and shrink them inward after each directional pass.
- Group the four passes into two pairs: (top row + right column) and (bottom row + left column). Each pair is safe to execute together without an intermediate check — the second pass in each pair will naturally do 0 iterations if the boundary has collapsed.
- A single guard between the two pairs is sufficient to prevent re-traversal.

---

## Approach

1. Initialize `left=0`, `right=len(matrix[0])-1`, `top=0`, `bottom=len(matrix)-1`.
2. While `left <= right and top <= bottom`:
   - Traverse the top row left to right; increment `top`.
   - Traverse the right column top to bottom; decrement `right`.
   - If `left > right or top > bottom`, break.
   - Traverse the bottom row right to left; decrement `bottom`.
   - Traverse the left column bottom to top; increment `left`.

---

## Why This Works

- The while condition guarantees both dimensions are valid at the start of each iteration.
- Within a pair (e.g. top row + right column), the second pass self-protects: if the first pass consumed the last row (`top > bottom`), `range(top, bottom+1)` is empty and does nothing.
- The mid-loop guard is placed between the two pairs — not after each individual pass — because it needs to prevent the bottom row and left column passes from re-traversing already-covered cells. One guard covers both potential offenders.

---

## Edge Cases

- Single row: top row consumed in the first pass; right column is empty; guard fires; done.
- Single column: right column consumed in the second pass; guard fires; done.
- Single element: while condition passes once, top row traversal picks it up, guard fires.
- Non-square (wider or taller): boundary math handles this naturally.

---

## Time & Space Complexity

- Time: O(m * n) — every element is visited exactly once.
- Space: O(1) auxiliary — output list excluded.

---

## Common Mistakes

- Placing a guard after every individual pass instead of once between the two pairs — unnecessary branching.
- Omitting the mid-loop guard entirely — causes re-traversal of already-covered rows or columns when a boundary collapses mid-iteration.

---

## Alternative Solutions

- **Direction vector rotation:** Maintain a current direction `(dr, dc)` and rotate 90 degrees clockwise when the next cell is out of bounds or already visited. Requires a `visited` matrix or in-place mutation — O(m * n) space.
- **Layer-by-layer recursion:** Peel one outer ring per recursive call. Cleaner conceptually but adds call stack overhead.
