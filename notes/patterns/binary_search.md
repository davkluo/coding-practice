# Pattern: Binary Search

---

## When to Use
- The input data is sorted or can be logically divided.
- The problem requires searching for a specific element or condition efficiently.

---

## Core Idea
- Repeatedly divide the search interval in half.
- Compare the target value to the middle element of the array.
- Narrow down the search to the left or right half based on the comparison.

---

## Common Techniques
- Standard Binary Search: Used on a fully sorted array.
- Modified Binary Search: Adapted for rotated sorted arrays or arrays with duplicates.
- Search for Boundaries: Finding the first or last occurrence of a target.

---

## Typical Time Complexity
- O(log n) for standard binary search operations.

---

## Common Pitfalls
- Not handling edge cases such as empty arrays or single-element arrays.
- Incorrectly calculating the mid-point, leading to infinite loops.
- Failing to adjust the search boundaries correctly based on comparisons.

---

## Canonical Problems
- Search in Rotated Sorted Array (LeetCode 33)