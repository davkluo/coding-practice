# 994 – Rotting Oranges

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Breadth-First Search (BFS)
**Link:** https://leetcode.com/problems/rotting-oranges/

---

## Problem Summary

Given a 2D grid, each cell can have one of three values:

- the value 0 representing an empty cell,
- the value 1 representing a fresh orange, or
- the value 2 representing a rotten orange.
  Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten. Return the minimum number of minutes that must elapse until no cell has a fresh orange, or -1 if this never happens.

---

## Key Insight

- The spreading of rot can be replicated by BFS starting from multiple sources (the rotten oranges)
- We can start by doing an initial pass through the grid to tally how many fresh oranges there are and to enqueue the positions of all the rotten oranges
- If there are fresh oranges that are unreachable from the initial rotten oranges, we can return -1

---

## Approach

1. Initialize a queue to keep track of the positions of the rotten oranges and a counter for the number of fresh oranges.
2. Iterate through the grid to populate the queue with the positions of the rotten oranges and count the fresh oranges.
3. If there are no fresh oranges, return 0.
4. Initialize a timer to keep track of the number of minutes elapsed.
5. Perform BFS from the initial rotten oranges:
   - Increment the timer
   - For each rotten orange currently in the queue (entire layer), rot the adjacent fresh oranges and enqueue their positions. Make sure to decrement the fresh orange counter for each one that gets rotted.
   - If at any point the fresh orange counter reaches zero, return the timer.
6. If the queue is empty and there are still fresh oranges, return -1.

---

## Why This Works

- BFS processes the grid level by level, simulating the minute-by-minute spread of rot
- Processing the entire layer of rotten oranges at once ensures that we are accurately counting the minutes elapsed
- The initial pass allows us to handle edge cases where there are no fresh oranges
- Counting how many fresh ones there are in total allows the final check if there are any unreachable fresh oranges

---

## Edge Cases

- No fresh oranges at the start (should return 0)
- All oranges are rotten at the start (should return 0)
- Fresh oranges that are completely isolated from rotten oranges (should return -1)

---

## Time & Space Complexity

- Time: O(m\*n) where m and n are the dimensions of the grid, since we need to process every cell at most once
- Space: O(m\*n) for the queue in the worst case when almost all oranges are rotten

---

## Common Mistakes

- Not processing the entire layer of rotten oranges before incrementing the timer
- Forgetting to check for the case where there are no fresh oranges at the start
- Not decrementing the fresh orange counter when rotting adjacent oranges

---

## Alternative Solutions

- BFS is the most straightforward here
