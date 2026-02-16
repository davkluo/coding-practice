# 416 – Partition Equal Subset Sum

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Link:** https://leetcode.com/problems/partition-equal-subset-sum/

---

## Problem Summary

Given an integer array `nums`, return `True` if you can partition the array into two subsets such that the sum of elements in both subsets is equal, and `False` otherwise.

---

## Key Insight

- The problem reduces to a 0/1 knapsack: can we select a subset of `nums` that sums to exactly `total_sum // 2`?
- If the total sum is odd, it's immediately impossible to split evenly.

---

## Approach

Both approaches share the same setup:

1. Compute `total_sum`. If it's odd, return `False`.
2. Set `target_sum = total_sum // 2`.

### 2D DP

3. Build a boolean table `dp[i][b]` where `i` is the number of items considered and `b` is the target sub-sum.
4. Base cases: `dp[i][0] = True` for all `i` (zero sum is always achievable); `dp[0][b] = False` for `b > 0` (no items means no positive sum).
5. Recurrence: `dp[i][b] = dp[i-1][b] OR (dp[i-1][b - nums[i-1]]` if `nums[i-1] <= b)`. Either skip the current number or include it if it fits inside the sub-sum.
6. Return `dp[len(nums)][target_sum]`.

### 1D DP

3. Initialize `dp = [True] + [False] * target_sum`.
4. For each `num` in `nums`, iterate `b` from `target_sum` down to `num`: `dp[b] = dp[b] OR dp[b - num]`.
5. Return `dp[target_sum]`.

---

## Why This Works

### 2D DP

- Each number is either included or excluded (0/1 knapsack), and the table tracks all achievable sums using the first `i` numbers.
- If we can form a subset summing to `target_sum`, the remaining elements must also sum to `target_sum` since the total is `2 * target_sum`.

### 1D DP

- Each row `i` only depends on the previous row `i-1`, so we can overwrite a single array in place.
- Iterating `b` backwards ensures we read from the "previous row" values (not yet overwritten), preserving the 0/1 property that each number is used at most once.
- We only read from values in the row to the left of the current `b`, since we subtract the value of the number if we take it. This is why iterating backwards doesn't read newly written values.

---

## Edge Cases

- Odd total sum (immediately `False`)
- Single element (always `False`)
- All elements equal (depends on whether count is even)

---

## Time & Space Complexity

### 2D DP

- Time: O(n \* target_sum), where n is the number of elements.
- Space: O(n \* target_sum)

### 1D DP

- Time: O(n \* target_sum)
- Space: O(target_sum)

---

## Common Mistakes

### 2D DP

- Off-by-one errors with the `i` index — `dp[i]` considers the first `i` numbers, so the current number is `nums[i-1]`, not `nums[i]`.

### 1D DP

- Iterating `b` forwards instead of backwards. This allows a single number to be "used" multiple times within the same pass, effectively turning the 0/1 knapsack into an unbounded knapsack.
