# Pattern: Prefix Sum

---

## When to Use
- Problems that require cumulative sums or products over a range of indices.
- Situations where you need to efficiently calculate the sum or product of subarrays multiple times.
- Scenarios where you want to avoid recomputing sums/products from scratch for overlapping subarrays.

---

## Core Idea
- Precompute a prefix sum (or product) array where each element at index `i` contains the sum (or product) of all elements from the start of the array up to index `i`.
- Use the prefix array to quickly calculate the sum (or product) of any subarray by subtracting the appropriate prefix sums (or dividing the appropriate prefix products).

---

## Common Techniques
- Create a prefix sum/product array. If possible consider using a single variable to store cumulative values to save space.
- Use two-pointer technique in conjunction with prefix sums/products for range queries.

---

## Typical Time Complexity
- O(n) for preprocessing the prefix sum/product array.
- O(1) for each range sum/product query after preprocessing.

---

## Common Pitfalls
- Forgetting to handle edge cases, such as empty arrays or single-element arrays.
- Miscalculating indices when using the prefix array to compute subarray sums/products.

---

## Canonical Problems
- Product of Array Except Self (LeetCode 238)