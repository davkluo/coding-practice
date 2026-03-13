# 1493 – Longest Subarray of 1's After Deleting One Element

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

---

## Problem Summary

Given a binary array, return the length of the longest subarray of 1s you can obtain by deleting exactly one element. Exactly one element must always be deleted.

---

## Key Insight

- Maintain a sliding window `(l, r]` that allows at most one deleted 0. Track where that deletion sits (`deleted_idx`) so the left boundary can jump past it when a second 0 enters the window.
- The count of 1s in the window is `(r - l) - 1` when a deletion has been used, since one slot in the window is occupied by the deleted element.

---

## Approach

1. Initialize `l = -1` (exclusive left boundary), `has_used_delete = False`, `deleted_idx = None`, `longest_ones = 0`.
2. For each index `r`:
   - If `nums[r] == 1`: compute `ones_length = (r - l) - (1 if has_used_delete else 0)`, update `longest_ones`, and continue.
   - If `nums[r] == 0` and delete not yet used: set `has_used_delete = True`, record `deleted_idx = r`.
   - If `nums[r] == 0` and delete already used: slide `l = deleted_idx` (old deleted 0 exits the window), then record `deleted_idx = r`.
3. If `longest_ones == len(nums)` (all 1s, deletion never forced), return `longest_ones - 1`. Otherwise return `longest_ones`.

---

## Why This Works

- `l` is an exclusive boundary, so the window contains indices `(l, r]` with `r - l` total elements.
- Allowing exactly one 0 in the window means the 1-count is the window size minus that one deleted slot.
- When a second 0 arrives, moving `l` to the previous `deleted_idx` evicts everything up to and including the old 0, restoring the one-deletion budget for the new 0.
- The all-1s case requires a special check because the loop never triggers the deletion logic, yet the problem mandates exactly one deletion.
- Checking if `longest_ones < len(nums)` is a sufficient check for the required deletion. So long as the longest sequence of 1s is shorter than the full array, even if a delete was not used in the longest sequence, we can choose one of the elements not in the longest sequence to delete.

---

## Edge Cases

- All 1s — deletion is mandatory; return `len(nums) - 1`.
- All 0s — no 1s exist regardless of which element is deleted; return 0.
- Single element — whether 0 or 1, deleting it leaves an empty subarray; return 0.
- One 0 at the boundary (start or end) — the window spans all 1s on the other side plus the deleted 0.

---

## Time & Space Complexity

- Time: O(n) — single pass, `l` only moves forward
- Space: O(1) — a fixed number of variables

---

## Common Mistakes

- Forgetting the all-1s edge case: if no 0 was ever encountered, `longest_ones` equals the full array length, but exactly one element must be deleted, so the answer is `longest_ones - 1`.
- Miscomputing `ones_length`: the window `(l, r]` has `r - l` elements, but one of those is the deleted 0 when `has_used_delete` is true — forgetting to subtract 1 overcounts.
- Off-by-one when sliding `l`: because `l` is an exclusive boundary, setting `l = deleted_idx` means the window starts at `deleted_idx + 1`, which correctly excludes the old deleted 0. Writing `l = deleted_idx + 1` instead would skip the element right after that 0, shrinking the window unnecessarily.

---

## Alternative Solutions

- **Zero-count sliding window**: track `zeros_in_window`; when it exceeds 1, advance `l` until a 0 exits. Answer is `r - l - 1` at the end (window size minus the mandatory deletion). Simpler to reason about and a more idiomatic sliding window pattern.
