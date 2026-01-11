# 238 – Product of Array Except Self

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Prefix Sum
**Link:** https://leetcode.com/problems/product-of-array-except-self/

---

## Problem Summary
Given an integer array `nums`, return an array `answer` such that `answer[i]` 
is equal to the product of all the elements of `nums` except `nums[i]`. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer. You must write an algorithm that runs in O(n) time and without using the division operation.

---

## Key Insight
- Using prefix and suffix products to compute the result without division.
- Constant space can be achieved by simply reusing the output array for intermediate results.
- Constant space can be achieved using two variables to track prefix and suffix products during a single pass.
- We can avoid special logic for the first and last elements by initializing prefix and suffix products to 1, and assigning the products to the index before multiplying by the current element.

---

## Approach
1. Initialize an output array `output` of the same length as `nums`, filled with `None`. 1s can also be used since they are neutral for multiplication.
2. Initialize two variables `prefix_product` and `suffix_product` to 1.
3. Iterate through the array from left to right:
   - For each index `i`, set `output[i]` to `prefix_product`.
   - Update `prefix_product` by multiplying it with `nums[i]`.
4. Iterate through the array from right to left:
   - For each index `i`, multiply `output[i]` by `suffix_product`.
   - Update `suffix_product` by multiplying it with `nums[i]`.
5. Return the `output` array.

---

## Why This Works
- The first pass computes the product of all elements to the left of each index.
- The second pass computes the product of all elements to the right of each index and combines it with the left product.
- This ensures that each index in the output array contains the product of all elements except the one at that index.

---

## Edge Cases
- Arrays with zeros: Ensure that the algorithm correctly handles cases where one or more elements are zero.
- Arrays with negative numbers: Verify that the product sign is handled correctly.
- Array with only two elements: Ensure the algorithm works for the smallest non-trivial case.

---

## Time & Space Complexity
- Time: O(n)
    - We make two passes through the array, each taking linear time.
- Space: O(1)
    - We use a constant amount of extra space for the prefix and suffix products, and the output array does not count towards space complexity as per problem constraints.

---

## Common Mistakes
- Using division to compute the product, which is not allowed.
- Not handling zeros correctly, leading to incorrect products.
- Forgetting to initialize the prefix and suffix products to 1, which can lead to incorrect results for the first and last elements.
- The second pass should multiply its values into the output array rather than overwriting them.

---

## Alternative Solutions
- Using two separate arrays for prefix and suffix products, then combining them with addition. This approach uses O(n) space but is simpler to implement.