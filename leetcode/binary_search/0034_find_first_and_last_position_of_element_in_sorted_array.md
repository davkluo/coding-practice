# 34 – Find First and Last Position of Element in Sorted Array

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

---

## Problem Summary

Given a non-decreasing array of integers and a target value, return the starting and ending positions of the target in the array. Return `[-1, -1]` if the target is not present.

---

## Key Insight

- Two separate binary searches: one to find the left boundary, one to find the right boundary.
- When `nums[m] == target`, record the index and keep narrowing in the boundary direction — the loop collapses to the true edge naturally.

---

## Approach

1. Run a binary search to find the start index:
   - Standard `< target` / `> target` cases move `l` or `r` as usual.
   - When `nums[m] == target`, record `m` as the current best start and set `r = m - 1` to keep searching left.
   - The loop naturally terminates when the range collapses; the last recorded value is the left boundary.
2. If start is still `-1`, return `[-1, -1]` immediately.
3. Run a second binary search for the end index, starting `l` at the known start (no need to scan before it):
   - When `nums[m] == target`, record `m` as the current best end and set `l = m + 1` to keep searching right.
   - Same natural termination — last recorded value is the right boundary.
4. Return `[start, end]`.

---

## Why This Works

- Each binary search halves the search space every iteration, so both together are still O(log n).
- When `nums[m] == target`, always recording and continuing (rather than checking the neighbor) lets the loop collapse naturally — the last recorded index is guaranteed to be the boundary.
- Starting the second search at `target_range[0]` is a safe optimization: the end position cannot be to the left of the start position.

---

## Edge Cases

- Target not in array: start search returns `-1`, short-circuit exits early.
- Single occurrence: both boundary checks fire at the same index, returning `[i, i]`.
- All elements are the target: left boundary lands at index `0`, right boundary at `len(nums) - 1`.
- Target at the very start or end of the array: the `m == 0` / `m == len(nums) - 1` guard handles the out-of-bounds neighbor check.

---

## Time & Space Complexity

- Time: O(log n) — two independent binary searches, each halving the search space
- Space: O(1) — only a few index variables used

---

## Common Mistakes

- Early-exiting on the first hit of `nums[m] == target` instead of continuing to narrow — misses the true boundary when duplicates exist.
- Reusing `l = 0` for the second search instead of `l = target_range[0]` — valid but wastes iterations on indices already known to not be the answer.

---

## Alternative Solutions

- Parameterized helper (`find_boundary(nums, target, find_left)`): same record-and-narrow logic, just with a flag to control direction — clean, but loses the `l = start` optimization for the second search without adding an extra parameter, which muddies the interface.
- Two calls to `bisect_left` / `bisect_right` from Python's `bisect` module — O(log n), concise, but relies on library knowledge.
