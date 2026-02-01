# Pattern: Monotonic Stack

---

## When to Use
- Finding the next greater or next smaller element for each element in an array.
- Finding the previous greater or previous smaller element.
- Problems involving "span" calculations (e.g., stock span, days until warmer temperature).
- Calculating areas of histograms or rectangles.
- Problems where you need to efficiently find bounds or ranges based on relative element sizes.

---

## Core Idea
Maintain a stack where elements are always in sorted order (either increasing or decreasing). When processing a new element, pop elements that violate the monotonic property. The popped elements have found their "answer" (next greater/smaller), and what remains on the stack provides context for future elements.

- **Monotonically Decreasing Stack**: Used to find the next greater element. Stack holds elements in decreasing order from bottom to top.
- **Monotonically Increasing Stack**: Used to find the next smaller element. Stack holds elements in increasing order from bottom to top.

---

## Common Techniques
- Iterate through the array (forward or backward depending on the problem).
- Pop elements from the stack while they violate the monotonic property relative to the current element.
- The current element becomes the "answer" for all popped elements.
- Push the current element (or its index) onto the stack.
- Store indices instead of values when you need position information.
- Use a hash map to store results when mapping between arrays.

---

## Typical Time Complexity
- Time Complexity: O(n) since each element is pushed and popped at most once.
- Space Complexity: O(n) for the stack in the worst case.

---

## Common Pitfalls
- Confusing when to use increasing vs decreasing stack (think about what you're looking for).
- Forgetting to handle remaining elements in the stack after iteration (they have no next greater/smaller).
- Off-by-one errors when storing indices vs values.
- Not considering whether to iterate forward or backward based on whether you need "next" or "previous" elements.

---

## Canonical Problems
- Next Greater Element I (LeetCode 496)
- Next Greater Element II (LeetCode 503)
- Daily Temperatures (LeetCode 739)
- Largest Rectangle in Histogram (LeetCode 84)
- Trapping Rain Water (LeetCode 42)
- Stock Span Problem (LeetCode 901)
