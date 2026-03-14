# 0904 – Fruit Into Baskets

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/fruit-into-baskets/

---

## Problem Summary

Given an array where `fruits[i]` is the fruit type at tree `i`, find the longest contiguous subarray containing at most 2 distinct fruit types. You can start at any tree and must pick one fruit per tree moving only right.

---

## Key Insight

- "Longest subarray with at most 2 distinct values" is a sliding window problem.
- The tricky part is efficiently knowing *where to move the left boundary* when a third type enters: it should jump to just after the last occurrence of the evicted type. A deque tracking insertion order (LRU-style) combined with a map of last-seen indices handles this in O(1).

---

## Approach

1. Maintain a deque `fruit_types` (at most 2 types, ordered least-recently-used to front) and a map `fruits_to_idx` of each type's most recent index. `l` is the exclusive left boundary, initialized to `-1`.
2. For each fruit at index `r`:
   - If already in `fruit_types`: update its last index. If it was the front (LRU), rotate it to the back so it is no longer the eviction candidate.
   - If new: append to deque and record index. If the deque now has 3 types, evict the front (LRU type), and advance `l` to `fruits_to_idx[evicted]` — the last position of the dropped type becomes the new exclusive left boundary.
3. After handling the window, update `most_fruit = max(most_fruit, r - l)`.
4. Return `most_fruit`.

---

## Why This Works

- The deque front is always the type not seen most recently, making it the safe eviction candidate when a third type arrives.
- Setting `l = fruits_to_idx[removed]` works because `l` is exclusive — the new window starts at `l + 1`, which is the element right after the last occurrence of the evicted fruit type.
- Rotating the front to the back when a type is "refreshed" keeps the LRU invariant correct.

---

## Edge Cases

- Single element — window size is 1, returned correctly.
- All same type — deque never exceeds 1 entry, window grows the whole way.
- Alternating two types — no eviction ever happens, answer is full array length.
- Third type appears immediately after a long run of one type — `l` jumps far forward.

---

## Time & Space Complexity

- Time: O(n) — single pass; deque operations are O(1)
- Space: O(1) — deque and map are bounded to at most 2 entries each

---

## Common Mistakes

- Forgetting to rotate the front to the back when the front type is seen again — without this, the wrong type gets evicted next.
- Using `l` as inclusive instead of exclusive: `r - l` gives the correct window size only when `l` is exclusive (the element at `l` is not in the window).
- Updating `most_fruit` only inside the `if fruit in fruit_types` branch — the update at the bottom of the loop must be unconditional to catch the new-fruit case too.

---

## Alternative Solutions

- **Sliding window with a `Counter`/`defaultdict`**: expand `r` each step; when `len(counter) > 2`, advance `l` one step at a time, decrementing counts and deleting keys that reach 0, until back to 2 types. O(n) amortized — each element is added and removed at most once across all shrink steps. Simpler logic than the deque approach, but requires deleting zero-count keys for `len(counter)` to stay accurate.
