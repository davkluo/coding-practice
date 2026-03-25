# 227 – Basic Calculator II

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Stack
**Link:** https://leetcode.com/problems/basic-calculator-ii/

---

## Problem Summary

Given a string representing a valid arithmetic expression with `+`, `-`, `*`, `/` and non-negative integers, evaluate and return the result with integer division truncating toward zero.

---

## Key Insight

- `*` and `/` bind tighter than `+` and `-`, so they must be evaluated before any pending addition/subtraction. This means you can eagerly resolve `*`/`/` the moment you see the next operator, while deferring `+`/`-` to a left-to-right cleanup pass.

---

## Approach

1. Scan left to right, accumulating digits into `curr_number`.
2. When a non-digit, non-space character is encountered, flush `curr_number`:
   - If the previous operator is `*` or `/`, pop the last number and evaluate immediately.
   - Otherwise, push `curr_number` onto the numbers stack.
3. Push the current operator onto the operators stack.
4. After the loop, flush the final `curr_number` the same way.
5. Process the remaining `+`/`-` operators left-to-right (front to back of the stacks).

---

## Why This Works

- By the time we reach a `+` or `-`, any `*`/`/` between the previous `+`/`-` and now has already been collapsed — so the numbers stack contains only addends/subtrahends, each representing a fully-evaluated term.
- Processing `+`/`-` left-to-right is critical: subtraction is not commutative, so popping from the back of the stack gives the wrong answer (e.g. `10-3-2` would yield `9` instead of `5`).

---

## Edge Cases

- Single number with no operators: loop ends with one item in numbers, no operators to process.
- Expression ends with `*` or `/`: the final number flush must apply the same eager evaluation as inside the loop — extract into a helper to avoid duplication.

---

## Time & Space Complexity

- Time: O(n) — single pass over the string, plus a linear cleanup of the remaining operators
- Space: O(n) — numbers and operators stacks, at most one entry per token

---

## Common Mistakes

- Flushing the last number after the loop with simpler logic than inside the loop — if the last operator is `*` or `/`, it won't be eagerly evaluated, leaving the wrong value in the stack.
- Processing the final `+`/`-` cleanup by popping from the back of the stack — this applies operators right-to-left, breaking subtraction and division.
- Using the sentinel trick (`s + "+"`) without realizing the `+` is appended to a temporary copy — the original string is not modified.

---

## Alternative Solutions

- Sentinel approach: append `"+"` to the input string so the final number is flushed through the same code path as all others, removing the need for post-loop special casing.
