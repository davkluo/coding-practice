# Pattern: Interval

---

## When to Use
- Problems involving ranges or intervals, especially when you need to merge, insert, or find overlaps between them.
- Situations where you need to manage a collection of intervals and perform operations like union, intersection, or difference.

---

## Core Idea
- Intervals can be represented as pairs of numbers (start, end).
- Key operations often involve comparing the start and end points of these intervals to determine relationships such as overlap or adjacency.
- Merging intervals typically involves taking the minimum start and maximum end of overlapping intervals.

---

## Common Techniques
- Sorting intervals by their start times to facilitate easier comparison and merging.
- Iterating through the sorted intervals and maintaining a list of merged intervals.
- Using a stack or a list to keep track of the current merged intervals as you iterate through the input.
- Checking for overlap by comparing the end of the current interval with the start of the next interval.

---

## Typical Time Complexity
- O(n log n) if there is an initial sorting step, followed by O(n) for the merging process

---

## Common Pitfalls
- Failing to sort the intervals before processing them, which can lead to incorrect merging.
- Not handling edge cases, such as intervals that are completely contained within others or intervals that touch at endpoints.
- Forgetting to add the last merged interval to the result after the iteration is complete.

---

## Canonical Problems
- Merge Intervals (LeetCode 56)
- Insert Interval (LeetCode 57)