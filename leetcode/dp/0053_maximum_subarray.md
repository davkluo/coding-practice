# 53 – Maximum Subarray

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Secondary Patterns:** Divide and Conquer
**Link:** https://leetcode.com/problems/maximum-subarray/

---

## Problem Summary
Given an integer array `nums`, find the contiguous subarray which has the largest sum and return its sum.

---

## Key Insight
- The maximum subarray ending at position `i` is either the element at `i` itself or the element at `i` plus the maximum subarray ending at `i-1`.
- This leads to a dynamic programming approach where we can build up the solution iteratively.
- Kadane's Algorithm efficiently computes this in O(n) time with O(1) space.
    - Essentially, whenever the current sum becomes negative, reset it to 0.

---

## Approach
1. Initialize two variables: `max_sum` to negative infinity (to handle all negative inputs) and `current_sum` to 0.
2. Iterate through each number in the array:
   - Update `current_sum` to be the maximum of the current number and `current_sum + current number.
   - Update `max_sum` to be the maximum of `max_sum` and `current_sum`.
3. Return `max_sum` after iterating through the array.

---

## Why This Works
- By maintaining a running sum (`current_sum`), we can efficiently determine whether to include the current element in the existing subarray or start a new subarray.
- The algorithm ensures that we always have the maximum possible sum at each step, leading to the overall maximum sum by the end of the iteration.

---

## Edge Cases
- Single element array.
- All negative numbers.

---

## Time & Space Complexity
- Time: O(n), where n is the length of the input array. We iterate through the array once.
- Space: O(1), as we use only a fixed amount of extra space regardless of input size.
---

## Common Mistakes
- Setting the initial `max_sum` to 0 instead of negative infinity, which can lead to incorrect results when all numbers are negative.
- Forgetting to update `max_sum` after updating `current_sum`.

---

## Alternative Solutions
- A divide and conquer approach can also be used, which splits the array into two halves and finds the maximum subarray in each half and across the midpoint. This approach has a time complexity of O(n log n).
    - Pseudocode:
        - Recursively find the maximum subarray sum in the left half.
        - Recursively find the maximum subarray sum in the right half.
        - Find the maximum subarray sum that crosses the midpoint.
        - Return the maximum of the three sums.
    - Finding the maximum that crosses the midpoint involves:
        - Starting from the midpoint and expanding leftwards to find the maximum sum on the left side.
        - Starting from the midpoint + 1 and expanding rightwards to find the maximum sum on the right side.
        - Note that the above two sums do not reset; they accumulate values as we expand.
        - Summing these two maximums gives the crossing sum.