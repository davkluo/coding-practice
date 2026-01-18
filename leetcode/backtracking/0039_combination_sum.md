# 39 – Combination Sum

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/combination-sum/

---

## Problem Summary
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order. The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different. It is guaranteed that the number of unique combinations that sum up to `target` is less than 150 combinations for the given input.

---

## Key Insight
- We can avoid duplicating combinations by ensuring we only consider candidates from the current index onward in our recursive calls.
- At each candidate, we have the choice to either include it (and stay at the same index) or exclude it (and move to the next index).

---

## Approach
1. Initialize an empty list `combinations` to store valid combinations.
2. Define a recursive function `backtrack(subcombination, i, target)`:
   - If `target` is 0, append a copy of `subcombination` to `combinations`.
   - If `target` is less than 0 or `i` is out of bounds, return.
   - Include the candidate at index `i`:
     - Append `candidates[i]` to `subcombination`.
     - Call `backtrack(subcombination, i, target - candidates[i])`.
     - Remove the last element from `subcombination` (backtrack).
   - Exclude the candidate at index `i`:
     - Call `backtrack(subcombination, i + 1, target)`.
3. Start the recursion with an empty `subcombination`, index `0`, and the original `target`.
4. Return the `combinations` list.

---

## Why This Works
- The backtracking approach systematically explores all potential combinations while pruning paths that exceed the target.

---

## Edge Cases
- Single candidate equal to target.
- No candidates can sum to target.

---

## Time & Space Complexity
- Time: O(n^(t/m + 1)), where `n` is the number of candidates, `t` is the target, and `m` is the minimum candidate value.
    - In the worst case, we may explore all combinations of candidates that sum up to `target`.
    - The maximum branching factor is `n`, and the maximum depth of the recursion tree is `t/m` (the maximum number of times we can use the smallest candidate to reach the target).
- Space: O(t/m), where `t` is the target and `m` is the minimum candidate value, due to the recursion stack and the space used by the current combination.
    - We can have at most `t/m` elements in the current combination at any time.

---

## Common Mistakes
- Forgetting to backtrack by removing the last added candidate after exploring that path.
- Not handling the case where candidates can be reused properly by not staying at the same index after including a candidate.

---

## Alternative Solutions
- Dynamic Programming: We can use a DP array where `dp[i]` contains all combinations that sum up to `i`. This approach builds up solutions for smaller targets to reach the final target.
    - For the recurrence relation, for each candidate `c`, we can iterate through all targets from `c` to `target` and append combinations from `dp[target - c]` to `dp[target]` with `c` added.