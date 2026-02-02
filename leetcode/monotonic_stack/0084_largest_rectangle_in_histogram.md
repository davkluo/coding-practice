# 84 – Largest Rectangle in Histogram

**Platform:** LeetCode
**Difficulty:** Hard
**Primary Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/largest-rectangle-in-histogram/

---

## Problem Summary

Given an array of integers representing histogram bar heights (each with width 1), find the area of the largest rectangle that can be formed within the histogram.

---

## Key Insight

- For each bar, the largest rectangle using that bar's height extends left and right until hitting a shorter bar.
- We need to efficiently find the **previous smaller** and **next smaller** elements for each bar—exactly what a monotonic increasing stack provides.

---

## Approach

1. Use a monotonic increasing stack to find `prev_smaller[i]` — the index of the nearest bar to the left that is strictly shorter (or -1 if none exists)
   - Iterate through `heights` from left to right
   - While the stack is not empty and the height at the top of the stack is greater than or equal to the current height, pop from the stack
   - The top of the stack (if any) is the index of the previous smaller element
   - Push the current index onto the stack
2. Use another pass with a monotonic increasing stack to find `next_smaller[i]` — the index of the nearest bar to the right that is strictly shorter (or `len(heights)` if none exists)
   - Iterate through `heights` from right to left
   - Similar logic as above, but in reverse
3. For each bar `i`, compute the width as `(next_smaller[i] - 1) - prev_smaller[i]`, which represents the span where bar `i` is the minimum height
4. Calculate area as `heights[i] * width` and track the maximum

---

## Why This Works

- Each bar can only extend horizontally until it encounters a shorter bar. The monotonic increasing stack maintains indices in ascending order of height, so when we encounter a new element, we pop all elements ≥ current height—the remaining top is guaranteed to be the previous smaller element. This gives O(1) amortized lookup per element.

---

## Edge Cases

- Single bar: rectangle is just that bar's height × 1
- All bars same height: rectangle spans entire width
- All zeros: answer is 0
- Strictly increasing/decreasing: each bar's rectangle limited by neighbors

---

## Time & Space Complexity

- Time: O(n) — each element pushed and popped at most once per stack
- Space: O(n) — storing the two dictionaries and the stack

---

## Common Mistakes

- Off-by-one errors in width calculation: width = `(next_smaller[i] - 1) - prev_smaller[i]`, not `next_smaller[i] - prev_smaller[i] - 1` (though mathematically equivalent, the grouping matters for understanding)
- Using `>` instead of `>=` when popping: must pop equal heights too, otherwise we find "previous smaller or equal" instead of "previous smaller"
- Forgetting sentinel values: -1 for left boundary, `len(heights)` for right boundary

---

## Alternative Solutions

- **Single-pass stack:** Process elements and compute areas when popping from the stack, avoiding the need for two separate passes

  ```python
  def largest_rectangle_area(self, heights: List[int]) -> int:
      heights = heights + [0]  # append sentinel to flush the stack
      stack = []
      largest_area = 0

      for i, h in enumerate(heights):
          while stack and heights[stack[-1]] >= h:
              popped_height = heights[stack.pop()]
              left_bound = stack[-1] if stack else -1
              width = i - left_bound - 1
              largest_area = max(largest_area, popped_height * width)
          stack.append(i)

      return largest_area
  ```
