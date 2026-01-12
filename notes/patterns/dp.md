# Pattern: Dynamic Programming (DP)

---

## When to Use
- Overlapping subproblems
- Optimal substructure
- Problems that can be broken down into simpler subproblems

---

## Core Idea
- Store results of subproblems to avoid redundant computations.
- Build solutions to larger problems using solutions to smaller problems.

---

## Common Techniques
- Memoization (top-down)
- Tabulation (bottom-up)
- Accumulating results in a single variable when possible

---

## Typical Time Complexity
- Dependent on the problem, often O(n^2) or O(n*m) for 2D problems, O(n) for 1D problems.

---

## Common Pitfalls
- Not identifying overlapping subproblems
- Excessive memory usage
- Incorrect base cases

---

## Canonical Problems
- Fibonacci sequence
- Knapsack problem
- Longest Common Subsequence (LCS)
- Coin Change problem
- Edit Distance