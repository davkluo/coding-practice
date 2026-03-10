# 0169 – Majority Element

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Array
**Link:** https://leetcode.com/problems/majority-element/

---

## Problem Summary

Given an array of integers, find the majority element — the element that appears more than `n/2` times. A majority element is guaranteed to exist.

---

## Key Insight

- Boyer-Moore Voting: votes for the current candidate cancel out votes against it. Since the majority element appears more than half the time, it always "survives" the cancellations.

---

## Approach

1. Initialize `candidate = None`, `count = 0`.
2. For each number:
   - If `count == 0`, set `candidate = num`.
   - If `num == candidate`, increment `count`; otherwise decrement `count`.
3. Return `candidate`.

---

## Why This Works

- The majority element appears more than `n/2` times, so it has more occurrences than all other elements combined.
- Every cancellation consumes one majority vote and one non-majority vote, but the majority element always has surplus votes.
- The final candidate when the loop ends is guaranteed to be the majority element.

---

## Edge Cases

- Single element — trivially the majority element.
- All elements the same — count only ever increments, candidate is set on the first element.
- Majority element clustered at the end — intermediate candidates may change, but the final candidate is correct because majority votes always outnumber cancellations.

---

## Time & Space Complexity

- Time: O(n) — single pass through the array
- Space: O(1) — only two variables used

---

## Common Mistakes

- Resetting the candidate when count hits 0 but forgetting to also check the current element against the new candidate in the same iteration (the code handles this by setting candidate first, then comparing).
- Assuming the algorithm works without the guaranteed majority — it doesn't; without the guarantee, a second pass to verify the candidate would be needed.

---

## Alternative Solutions

- **Hash map frequency count**: count occurrences of each element, return the one with count > n/2. O(n) time, O(n) space — simpler to reason about but uses extra memory.
- **Sort**: sort the array and return `nums[n//2]`; the majority element always occupies the middle index. O(n log n) time, O(1) space — easy to implement but slower.
- **Bit manipulation**: for each bit position, count how many numbers have that bit set; if more than n/2, the majority element has that bit. O(32n) = O(n) time, O(1) space.
