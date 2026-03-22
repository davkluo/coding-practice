# 402 – Remove K Digits

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/remove-k-digits/

---

## Problem Summary

Given a string `num` representing a non-negative integer and an integer `k`, remove `k` digits to produce the smallest possible number.

---

## Key Insight

- The leftmost digits dominate the magnitude of a number, so reducing a higher place value has greater effect than reducing a lower one.
- When scanning left to right, a digit should be removed if the next digit is smaller — keeping it would leave a larger value in a higher place.
- A monotonically non-decreasing stack lets us greedily enforce this: whenever a new digit is smaller than the stack top, pop (remove) the top, spending one removal.

---

## Approach

1. Iterate through each digit in `num`.
2. While the stack is non-empty, the top is greater than the current digit, and `k > 0`, pop the stack and decrement `k`.
3. Push the current digit onto the stack.
4. After the loop, if `k > 0` remain, pop from the end of the stack (handles non-decreasing inputs like `"1111"`).
5. Join the stack, strip leading zeros, and return `"0"` if the result is empty.

---

## Why This Works

- The stack invariant is that digits are kept in non-decreasing order. Any digit that is larger than what follows it is a candidate for removal — removing it shrinks the number at the highest possible place value.
- Since each digit is pushed and popped at most once, the total work is O(n) across all k removals.
- If no drop is ever found (non-decreasing input), the smallest result is obtained by truncating the tail — the last digits are the least significant.

---

## Edge Cases

- `k = 0`: return `num` unchanged.
- `k = len(num)`: every digit is removed, return `"0"`.
- Non-decreasing input (e.g. `"12345"`, k=3): no pops during scan; remove last k digits.
- Result has leading zeros (e.g. `"10200"`, k=1 → `"0200"`): strip with `lstrip("0")`, guard against empty string.
- Single digit with k=1: return `"0"`.

---

## Time & Space Complexity

- Time: O(n) — each digit is pushed and popped at most once across the entire scan
- Space: O(n) — the stack holds at most all digits of `num`

---

## Common Mistakes

- Forgetting to handle remaining removals after the loop (non-decreasing case) — must trim from the tail.
- Stripping leading zeros but returning `""` instead of `"0"` when the entire result is zeros.
- Decrementing k inside the loop but not checking `k > 0` as a loop condition — can over-remove.

---

## Alternative Solutions

- Naive repeat scan: find and remove the first "drop" digit k times — O(k·n), acceptable for small k but degrades to O(n²) in the worst case.
