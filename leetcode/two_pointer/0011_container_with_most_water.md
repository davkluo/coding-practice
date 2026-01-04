# 11 – Container With Most Water

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Two Pointer
**Link:** https://leetcode.com/problems/container-with-most-water/

---

## Problem Summary
Given an array of non-negative heights, corresponding to vertical lines
at the associated index, find the maximum area of water that can be
contained between two lines.

---

## Key Insight
- Using two pointers starting at both ends of the array and moving towards
the center allows us to efficiently explore all potential container widths
while maximizing height, leading to an optimal solution in linear time.
- Moving the smaller height pointer inward is a safe greedy choice, since that line can no longer produce a larger area. To understand this consider that it is the limiting height and is therefore "at capacity". Moving the taller line inward cannot increase the area since the height is still limited by the shorter line, and the width is reduced.

---

## Approach
1. Initialize two pointers, one at the start (left) and one at the end (right) of the height array.
2. Initialize a variable to keep track of the maximum area found so far.
3. While the left pointer is less than the right pointer:
   - Calculate the area formed by the lines at the left and right pointers.
   - Update the maximum area if the calculated area is greater.
   - Move the pointer corresponding to the shorter line inward (either left++ or right--).
4. Return the maximum area found.

---

## Why This Works
- The two-pointer technique efficiently narrows down the search space by leveraging the fact that the area is limited by the shorter line. By always moving the pointer of the shorter line, we ensure that we are exploring potentially taller lines that could lead to a larger area.
- This approach avoids checking all pairs and instead finds the optimal solution in a single pass.

---

## Edge Cases
- Arrays with only two heights.
- Heights with the same value.

---

## Time & Space Complexity
- Time: O(n), where n is the number of heights. We only make one pass through the array.
- Space: O(1), as we use a constant amount of extra space.
---

## Common Mistakes
- Failing to move the pointer of the shorter line, which can lead to missing potential larger areas.
- Off-by-one errors when calculating width or updating pointers.

---

## Alternative Solutions
- None more optimal than the two-pointer approach for this problem.