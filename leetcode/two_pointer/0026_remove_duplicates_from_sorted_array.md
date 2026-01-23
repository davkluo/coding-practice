# 26 – Remove Duplicates from Sorted Array

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Two Pointer
**Link:** https://leetcode.com/problems/remove-duplicates-from-sorted-array/

---

## Problem Summary

Given a sorted integer array, remove duplicates in-place and return the count of unique elements. The first k elements should contain the unique values in order.

---

## Key Insight

- Since the array is already sorted, duplicates are always adjacent.
- Use a write pointer to track where the next unique element should go, and a read pointer to scan through the array.

---

## Approach

1. Initialize two pointers: `swap_idx` (write position) at 0 and `i` (read position) at 0
2. While `i` is within bounds:
   - Store the current value
   - Swap the current element to the write position and increment `swap_idx`
   - Advance `i` past all duplicates of the current value
3. Return `swap_idx` as the count of unique elements

---

## Why This Works

- The write pointer always points to the next available slot for a unique element.
- Since the array is sorted, all duplicates of a value are consecutive, so we can skip them in a single inner loop.
- Each unique element gets placed at the front in order, maintaining the relative ordering.

---

## Edge Cases

- Single element → return 1, array unchanged
- All same elements → return 1, first element is the unique value
- No duplicates → return full length, array unchanged
- Negative numbers → handled the same way since array is sorted

---

## Time & Space Complexity

- Time: O(n) — single pass through the array
- Space: O(1) — only uses two pointers, modification is in-place

---

## Common Mistakes

- Off-by-one errors when checking bounds in the duplicate-skipping loop
- Returning `i` instead of `swap_idx`

---

## Alternative Solutions

- **Simple overwrite**: Instead of swapping, just overwrite `nums[swap_idx] = nums[i]` since we don't need to preserve the original values after position `swap_idx`
