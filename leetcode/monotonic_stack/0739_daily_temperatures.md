# 739 – Daily Temperatures

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/daily-temperatures/

---

## Problem Summary

Given a list of daily temperatures, return a list where each element is the number of days you must wait until a warmer temperature. If no warmer day exists, use 0.

---

## Key Insight

- A monotonic decreasing stack lets you defer the answer for each day until a warmer day is actually found
- Store unresolved days on the stack and resolve them lazily when a higher temperature appears.

---

## Approach

1. Initialize `days_til_warmer_temp` as an array of zeros with the same length as `temperatures`.
2. Maintain a stack of `(day_index, temperature)` tuples, representing days whose answer hasn't been resolved yet.
3. For each day `i` with temperature `temp`, pop all stack entries whose temperature is less than `temp` — for each popped entry, set `result[prev_day] = i - prev_day`.
4. Push `(i, temp)` onto the stack.
5. Anything remaining on the stack at the end already has a 0 in the result array.

---

## Why This Works

- The stack maintains a monotonically decreasing sequence of temperatures. When a new temperature breaks this sequence, every popped entry found its first warmer day — no earlier day could have been the answer because they were all cooler than or equal to the top of the stack.
- Days that never get popped (no future warmer day) naturally keep their initialized 0 value.

---

## Edge Cases

- Single element: no warmer day exists, return `[0]`
- Strictly decreasing temperatures: all zeros, stack never gets popped
- All equal temperatures: treated the same as decreasing — `<` comparison means equal temps don't resolve each other
- Last element: always 0

---

## Time & Space Complexity

- Time: O(n) — each element is pushed and popped at most once
- Space: O(n) — stack can hold up to n elements in the worst case (strictly decreasing input)

---

## Common Mistakes

- Using `<=` instead of `<` when comparing stack temperatures — equal temperatures should not resolve each other, only strictly warmer days count.
- Forgetting to store the index (not just the temperature) on the stack — you need the index to compute the number of days elapsed.

---

## Alternative Solutions

- Brute force: for each day, scan forward until a warmer day is found — O(n²) time, O(1) extra space.
