# 300 – Longest Increasing Subsequence

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Secondary Patterns:** Binary Search
**Link:** https://leetcode.com/problems/longest-increasing-subsequence/

---

## Problem Summary

Given an integer array `nums`, return the length of the longest strictly increasing subsequence.

---

## Key Insight

- For the DP approach: if we know the LIS ending at every index before `i`, then the LIS ending at `i` is simply `1 + max(dp[j])` for all `j < i` where `nums[j] < nums[i]`.
- For the binary search approach: we don't need to track the actual subsequence. Instead, maintain the smallest possible tail element for increasing subsequences of each length. This lets us use binary search to decide whether to extend or replace.

---

## Approach

### O(n^2) DP

1. Create a `dp` array where `dp[i]` represents the length of the LIS ending at index `i` (including `nums[i]`).
2. For each index `i`, check all previous indices `j < i`:
   - If `nums[i] > nums[j]`, then `nums[i]` can extend the subsequence ending at `j`, so update `dp[i] = max(dp[i], dp[j] + 1)`.
   - Otherwise, `dp[i]` is at least `1` (the element itself).
3. Return `max(dp)`.

### O(n log n) Binary Search (Patience Sorting)

1. Maintain a list `buckets` representing the smallest tail element for increasing subsequences of each length.
2. For each number in `nums`:
   - If it's larger than every element in `buckets`, append it (extends the longest subsequence found so far).
   - Otherwise, binary search for the leftmost element in `buckets` that is >= the current number, and replace it (keeps the tails as small as possible to allow for longer future subsequences).
3. Return `len(buckets)`.

---

## Why This Works

### DP

- The recurrence `dp[i] = max(dp[j] + 1) for all j < i where nums[j] < nums[i]` exhaustively considers every valid preceding element. By taking the max over all `dp[i]`, we guarantee the global optimum.

### Binary Search

- `buckets[k]` always holds the smallest possible tail of an increasing subsequence of length `k + 1`. When we encounter a smaller element, replacing it in `buckets` doesn't change the current LIS length but opens up more opportunities for future elements to extend the sequence. Since `buckets` is always sorted, binary search efficiently finds the correct position.

---

## Edge Cases

- Single element array — LIS is `1`.
- All elements are the same (`[7, 7, 7]`) — LIS is `1` since the subsequence must be strictly increasing.
- Already sorted in increasing order — LIS is the full array length.
- Sorted in decreasing order — LIS is `1`.

---

## Time & Space Complexity

### DP

- Time: O(n^2), two nested loops over the array.
- Space: O(n), for the `dp` array.

### Binary Search

- Time: O(n log n), one pass through the array with a binary search at each step.
- Space: O(n), for the `buckets` array.

---

## Common Mistakes

- Forgetting that the subsequence must be **strictly** increasing (using `>=` instead of `>` when comparing elements).
- In the DP approach, forgetting to initialize each `dp[i]` to at least `1` (every element is a subsequence of length 1 by itself).
- In the binary search approach, confusing the contents of `buckets` with the actual LIS. The `buckets` array gives the correct **length** but does not necessarily contain the actual subsequence.

---

## Alternative Solutions

- **Top-down DP with memoization:** Recursive approach where `dfs(i)` returns the LIS starting at index `i`. Same O(n^2) complexity as bottom-up but with recursion overhead.
