# 55 – Jump Game

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Secondary Patterns:** Greedy
**Link:** https://leetcode.com/problems/jump-game/

---

## Problem Summary

Given an integer array `nums` where each element represents the maximum jump length from that position, determine if you can reach the last index starting from index 0.

---

## Key Insight

- You don't need to track every reachable index individually. Instead, maintain a single variable `max_reachable` representing the farthest index you can reach so far.
- At each position, if `max_reachable` is less than the current index, you're stuck and can never reach the end.

---

## Approach

1. Initialize `max_reachable = 0`.
2. Iterate through each index `i` in `nums`:
   - If `max_reachable < i`, return `False` (we can't reach this index).
   - Update `max_reachable = max(max_reachable, i + nums[i])`.
3. If we finish the loop, return `True`.

---

## Why This Works

- The invariant is: after processing index `i`, `max_reachable` holds the farthest index reachable from any index in `[0, i]`.
- If we can reach index `i`, then we can reach any index up to `i + nums[i]`. By taking the max, we always know the global farthest reachable position.
- If at any point the current index exceeds `max_reachable`, no prior position could have jumped here, so the end is unreachable.

---

## Edge Cases

- Single element array (`[0]`) — already at the last index, return `True`.
- A zero at the start (`[0, 1]`) — immediately stuck, return `False`.
- Large jump at the start that clears all zeros (`[5, 0, 0, 0, 0, 0]`).

---

## Time & Space Complexity

- Time: O(n), where n is the length of the input array. We iterate through the array once.
- Space: O(1), only a single variable is used.

---

## Common Mistakes

- Thinking that the elements represent the only available jump distance at a position, rather than the maximum jump distance

---

## Alternative Solutions

- **Bottom-up DP:** Create a boolean array `dp` where `dp[i]` indicates whether index `i` is reachable. For each reachable index, mark all indices within its jump range. This is O(n^2) time and O(n) space.
- **Top-down DP with memoization:** Start from the last index and work backwards, checking if any earlier index can jump to the current "good" position. O(n^2) time in the worst case.
- **Greedy from the right:** Track the leftmost "good" index (one that can reach the end). Iterate backwards; if `i + nums[i] >= last_good`, update `last_good = i`. At the end, check if `last_good == 0`.
