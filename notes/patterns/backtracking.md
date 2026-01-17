# Pattern: Backtracking

---

## When to Use
- Problems that require exploring all possible configurations or combinations, often with constraints.
- Problems where you need to build a solution incrementally and abandon solutions that fail to satisfy the constraints at any point.
- Common in puzzles, combinatorial problems, and pathfinding problems.

---

## Core Idea
- Explore all potential solutions by incrementally building candidates and reverting when a candidate cannot lead to a valid solution in order to explore other candidates.
- At any given point there is only one candidate state being maintained.

---

## Common Techniques
- Depth-First Search (DFS) to explore all possible paths or configurations.
- Backtracking by undoing the last step when a path does not lead to a solution.
- Using recursion to manage the state of the current candidate solution.
- Iterative approaches using stacks for candidate state to simulate recursion.

---

## Typical Time Complexity
- Exponential time complexity, often O(k^n), where k is the number of choices at each step and n is the depth of the recursion/tree.

---

## Common Pitfalls
- Failing to properly backtrack, leading to incorrect states.
- Not pruning invalid paths early, resulting in unnecessary computations.
- Overcomplicating the state management, making it hard to track the current candidate solution.

---

## Canonical Problems
- Word Search (LeetCode 79)