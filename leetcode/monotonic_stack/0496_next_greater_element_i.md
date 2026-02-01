# 496 – Next Greater Element I

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Monotonic Stack
**Link:** https://leetcode.com/problems/next-greater-element-i/

---

## Problem Summary

Given two arrays `nums1` (a subset of `nums2`) and `nums2`, for each element in `nums1`, find the first element to its right in `nums2` that is greater. Return -1 if no such element exists.

---

## Key Insight

- A monotonic decreasing stack can efficiently track the next greater elements as we iterate through `nums2` backwards.
- As we traverse backwards through `nums2`, for each number, we can essentially pop all smaller elements from the existing stack because any number they would have been the next greater for will now have this current number as their next greater.

---

## Approach

1. Initialize an empty stack and a hash map `next_greater`
2. Iterate through `nums2` from right to left:
   - While the stack is non-empty and the current element is greater than the top of the stack:
     - Pop the stack
   - If the stack is empty after popping, it means there is no greater element to the right, so map the current element to -1.
   - Otherwise, map the current element to the top of the stack (the next greater element).
   - Push the current element onto the stack
3. Finally, construct the result for `nums1` using the `next_greater` map and return it.

---

## Why This Works

- The stack maintains a **monotonically decreasing** sequence of elements that represent potential next greater elements for the upcoming numbers. By processing `nums2` from right to left, we ensure that when we encounter a number, all elements to its right have already been processed and the stack contains only those that are greater than the current number.
- We essentially condense the numbers such that any decreasing regions are eliminated, leaving only the next greater candidates.
- After collapsing the decreasing region between a number and its next greater, the top of the stack will always be the next greater element for that number.

---

## Edge Cases

- `nums1` has only one element with no greater element to its right → return [-1]
- All elements in `nums2` are in decreasing order → all map to -1
- `nums1` and `nums2` are identical → standard case

---

## Time & Space Complexity

- Time: O(n + m) where n = len(nums2), m = len(nums1). Each element pushed/popped once.
- Space: O(n) for the stack and hash map

---

## Common Mistakes

- Processing `nums1` directly instead of precomputing for all of `nums2`
- Forgetting that elements left in the stack have no next greater element
- Using a monotonically increasing stack instead of decreasing

---

## Alternative Solutions

- Iterate left to right through `nums2` for the same complexity
  - For every element, pop smaller elements from the stack until you find a greater one or the stack is empty.
  - For each of these smaller elements, record the current element as their next greater.
  - For all remaining elements in the stack after processing, map them to -1.
