# 322 – Coin Change

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Link:** https://leetcode.com/problems/coin-change/

---

## Problem Summary
Given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money, return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

---

## Key Insight
- The problem can be solved using dynamic programming by building up a solution for smaller amounts.
- For each amount, we can go through the denominations and see if using that coin would lead to a smaller number of coins needed.

---

## Approach
1. Initialize an array of length `amount + 1` that tracks how many coins are needed to make up each amount from `0` to `amount`. Set the value for `0` to `0` and all others to infinity.
2. Iterate through each amount from `1` to `amount`:
    - For each coin in `coins`, if the coin is less than or equal to the current amount, update the array at the current amount index with the minimum of its current value and `1 +` the value at `current amount - coin`.
3. After filling the array, if the value at `amount` is still infinity, return `-1`. Otherwise, return the value at `amount`.

---

## Why This Works
- This approach ensures that we consider all combinations of coins for each amount, building up from smaller amounts to larger ones.
- By always taking the minimum number of coins needed for each amount, we ensure that we find the optimal solution.
- We avoid redundant calculations by storing intermediate results in the array and referencing them in later calculations.

---

## Edge Cases
- Amount is 0
- Change cannot be made with given coins

---

## Time & Space Complexity
- Time: O(n * m), where n is the amount and m is the number of coin denominations.
- Space: O(n), for the array storing the minimum coins needed for each amount.

---

## Common Mistakes
- Not correctly handling the case where the current amount minus the coin value is not possible given the denominations. We need to be able to propagate this information correctly.
    - For example, if we initialized the dp array with `-1` instead of infinity, we would need an additional check to avoid simply adding `1` to `-1` and obtaining a value of `0`.
    - When we use infinity, adding `1` still results in infinity, which will be ignored when taking the minimum.

---

## Alternative Solutions
- A recursive approach with memoization could also be used, but it may be less efficient due to the overhead of recursive calls.