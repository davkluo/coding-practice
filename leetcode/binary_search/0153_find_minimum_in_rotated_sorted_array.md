# 153 – Find Minimum in Rotated Sorted Array

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

---

## Problem Summary
Given a rotated sorted array of unique elements, return the minimum element in the array. The solution must run in O(log n) time complexity.

---

## Key Insight
- We can use a modified binary search since the array is partially sorted.
- The base case in our search is when the pointer window is sorted, indicating the minimum is at the left pointer.
- We can detect when the pointer window is sorted by comparing the left and right elements.

---

## Approach
1. Initialize two pointers, `left` and `right`, at the start and end of the array.
2. While `left` is less than or equal to `right`:
    - Check if the subarray from `left` to `right` is sorted. If it is, return the element at `left`.
    - Calculate the mid-point `mid`.
    - Determine which side has the rotation:
        - If the mid value is greater than or equal to the left value, the left side is sorted, so the minimum must be in the right side and the mid value is not the minimum. Move `left` to `mid + 1`.
        - Otherwise, the minimum is in the left side and the mid value could be the minimum. Move `right` to `mid`.
    - Continue until the minimum is found.

---

## Why This Works
- The binary search approach narrows down the search space by half each iteration, ensuring O(log n) time complexity.
- We are guaranteed to terminate because in the worst case, we will eventually narrow down to a single element, which is considered sorted.

---

## Edge Cases
- Single element array.
- Already sorted array (not rotated).

---

## Time & Space Complexity
- Time: O(log n)
- Space: O(1)

---

## Common Mistakes
- Failing to check if the current subarray is sorted before proceeding with binary search.
- Incorrectly updating the pointers, leading to infinite loops or missing the minimum element.
    - Don't include `mid` when it cannot be the minimum.
    - Include `mid` on the else condition of the above.
- Failing to check whether the mid element is greater than or equal to the left element to determine which side is sorted, since the mid element could be the leftmost element.

---

## Alternative Solutions
- None as efficient as binary search for this problem due to the O(log n) requirement.