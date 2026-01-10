# 56 – Merge Intervals

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Interval
**Secondary Pattern:** Greedy, Sorting
**Link:** https://leetcode.com/problems/merge-intervals/

---

## Problem Summary
Given an array of intervals represented as [start, end], merge all overlapping intervals and return an array of the non-overlapping intervals.

---

## Key Insight
- Sorting the intervals by their start times allows for a linear scan to merge overlapping intervals.

---

## Approach
1. Sort the intervals based on the start time.
2. Initialize an empty list to hold merged intervals.
3. Initialize variables to track the current start and end of the interval being merged to be the start and end of the first interval.
4. Loop through each interval:
    - If the interval's start is less than or equal to the current end, update the current end to be the maximum of the current end and the interval's end. Note that we don't need to check if the interval's start is greater than the current start because the intervals are sorted.
    - If the interval's start is greater than the current end, append `[current_start, current_end]` to the merged list, and update `current_start` and `current_end` to the start and end of the new interval.
5. After the loop, append the last interval `[current_start, current_end]` to the merged list.
    - Note that if the last iteration merged with previous intervals, it won't be added yet. Similarly, if the last interval was standalone, it also needs to be added.
6. Return the merged list.

---

## Why This Works
- Sorting ensures that all overlapping intervals are adjacent, allowing for a single pass to merge them efficiently.

---

## Edge Cases
- Intervals that touch at endpoints (e.g., [1,4] and [4,5]) should be merged.
- Single interval input should return the same interval.

---

## Time & Space Complexity
- Time: O(n log n) due to sorting the intervals.
    - Merging the intervals takes O(n) time.
- Space: O(1) if the output list does not count towards space complexity, otherwise O(n) for the output list.

---

## Common Mistakes
- Forgetting to add the last merged interval after the loop.

---

## Alternative Solutions
- Using a stack to keep track of merged intervals, pushing new intervals onto the stack or merging with the top of the stack as needed.