# 75 – Sort Colors

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Two Pointers
**Link:** https://leetcode.com/problems/sort-colors/

---

## Problem Summary

Given an array of integers where each value is 0, 1, or 2 (representing red, white, and blue), sort the array in-place so that all 0s come first, then 1s, then 2s.

---

## Key Insight

- Use three regions: a settled-0s region on the left, a settled-2s region on the right, and an unsorted middle.
- A single pass with two boundary pointers and a scan pointer partitions the array in O(n) time and O(1) space — this is the Dutch National Flag algorithm.

---

## Approach

1. Initialize `swap_r = 0` (next position for a 0) and `swap_b = len(nums) - 1` (next position for a 2).
2. Walk `i` from 0 while `i <= swap_b`:
   - If `nums[i] == 0`: swap `nums[i]` with `nums[swap_r]`, increment `swap_r`, and set `i = swap_r` (everything before `swap_r` is finalized).
   - If `nums[i] == 2`: swap `nums[i]` with `nums[swap_b]`, decrement `swap_b`. Do **not** advance `i` — the swapped-in value is unseen and needs to be checked.
   - If `nums[i] == 1`: just increment `i`.

---

## Why This Works

Three invariants are maintained at all times:

- `nums[0..swap_r)` contains only 0s.
- `nums(swap_b..end]` contains only 2s.
- `nums[swap_r..i)` contains only 1s.

When we swap a 0 to the left, the value displaced from `swap_r` must be a 1 (because `swap_r <= i` and everything in `[swap_r, i)` is 1), so we can safely advance both `swap_r` and `i`. When we swap a 2 to the right, the displaced value is unknown, so we re-examine position `i` before advancing.

---

## Edge Cases

- All elements the same (e.g., `[0,0,0]`, `[1,1,1]`, `[2,2,2]`): the loop runs without issue.
- Already sorted input: no swaps needed.
- Single element: loop body runs once and terminates.

---

## Time & Space Complexity

- Time: O(n) — each element is visited at most once.
- Space: O(1) — in-place with only a few pointer variables.

---

## Common Mistakes

- Advancing `i` after swapping with `swap_b` — the newly placed value hasn't been examined yet.
- Forgetting to set `i = swap_r` after a left swap, which could re-examine already-finalized elements.

---

## Alternative Solutions

- **Frequency counter (two-pass):** Count the number of 0s, 1s, and 2s in one pass, then overwrite the array with the correct counts in a second pass. Also O(n) time and O(1) space (only 3 counts needed), but requires two passes and doesn't generalize beyond a fixed number of distinct values.
