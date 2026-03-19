# 875 – Koko Eating Bananas

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Search on Answer
**Link:** https://leetcode.com/problems/koko-eating-bananas/

---

## Problem Summary

Given a list of banana pile sizes and an integer `h`, return the minimum integer eating speed `k` such that Koko can finish all piles within `h` hours. Koko eats at most `k` bananas per hour from a single pile, and `h >= len(piles)`.

---

## Key Insight

- The answer lives in a bounded, monotonic search space: speeds in `[1, max(piles)]`
- Monotonicity: if speed `k` is valid, every speed `k' > k` is also valid — so binary search applies
- Use `l < r` with `r = m` (not `r = m - 1`) to find the leftmost valid speed; the window collapses to the answer

---

## Approach

1. Set `l = 1`, `r = max(piles)`
2. While `l < r`, compute `m = (l + r) // 2`
3. Check if speed `m` can finish all piles in `h` hours using `is_valid_speed`
   - For each pile, add `ceil(pile / m)` to a running total; short-circuit if it exceeds `h`
4. If valid: `r = m` (keep `m` as a candidate, try slower)
5. If not valid: `l = m + 1` (discard `m`, must go faster)
6. Return `l` when loop exits

---

## Why This Works

- `l < r` exits when `l == r`, at which point both pointers sit on the same value
- The invariant: `l` is never moved past a valid speed, `r` is never moved past a valid speed — so the single remaining element must be the minimum valid speed
- Contrast with classic exact-match binary search (`l <= r` with early return): here there is no early return, so we rely on window collapse rather than a hit condition

---

## Edge Cases

- `h == len(piles)`: tightest constraint, answer is `max(piles)` — must finish each pile in exactly one hour
- `h >> len(piles)`: speed of 1 is sufficient
- Single pile: answer is `ceil(pile / h)`
- One very large pile among small ones: answer dominated by the large pile

---

## Time & Space Complexity

- Time: O(n log C) — binary search over `[1, max(piles)]` is O(log C), each validity check is O(n)
  - C is the maximum pile size
- Space: O(1) — no extra data structures

---

## Common Mistakes

- Using `l <= r` without an early return causes an infinite loop when `canFinish(m)` is true and `r = m` produces no change
- Using `r = m - 1` instead of `r = m` skips the minimum valid speed
- Forgetting to use `ceil` for hours per pile (integer division rounds down, undercounting time)

---

## Alternative Solutions

- No meaningfully better alternative — O(n log C) is optimal since all piles must be checked and the search space can't be reduced below O(log C)
