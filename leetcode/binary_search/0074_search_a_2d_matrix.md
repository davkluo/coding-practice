# 74 – Search a 2D Matrix

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search
**Link:** https://leetcode.com/problems/search-a-2d-matrix/

---

## Problem Summary

Given an m x n matrix where each row is sorted in ascending order and the first integer of each row is greater than the last integer of the previous row, write an efficient algorithm to search for a target value in the matrix. Return true if the target is found, and false otherwise.

---

## Key Insight

- The matrix can be treated as a sorted array as long as we handle the wrapping of rows
- This allows us to apply binary search techniques

---

## Approach

1. Set up left and right pointers for binary search by assigning `left = 0` and `right = m * n - 1`, where `m` is the number of rows and `n` is the number of columns.
2. While `left` is less than or equal to `right`:
   - Calculate the mid index: `mid = (left + right) // 2`.
   - Convert the mid index to 2D coordinates:
     - `row = mid // n`
     - `col = mid % n`
   - Compare the value at `matrix[row][col]` with the target:
     - If it equals the target, return true.
     - If it is less than the target, move the left pointer: `left = mid + 1`.
     - If it is greater than the target, move the right pointer: `right = mid - 1`.
3. If the loop ends without finding the target, return false.

---

## Why This Works

- This is essentially binary search except we need to transform the 1D index back to 2D coordinates.
- We achieve O(log(m\*n)) time complexity since binary search halves the search space with each iteration.

---

## Edge Cases

- Single element matrix: Check if that element is the target.

---

## Time & Space Complexity

- Time: O(log(m\*n)) where m is the number of rows and n is the number of columns.
- Space: O(1) since we only use a few extra variables.

---

## Common Mistakes

- Forgetting to convert the mid index back to 2D coordinates correctly.
- Not necessarily a mistake, but we don't need 2D coordinate representations for the left and right pointers themselves, since we don't actually access the elements at the boundary pointers.
- Moving the wrong pointer based on the comparison.

---

## Alternative Solutions

- None as efficient as binary search for this problem.
