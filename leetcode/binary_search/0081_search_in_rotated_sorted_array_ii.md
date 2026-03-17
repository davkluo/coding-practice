# 81 – Search in Rotated Sorted Array II

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

---

## Problem Summary

Given an array sorted in non-decreasing order, possibly rotated at an unknown pivot, with possible duplicates and a target value, return true if the target exists in the array, false otherwise.

---

## Key Insight

- Like problem 33, one half of the array is always sorted — but duplicates can make it impossible to determine which half when `nums[l] == nums[m]` or `nums[r] == nums[m]`, since there could be a concavity at the pivot.
- When the endpoint equals `nums[m]`, the only safe move is to shrink that endpoint inward by 1, accepting O(n) worst case.
- The early `nums[m] == target` check is the safety net that makes shrinking safe: if the endpoint were the target, it would have been caught already.

---

## Approach

1. Initialize `l = 0`, `r = len(nums) - 1`.
2. While `l <= r`:
   - Compute `m = (l + r) // 2`.
   - If `nums[m] == target`, return `True`.
   - If `nums[m] > target` (target is to the left of mid if it exists in the left half):
     - If `nums[l] <= target` (target in sorted left range) OR `nums[l] > nums[m]` (rotation is in left half, so right half is sorted and target can't be there) → `r = m - 1`.
     - Elif `nums[l] == nums[m]` (can't determine which side is sorted) → `l += 1`.
     - Else (left is sorted but target is below `nums[l]`) → `l = m + 1`.
   - If `nums[m] < target` (symmetric):
     - If `nums[r] >= target` OR `nums[r] < nums[m]` → `l = m + 1`.
     - Elif `nums[r] == nums[m]` → `r -= 1`.
     - Else → `r = m - 1`.
3. Return `False`.

---

## Why This Works

- In the no-duplicate case, comparing `nums[l]` or `nums[r]` to `nums[m]` always identifies the sorted half, allowing us to eliminate one half confidently.
- When `nums[l] == nums[m]`, we genuinely can't determine which side is sorted. Incrementing `l` is safe because `nums[l] != target` (guaranteed by the earlier `nums[m] == target` check) and only shrinks the window by 1 — making eventual progress inevitable.
- The same invariant applies symmetrically to `nums[r] == nums[m]`.

---

## Edge Cases

- Single element array where the element is or isn't the target.
- All elements are the same value (e.g. `[1, 1, 1, 1]`) — degrades to O(n).
- Target at the boundary obscured by duplicates (e.g. `[1, 0, 1, 1, 1]`, target `0`).

---

## Time & Space Complexity

- Time: O(log n) average, O(n) worst case — duplicates can force single-step shrinking every iteration
- Space: O(1)

---

## Common Mistakes

- Forgetting the `nums[l] == nums[m]` (and symmetric right) case, causing incorrect elimination of the half containing the target.
- Trying to avoid the O(n) worst case — it is unavoidable with duplicates; the problem's follow-up explicitly asks about this tradeoff.
- Using the exact same approach as problem 33 without accounting for duplicates, leading to incorrect results since binary search relies on a strictly increasing or decreasing order to eliminate halves.

---

## Alternative Solutions

- Linear scan is O(n) and trivially correct, but defeats the purpose of binary search.
