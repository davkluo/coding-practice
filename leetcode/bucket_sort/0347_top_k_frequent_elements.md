# 347 – Top K Frequent Elements

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Bucket Sort
**Link:** https://leetcode.com/problems/top-k-frequent-elements/

---

## Problem Summary
Given an array of integers and an integer k, return the k most frequent elements in any order. The algorithm should have a time complexity better than O(n log n).

---

## Key Insight
- Using a bucket sort approach allows us to group elements by their frequency efficiently since the maximum frequency of any element cannot exceed the length of the array.
- Sorting by other means or using a heap would not meet the time complexity requirement.

---

## Approach
1. Count the frequency of each element using a hash map (dictionary).
2. Create a list of buckets where the index represents the frequency, and each bucket contains a list of elements with that frequency.
3. Iterate through the buckets in reverse order (from highest frequency to lowest) and collect elements until we have k elements.
4. Return the collected elements once we reach k.

---

## Why This Works
- The bucket sort method leverages the fact that frequencies are bounded by the size of the input array, allowing us to avoid more complex sorting algorithms.
- By directly accessing buckets based on frequency, we can efficiently gather the top k frequent elements.

---

## Edge Cases
- Single element array.
- All elements are the same.
- k equals the number of unique elements.

---

## Time & Space Complexity
- Time: O(n)
    - Counting frequencies takes O(n).
    - Creating buckets takes O(n).
    - Collecting top k elements takes O(n) in the worst case.
- Space: O(n)
    - The frequency map and buckets both require O(n) space in the worst case.
---

## Common Mistakes
- Using a sorting algorithm that exceeds O(n log n) time complexity.
- Initializing a bucket list of lists using `[[]] * (n + 1)` which creates references to the same list.

---

## Alternative Solutions
- Using a max-heap to keep track of the top k elements, which would have a time complexity of O(n log k).