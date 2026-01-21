# 42 – Trapping Rain Water

**Platform:** LeetCode
**Difficulty:** Hard
**Primary Pattern:** Two Pointers 
**Link:** https://leetcode.com/problems/trapping-rain-water/

---

## Problem Summary
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

---

## Key Insight
- The amount of water trapped at any position is determined by the minimum of the maximum heights to its left and right, minus the height at that position.
- Using two pointers allows us to efficiently calculate trapped water in a single pass.
- Water is trapped when we find a bar lower than the current maximum on either side.

---

## Approach
1. If the input list has 2 or fewer elements, return 0 since no water can be trapped.
2. Initialize two pointers, `l` and `r`, at the start and end of the list, respectively.
3. Maintain two variables, `left_max` and `right_max`, to track the maximum heights encountered from the left and right sides.
4. While `l` is less than `r`:
   - If `left_max` is less than `right_max`,
     - Move the left pointer to the right.
     - If the height at the new left pointer is less than or equal to `left_max`, add the difference to the trapped water.
     - Otherwise, update `left_max`.
   - Else,
     - Move the right pointer to the left.
     - If the height at the new right pointer is less than or equal to `right_max`, add the difference to the trapped water.
     - Otherwise, update `right_max`.
5. Return the total trapped water.

---

## Why This Works
- By always moving the pointer with the smaller maximum height, we ensure that we are calculating trapped water based on the limiting wall.
- When we move the pointer, we can be certain that the other side has a taller wall, allowing us to safely calculate trapped water without needing to check all positions in between.
- If we move the pointer to a shorter wall, the height difference directly contributes to trapped water because the opposing wall is guaranteed to be taller.

---

## Edge Cases
- An empty list or a list with fewer than 3 elements should return 0.

---

## Time & Space Complexity
- Time: O(n), where n is the number of elements in the height list. Each element is processed at most once.
- Space: O(1), as we are using a constant amount of extra space.

---

## Common Mistakes
- Failing to update the maximum heights correctly when moving the pointers.
- Using `<=` instead of `<` when comparing heights, which can lead to incorrect trapped water calculations. In particular, it causes overcounting.
- Not handling edge cases where the input list is too short to trap any water.

---

## Alternative Solutions
- **Dynamic Programming:** Precompute the maximum heights to the left and right for each position, then calculate trapped water in a single pass. This approach uses O(n) space.