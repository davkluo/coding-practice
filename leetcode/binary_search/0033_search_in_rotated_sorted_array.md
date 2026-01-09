# 33 – Search in Rotated Sorted Array

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/

---

## Problem Summary
Given a rotated sorted array and a target value, find the index of the target in O(log n) time complexity. If the target is not found, return -1.

---

## Key Insight
- The array is sorted but rotated, which means one half of the array is always sorted.
- Use binary search to determine which half is sorted and decide which half to continue searching in.
- We can simply use binary search with an added condition of checking whether or not the end of the partition of interest has rotated over.

---

## Approach
1. Initialize two pointers, `left` and `right`, to the start and end of the array.
2. While `left` is less than or equal to `right`:
   - Calculate the mid-point index.
   - If the middle element is the target, return its index.
   - Determine which half of the array is sorted:
     - If the left half is sorted:
       - Check if the target lies within this range. If yes, adjust `right` to `mid - 1`, else adjust `left` to `mid + 1`.
     - If the right half is sorted:
       - Check if the target lies within this range. If yes, adjust `left` to `mid + 1`, else adjust `right` to `mid - 1`.
3. If the target is not found, return -1.

---

## Why This Works
- The binary search approach efficiently narrows down the search space by leveraging the properties of the rotated sorted array.
- Focusing on the sorted half and leaving the other half in the else condition makes the operations essentially the same as a standard binary search, maintaining O(log n) complexity.

---

## Edge Cases
- Single element array.
- Target not present in the array.

---

## Time & Space Complexity
- Time: O(log n)
- Space: O(1)

---

## Common Mistakes
- Failing to correctly identify which half of the array is sorted.
- Not adjusting the pointers correctly based on the target's position relative to the sorted half.
- Forgetting to check that the end of the partition of interest has rotated over.

---

## Alternative Solutions
- None that meets the O(log n) requirement; linear search would be O(n).