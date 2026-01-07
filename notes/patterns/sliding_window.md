# Pattern: Sliding Window

---

## When to Use
- Problems involving contiguous subarrays or substrings.
- When you need to find optimal or specific properties within a range that can be adjusted.
    - e.g. Finding a minimum or maximum sum/length.
- Situations where recalculating results for overlapping segments is inefficient.

---

## Core Idea
- Maintain a window defined by two pointers that can expand or contract based on conditions.
    - Usually by moving the right pointer to expand and the left pointer to contract in order to maintain linear time complexity.
- Update results incrementally as the window changes.

---

## Common Techniques
- Using two pointers to represent the current window boundaries.
- Expanding the window by moving the right pointer and contracting it by moving the left pointer.
- Keeping track of necessary data (like sums, counts, or frequencies) within the window using auxiliary data structures.

---

## Typical Time Complexity
- Time Complexity: O(n) since each element is processed at most twice (once when expanding and once when contracting the window).
- Space Complexity: O(1) or O(k) depending on the auxiliary data structures used

---

## Common Pitfalls
- Failing to properly update the window boundaries, leading to incorrect results.
- Not handling edge cases, such as empty arrays or when the window size exceeds the array length.
- Failing to update state variables such as sums or counts when the window changes.

---

## Canonical Problems
- Longest Substring Without Repeating Characters
- Minimum Size Subarray Sum