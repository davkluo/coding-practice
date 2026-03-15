# 303 – Range Sum Query - Immutable

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Prefix Sum
**Link:** https://leetcode.com/problems/range-sum-query-immutable/

---

## Problem Summary

Given an integer array, answer multiple range sum queries `sum_range(left, right)` returning the sum of elements between indices `left` and `right` inclusive.

---

## Key Insight

- Precompute a prefix sum array so each query is answered in O(1) instead of O(n).
- `prefix_sums[i]` stores the sum of `nums[0..i]` inclusive, so a range sum is a single subtraction plus the left element.

---

## Approach

1. In `__init__`, build `prefix_sums` where `prefix_sums[i] = prefix_sums[i-1] + nums[i]`.
2. For `sum_range(left, right)`, return `prefix_sums[right] - prefix_sums[left] + nums[left]`.
   - `prefix_sums[right]` is the sum of `nums[0..right]`.
   - Subtracting `prefix_sums[left]` removes `nums[0..left]`, but that overshoots by one — it also removes `nums[left]` itself, so add it back.

---

## Why This Works

- `prefix_sums[right] - prefix_sums[left]` gives the sum of `nums[left+1..right]`.
- Adding `nums[left]` back includes the left endpoint, giving the correct inclusive range sum.

---

## Edge Cases

- `left == right` — single element; `prefix_sums[right] - prefix_sums[left] + nums[left]` simplifies to `nums[left]`. ✓
- `left == 0` — `prefix_sums[right] - prefix_sums[0] + nums[0]` = `prefix_sums[right]`, the full prefix. ✓
- Single-element array — only one valid query `(0, 0)`, handled correctly.

---

## Time & Space Complexity

- Time: O(n) build, O(1) per query
- Space: O(n) — for the prefix sum array

---

## Common Mistakes

- Forgetting to add `nums[left]` back: `prefix_sums[right] - prefix_sums[left]` returns `nums[left+1..right]`, missing the left endpoint.
- Using the canonical sentinel formulation (`prefix[0] = 0`, `prefix[i] = sum of nums[0..i-1]`) would simplify the query to `prefix[right+1] - prefix[left]` with no correction needed — mixing the two formulations causes off-by-one errors.

---

## Alternative Solutions

- **Canonical sentinel prefix array**: define `prefix[0] = 0` and `prefix[i+1] = prefix[i] + nums[i]`, so `sum_range(left, right) = prefix[right+1] - prefix[left]`. Cleaner formula with no `+ nums[left]` correction, at the cost of a length `n+1` array.
- **Brute force**: iterate and sum on each query. O(n) per query — correct but defeats the purpose when multiple queries are needed.
