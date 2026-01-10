# 57 – Insert Interval

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Interval
**Secondary Patterns:** Greedy
**Link:** https://leetcode.com/problems/insert-interval/

---

## Problem Summary
Given an array of non-overlapping intervals sorted by their start times, insert a new interval into the intervals (merge if necessary). Return the updated list of intervals. Note that we do not need to modify the intervals in place.

---

## Key Insight
- We can iterate through the existing intervals and determine where the new interval fits.
- If the current interval ends before the new interval starts, it goes before the new interval.
- If the current interval starts after the new interval ends, it goes after the new interval.
- If the intervals overlap, we merge them by updating the start and end of the new interval.

---

## Approach
1. If the list of intervals is empty, return a list containing just the new interval.
2. Initialize an empty list to hold the new intervals and a flag to track if the new interval has been merged.
3. Iterate through each interval in the list:
   - If the current interval ends before the new interval starts, append it to the new list.
   - If the current interval starts after the new interval ends, check if the new interval has been merged; if not, append it to the new list and set the merged flag. Then append the current interval.
   - If the intervals overlap, update the start and end of the new interval to the minimum start and maximum end of the overlapping intervals.
4. After the loop, if the new interval has not been merged, append it to the new list.
5. Return the new list of intervals.

---

## Why This Works
- The approach ensures that we maintain the order of intervals while correctly merging overlapping intervals.
- Whenever we encounter an interval that overlaps with the new interval, we adjust the boundaries to create a single merged interval that we then need to continue checking against the remaining intervals.

---

## Edge Cases
- Empty input
- New interval does not overlap with any existing intervals
- New interval overlaps with all existing intervals
- New interval sits entirely within an existing interval

---

## Time & Space Complexity
- Time: O(n), where n is the number of intervals
- Space: O(n), since we create a new list to hold the merged intervals.
    - Could be O(1) if we modified the input list in place, but that is not required. This would be done by tracking the indices where the new interval should be inserted, splicing out those intervals, and inserting the merged interval.

---

## Common Mistakes
- Failing to handle the case where the new interval is added at the end of the list.
- Not updating both the new interval's start and end correctly when merging overlapping intervals.

---

## Alternative Solutions
- In-place modification of the intervals list to reduce space complexity.
- The use of binary search to find the correct insertion point for the new interval, which could optimize the search time in certain scenarios. However the overall complexity remains O(n) due to the merging process and assembling the output.