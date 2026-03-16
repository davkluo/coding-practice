# 1094 – Car Pooling

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Difference Array
**Link:** https://leetcode.com/problems/car-pooling/

---

## Problem Summary

Given a list of trips `[numPassengers, from, to]` and a car capacity, determine whether all passengers can be picked up and dropped off without exceeding capacity at any location. Locations are bounded between 0 and 1000.

---

## Key Insight

- Use a difference array over locations: record the net change in passengers at each stop, then scan left to right checking the running total never exceeds capacity.
- Trips can be processed in any order — no sorting needed — because the difference array encodes all changes by position, not by trip order.

---

## Approach

1. Allocate `deltas = [0] * 1001` (locations 0–1000).
2. For each trip `(num_passengers, src, dst)`:
   - `deltas[src] -= num_passengers` (passengers board, consuming capacity)
   - `deltas[dst] += num_passengers` (passengers alight, freeing capacity)
3. Scan `deltas` left to right, accumulating into `capacity`:
   - If `capacity + change < 0` at any location, return `False`.
   - Otherwise apply: `capacity += change`.
4. Return `True`.

---

## Why This Works

- The difference array captures all boarding and alighting events at their exact locations. Scanning it left to right reconstructs the running passenger load in location order regardless of trip input order.
- Tracking remaining capacity (decrement on board, increment on alight) lets you check `capacity + change < 0` directly — no separate passenger count variable needed.
- Drop-off happens before boarding at the same stop because `dst` of one trip and `src` of another at the same index are both applied as part of the same `change` value, which nets out correctly.

---

## Edge Cases

- Two trips sharing a stop where one drops off and the other boards — handled correctly since both deltas land at the same index and are summed together.
- Trips unsorted by start location — irrelevant; the difference array is position-indexed, not trip-ordered.
- Single trip exactly at capacity — `capacity + change == 0`, which passes the `< 0` check.

---

## Time & Space Complexity

- Time: O(n + 1000) = O(n) — one pass to build deltas, one fixed-size pass to scan
- Space: O(1) — `deltas` is always length 1001 regardless of input size

---

## Common Mistakes

- Thinking trips need to be sorted by start location — the difference array makes this unnecessary. Sorting would increase time complexity to O(n log n) and space complexity to O(n).
- Using size 1000 instead of 1001 — locations go up to 1000 inclusive, so index 1000 must be valid.

---

## Alternative Solutions

- **Sorting + min-heap**: sort trips by start, use a heap to track active drop-offs. O(n log n) time — more complex and slower; useful if the location bound were not fixed.
- **Event list**: collect `(location, delta)` pairs, sort by location, scan. O(n log n) due to sort — equivalent to the difference array approach but without exploiting the fixed location bound.
