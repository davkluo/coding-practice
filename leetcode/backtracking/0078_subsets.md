# 78 – Subsets

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/subsets/

---

## Problem Summary
Given an integer array `nums` of unique elements, return all possible subsets (the power set).

---

## Key Insight
- Each element can either be included or excluded from a subset, resulting in `2^n` possible subsets for `n` elements.
- To avoid duplicates, we can use an index to track our position in the array and only consider elements from that index onward.

---

## Approach
1. Initialize a list to hold all subsets (power set).
2. Use a backtracking function that takes the current subset (not including the element at the current index) and the current index:
    - Add the current subset to the power set.
    - For each index from the current index to the end of the array:
        - Include the element at the current index in the subset.
        - Recursively call the backtracking function with the next index.
        - Backtrack by removing the last added element.
3. Start the backtracking with an empty subset and index `0`.
4. Return the power set.

---

## Why This Works
- The key is the for loop in the backtracking function, which ensures that each recursive call considers only the elements that come after the current index.
- The key detail is that when we loop through the indices, we skip over all numbers until that index. This implements the above realization that each subset is a configuration of included/excluded elements.

---

## Edge Cases
- Single element array.

---

## Time & Space Complexity
- Time: O(2^n * n) – There are `2^n` subsets, and copying each subset to the resulting power set takes O(n) time.
- Space: O(2^n * n) – The space required to store all subsets in the power set.

---

## Common Mistakes
- Not handling duplicate subsets
- The for-loop solution automatically avoids duplicates by only considering elements after the current index.
- If doing an approach where we branch into including/excluding each element, we must only add to the power set in the branch where we include the element. This is because if we don't include it, an earlier branch would have already added that subset.

---

## Alternative Solutions
- Iterative approach that builds subsets by adding each element to existing subsets, doubling the number of subsets at each step.