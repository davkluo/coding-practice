# 189 – Rotate Array

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Array / Two Pointers
**Link:** https://leetcode.com/problems/rotate-array/

---

## Problem Summary

Given an integer array `nums`, rotate it to the right by `k` steps in-place.

---

## Key Insight

- Rotating right by `k` is equivalent to moving the last `k` elements to the front. The reverse technique exploits this: reversing the whole array, then reversing each half, rearranges elements into the rotated order without extra space.
- Always reduce `k` to `k % n` first — rotating by a full multiple of `n` is a no-op.

---

## Approach

**Solution 1 — Reverse (O(1) space):**

1. Compute `shift = k % n`.
2. Reverse the entire array.
3. Reverse `nums[0 : shift]`.
4. Reverse `nums[shift : n]`.

**Solution 2 — Cyclic Replacements (O(1) space):**

1. Compute `shift = k % n`.
2. Starting from index 0, place each element at its destination `(curr + shift) % n`, saving the displaced element.
3. If we return to the start index before rotating all `n` elements (happens when `gcd(n, shift) > 1`), advance the start by 1 and continue.
4. Stop when `n` elements have been placed.

**Solution 3 — Slice Assignment (O(n) space):**

1. Compute `shift = k % n`.
2. Assign `nums[:] = nums[n-shift:] + nums[:n-shift]`.

**Solution 4 — Deque (O(n) space):**

1. Load `nums` into a `deque`.
2. For each of the `shift` steps, pop from the right and appendleft.
3. Copy the deque back into `nums`.

---

## Why This Works

- **Reverse technique:** reversing the whole array mirrors all elements; reversing each half un-mirrors them back into the correct rotated positions. The invariant is that after the three reversals, element originally at index `i` lands at index `(i + k) % n`.
- **Cyclic replacements:** each element is moved exactly once to its final position. When `gcd(n, shift) > 1`, the cycle length is `n / gcd(n, shift)`, so there are multiple independent cycles — advancing the start index handles each one.
- **Slice / deque:** both directly construct the rotated sequence by concatenating the two halves in the correct order.

---

## Edge Cases

- `k == 0` or `k % n == 0`: no rotation needed — guard with an early return
- Single-element array: all solutions handle this without issue
- `k > n`: reduce with `k % n` before any work

---

## Time & Space Complexity

| Solution    | Time                                   | Space                      |
| ----------- | -------------------------------------- | -------------------------- |
| 1 — Reverse | O(n) — three linear passes             | O(1) — in-place swaps only |
| 2 — Cyclic  | O(n) — each element moved exactly once | O(1) — one temp variable   |
| 3 — Slice   | O(n) — slice + concatenation           | O(n) — new list allocated  |
| 4 — Deque   | O(n) — deque build + shift + copy-back | O(n) — deque copy of nums  |

---

## Common Mistakes

- Forgetting to reduce `k` with `% n` — causes index errors or unnecessary work
- In cyclic replacements, not handling the case where `gcd(n, shift) > 1` (multiple independent cycles), causing an infinite loop or incomplete rotation
- In the reverse technique, using `k` instead of `shift = k % n` for the split index

---

## Alternative Solutions

- All four approaches above are O(n) time; the tradeoff is O(1) vs O(n) space.
- A brute-force single-step rotation repeated `k` times is O(n·k) — avoid.

---

## Python Runtime Quirk

Despite solutions 1 and 2 being theoretically superior in space complexity, in practice on LeetCode (and CPython generally) solutions 3 and 4 often post better runtime and memory statistics:

- **Slice assignment (`nums[:] = a + b`) and deque operations are implemented in C** inside CPython. Each "operation" is a bulk memory move with minimal Python bytecode overhead.
- **The O(1) solutions execute more Python bytecode per element** — each swap in `reverse_range` involves a tuple unpack and two index assignments, all interpreted at the Python level.

The takeaway: in CPython, offloading work to C-backed builtins (slicing, `deque`, `collections`) often beats a tighter algorithm written in pure Python loops, even when the pure-Python version has better asymptotic space complexity. The theoretical analyses are still correct — the constant factors just happen to favor the O(n) space solutions at practical input sizes on this platform.
