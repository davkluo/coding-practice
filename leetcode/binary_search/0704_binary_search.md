# 704 – Binary Search

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Binary Search  
**Link:** https://leetcode.com/problems/binary-search/

---

## Problem Summary

Given a sorted array of integers and a target value, find the index of the target in the array. If the target is not found, return -1.

---

## Key Insight

- The array is sorted, allowing for efficient searching using binary search.
- At each step, we can halve the search space based on comparisons.

---

## Approach

1. Initialize two pointers, `left` and `right`, to the start and end of the array.
2. While `left` is less than or equal to `right`:
   - Calculate the middle index `mid`.
   - If `nums[mid]` equals the target, return `mid`.
   - If `nums[mid]` is less than the target, move the `left` pointer to `mid + 1`.
   - If `nums[mid]` is greater than the target, move the `right` pointer to `mid - 1`.
3. If the target is not found, return -1.

---

## Why This Works

- Binary search efficiently narrows down the search space by leveraging the sorted property of the array.
- Comparing the middle element with the target allows us to discard half of the remaining elements in each iteration.
- We can guarantee which half potentially has the target because of the sorted order.

---

## Edge Cases

- Empty array: Should return -1.
- Single element array: Should return 0 if the element matches the target, otherwise -1

---

## Time & Space Complexity

- Time: O(log n)
- Space: O(1)

---

## Common Mistakes

- Not updating the pointers correctly, leading to infinite loops.
- Off-by-one errors when calculating the middle index or updating pointers.

---

## Alternative Solutions

- None as efficient as binary search for this problem.
