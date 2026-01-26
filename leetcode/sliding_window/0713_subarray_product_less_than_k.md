# 713 – Subarray Product Less Than K

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/subarray-product-less-than-k/

---

## Problem Summary

Given an array of positive integers and a positive integer k, count the number of contiguous subarrays where the product of all elements is strictly less than k.

---

## Key Insight

- For each position `r`, the number of valid subarrays ending at `r` is simply `r - l + 1`, where `l` is the smallest index such that the product of elements from `l` to `r` is less than k
- This counting trick avoids enumerating all subarrays explicitly
- Instead of precalculating all prefix products, we can maintain a running product and adjust the left pointer as needed

---

## Approach

1. Handle the edge case where `k <= 1`: since all elements are positive integers, no product can be less than 1, so return 0.
2. Initialize a left pointer `l` at index 0 and a running product starting at 1.
3. Iterate through the array with the right pointer `r`:
   - Multiply the current element into the running product.
   - While the running product is >= k, divide out the element at `l` and increment `l`.
   - After the while loop, the window `[l, r]` contains all valid subarrays ending at `r`.
   - Add `r - l + 1` to the count (representing subarrays `[r]`, `[r-1, r]`, ..., `[l, r]`).
4. Return the total count.

---

## Why This Works

- The sliding window maintains the invariant that the product of elements in `[l, r]` is always less than k after processing each `r`.
- Since all elements are positive, expanding the window (increasing `r`) can only increase the product, and shrinking the window (increasing `l`) can only decrease it. This monotonic property ensures the window adjustments are correct.
- When a single element `nums[r] >= k`, the while loop pushes `l` past `r`, resulting in `l = r + 1` and a contribution of 0 subarrays, which is correct.
- Each valid subarray is counted exactly once: when processing the rightmost element of that subarray.

---

## Edge Cases

- `k <= 1`: No valid subarrays exist (all products are >= 1).
- Single element equal to or greater than k: contributes 0 subarrays.
- Single element less than k: contributes 1 subarray.
- All elements are 1 with k > 1: all possible subarrays are valid.

---

## Time & Space Complexity

- Time: O(n) – Each element is visited at most twice (once by each pointer).
- Space: O(1) – Only a few variables are used for tracking pointers, product, and count.

---

## Common Mistakes

- Forgetting to handle `k <= 1` as a special case, which can lead to infinite loops or incorrect results.
  - Particularly when a single element is >= k, ensuring the left pointer moves correctly.
- Using integer division instead of regular division when shrinking the window (though with positive integers, either works).
- Miscounting subarrays by using `r - l` instead of `r - l + 1`.
- Trying to enumerate subarrays explicitly.

---

## Alternative Solutions

- A brute force approach would enumerate all subarrays and check each product, resulting in O(n²) time complexity.
- Using logarithms, the product constraint can be converted to a sum constraint (`log(a*b) = log(a) + log(b)`), allowing the use of prefix sums, though this introduces floating-point precision issues.
