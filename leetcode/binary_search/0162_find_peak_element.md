# 162 – Find Peak Element

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/find-peak-element/

---

## Problem Summary

Given an integer array `nums`, find a peak element, and return its index. A peak element is an element that is strictly greater than its neighbors. If the array contains multiple peaks, return the index to any of the peaks. Out of bounds elements are considered to be negative infinity. The algorithm must run in O(log n) time. No two consecutive elements are equal.

---

## Key Insight

- It is trivial to solve this with a linear scan, but the O(log n) time requirement suggests a binary search approach.
- There is guaranteed to be at least one peak in the array since the ends are considered negative infinity.
- If we compare a middle element with its neighbors, either
  - It is a peak itself
  - The left neighbor is greater, indicating a peak exists on the left side
  - The right neighbor is greater, indicating a peak exists on the right side
- The fact that no two consecutive elements are equal allows the above logic to hold.

---

## Approach

1. Define two pointers, `left` and `right`, initialized to the start and end of the array.
2. While `left` is less than or equal to `right`:
   - Calculate the middle index `mid`.
   - Calculate the left and right neighbors of `mid`, treating out-of-bounds indices as negative infinity.
   - If `nums[mid]` is greater than both its neighbors (or if it is at the boundary), return `mid` as the peak index.
   - If the left neighbor is greater than `nums[mid]`, move the `right` pointer to `mid - 1`.
   - Otherwise, move the `left` pointer to `mid + 1`.

---

## Why This Works

- Binary search gives us O(log n) runtime
- When we check the middle element against its neighbors, we know for a fact that if it is not a peak itself, a peak must exist in the direction of the greater neighbor.
  - We know this because the value rises towards that neighbor, and must eventually fall back down to negative infinity at the boundaries, ensuring a peak exists in between.
- We move the pointers beyond `mid` when it is confirmed that a peak cannot exist at `mid`, ensuring we do not get stuck in an infinite loop.

---

## Edge Cases

- Single element array: The only element is the peak.
- Two element array: The larger of the two is the peak.

---

## Time & Space Complexity

- Time: O(log n)
- Space: O(1)

---

## Common Mistakes

- Failing to handle boundary conditions correctly, especially when `mid` is at the start or end of the array.
- Not considering the case where the peak is at the boundaries of the array.

---

## Alternative Solutions

- Binary search is the most efficient solution here.
