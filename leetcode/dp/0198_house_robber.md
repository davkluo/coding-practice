# 198 – House Robber

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Link:** https://leetcode.com/problems/house-robber/

---

## Problem Summary
Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police (i.e., you cannot rob two adjacent houses).

---

## Key Insight
- At each house, we can either rob it or skip it
- We only need to maintain two variables that track the maximum amount robbed up to the previous two houses, which we pair with the above decision

---

## Approach
1. Initialize two variables, `two_prior` and `one_prior`, to 0. These will track the maximum amount robbed up to the house two steps back and one step back, respectively.
2. Iterate through each house's amount in `nums`:
   - Calculate the best choice at the current house as the maximum of:
     - Robbing the current house plus the amount from two houses back (`num + two_prior`)
     - Skipping the current house and taking the amount from the previous house (`one_prior`)
   - Update `two_prior` to be `one_prior` and `one_prior` to be the best choice calculated.
3. After processing all houses, `one_prior` will contain the maximum amount that can be robbed without alerting the police.
4. Return `one_prior`.

---

## Why This Works
- The decision to rob or skip each house is based on the maximum amounts calculated from previous houses. This ensures that we always have the optimal solution at each step without needing to store all previous results, thus optimizing space usage.

---

## Edge Cases
- Single element
- All elements are zero
- Large input size

---

## Time & Space Complexity
- Time: O(n), where n is the number of houses. We iterate through the list once.
- Space: O(1), as we only use a fixed amount of extra space regardless of input size.
---

## Common Mistakes
- Forgetting to update the `two_prior` and `one_prior` variables correctly after each iteration.

---

## Alternative Solutions
- Using a DP array to store maximum amounts at each house, which would use O(n) space instead of O(1).