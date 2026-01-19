# 46 – Permutations

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/permutations/

---

## Problem Summary
Given an array of distinct integers, return all possible permutations. You can return the answer in any order.

---

## Key Insight
- Each permutation can be built incrementally by choosing each unused number at each step.
- Backtracking allows us to explore all possible configurations without exploding memory usage.

---

## Approach
1. Initialize an empty list to store the permutations.
2. Define a backtracking function:
    - Takes the current permutation being built and a list of booleans indicating which numbers have been used.
    - If the current permutation's length equals the input array's length, append a copy of it to the results.
    - Iterate through the input numbers:
        - If a number hasn't been used, mark it as used, add it to the current permutation, and recursively call the backtracking function.
        - After returning from recursion, backtrack by removing the last number and marking it as unused.
3. Start the backtracking process with an empty permutation and all numbers marked as unused.
4. Return the list of permutations.

---

## Why This Works
- The backtracking approach systematically explores all possible arrangements by making choices at each step and reverting those choices to explore other possibilities.

---

## Edge Cases
- Single element array (e.g., [1])

---

## Time & Space Complexity
- Time: O(n! * n) where n is the number of elements in the input array. There are n! permutations and generating each permutation takes O(n) time.
    - Generating the permutation refers to making a copy of the current permutation to store in the results.
- Space: O(n! * n) for storing all permutations, each of length n.

---

## Common Mistakes
- Forgetting to backtrack properly by not marking numbers as unused after exploring a path.
- Not starting all numbers as available

---

## Alternative Solutions
- Iterative approach using Heap's algorithm
    - Fixes a suffix and permutes the prefix iteratively using swaps.
    - The elements swapped is governed by whether the prefix length is even or odd.