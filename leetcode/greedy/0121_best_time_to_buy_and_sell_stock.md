# 121 – Best Time to Buy and Sell Stock

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Greedy  
**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

---

## Problem Summary
Given an array of prices representing stock price on a given day,
determine the maximum profit from buying on one day and selling on a
different future date. If no positive profit is possible return 0.

---

## Key Insight
The maximum profit on a given day is determined by the minimum price seen thus far. By tracking the minimum price as we iterate through the list, we can calculate potential profits and update the maximum profit accordingly.

---

## Approach
1. Check for the edge case where the list has only one price; return 0 in that case.
2. Initialize `min_price` to the price on the first day and `max_profit` to 0.
3. Iterate through the prices starting from the second day:
    - Calculate the potential profit by subtracting `min_price` from the current price.
    - Update `max_profit` if the potential profit is greater than the current `max_profit`.
    - Update `min_price` if the current price is lower than `min_price`.
4. Return `max_profit` after iterating through all prices.

---

## Why This Works
We keep track of the minimum price seen as we iterate through the array, so for each price we can compute the maximum profit achievable by selling on that day. By the end of the iteration we have considered all possible maximal profits.

---

## Edge Cases
- Only a single price in the list.
- Prices that are always decreasing.
- Maximum profit is zero.

---

## Time & Space Complexity
- Time: O(n), where n is the number of days (prices).
- Space: O(1), as we only use a few variables regardless of input size.
---

## Common Mistakes
- Forgetting to update the minimum price after calculating profit.
- Not handling the edge case of a single price correctly.

---

## Alternative Solutions
- A bottom-up tabulation could also work but would unnecessarily increase space complexity to O(n).