# 0567 – Permutation in String

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/permutation-in-string/

---

## Problem Summary

Given two strings `s1` and `s2`, return `True` if any permutation of `s1` is a substring of `s2`. All characters are lowercase English letters.

---

## Key Insight

- A permutation of `s1` is just any window of `s2` with the same character frequency counts as `s1`.
- Use a fixed-size sliding window of length `len(s1)` over `s2` and compare frequency arrays at each step.

---

## Approach

1. If `len(s1) > len(s2)`, return `False` immediately.
2. Build `s1_counts`, a length-26 integer array of character frequencies for `s1`.
3. Slide a window of size `len(s1)` across `s2`, maintaining `s2_counts`:
   - Add the incoming character at position `i`.
   - If the window exceeds `len(s1)`, remove the character at `window_start` and advance `window_start`.
   - If `s1_counts == s2_counts`, return `True`.
4. Return `False` if no matching window was found.

---

## Why This Works

- A permutation has identical character counts to the original, so frequency equality is a necessary and sufficient check.
- The fixed-size window ensures we always compare exactly `len(s1)` characters at a time.
- The 26-element array comparison is O(26) = O(1), so each step is constant time.

---

## Edge Cases

- `len(s1) > len(s2)` — impossible to contain a permutation, return `False` early.
- `s1` and `s2` are equal length — the only window to check is all of `s2`.
- Single character `s1` — any occurrence of that character in `s2` is a match.

---

## Time & Space Complexity

- Time: O(n + m) — O(n) to build `s1_counts`, O(m) to slide the window over `s2`
- Space: O(1) — two fixed-size arrays of length 26, independent of input size

---

## Common Mistakes

- Using a `Counter` or `defaultdict` instead of a fixed array: equality between dicts only works correctly if keys with zero counts are deleted, requiring extra bookkeeping on every add/remove. A length-26 array avoids this entirely — zeroes are fine and comparisons always work.
- Off-by-one on window shrinking: shrink when `window_length > n`, not `>= n`, so the window reaches exactly size `n` before comparing.
- Forgetting to check after the window is exactly size `n` — the comparison must happen every iteration once the window is full, including the step where it first reaches size `n`.

---

## Alternative Solutions

- **Counter with a `matches` variable**: track how many of the 26 characters have equal counts between the two windows, incrementing/decrementing as the window slides. Avoids the full array comparison each step, but requires careful handling of zero-count keys if using a dict. O(n + m) time, O(1) space.
- **Two-pointer with sorting**: generate all length-`n` substrings of `s2`, sort each, and compare to sorted `s1`. O(m * n log n) time — correct but far too slow for large inputs.
