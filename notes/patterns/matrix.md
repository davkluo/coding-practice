# Pattern: Matrix

---

## When to Use
- The input is a 2D grid and the problem involves traversal, boundary tracking, or spatial relationships.
- You need to process elements in a specific order (spiral, layer-by-layer, directional).
- You need to search, mark, or propagate values across adjacent cells.

---

## Core Idea
Represent the grid with boundary pointers or direction vectors, and reduce the problem to a sequence of linear passes or neighbor expansions.

---

## Common Techniques
- **Shrinking boundaries**: Maintain `left`, `right`, `top`, `bottom` pointers and collapse them inward after each pass. Used for layer-by-layer or spiral traversal.
- **Direction vectors**: Define `dirs = [(0,1),(0,-1),(1,0),(-1,0)]` and iterate over neighbors. Used for flood fill, BFS/DFS spreading, and reachability problems.
- **In-place visited marking**: Mutate cell values (e.g., set to 0 or a sentinel) to avoid a separate `visited` set. Restore if needed after backtracking.
- **2D binary search**: For a row-sorted and column-sorted matrix, start at the top-right corner and eliminate a row or column per step — O(m + n).

---

## Typical Time Complexity
- O(m * n) for full traversal — each cell visited once.
- O(m + n) for sorted-matrix search via corner elimination.

---

## Common Pitfalls
- Off-by-one on boundary ranges (e.g., `range(left, right+1)` vs `range(left, right)`).
- Forgetting a mid-loop guard when traversing in pairs — after consuming a row or column, the complementary pass in the same iteration can re-traverse already-covered cells.
- Not checking bounds before accessing neighbors in direction-vector traversal.
- Mutating cells in-place for visited tracking without restoring them when backtracking is required.

---

## Canonical Problems
- Spiral Matrix (LeetCode 54)
- Search a 2D Matrix (LeetCode 74)
