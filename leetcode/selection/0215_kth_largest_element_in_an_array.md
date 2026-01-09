# 215 – Kth Largest Element in an Array

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Selection
**Secondary Patterns:** Heap, Quickselect
**Link:** https://leetcode.com/problems/kth-largest-element-in-an-array/

---

## Problem Summary
Given an integer array `nums` and an integer `k`, return the kᵗʰ largest element in the array. Try to solve it without sorting.

---

## Key Insight
- Using a min-heap of size `k` to keep track of the k largest elements.
    - This works because the smallest elements other than the k largest can be discarded.
    - The root of the min-heap will be the kᵗʰ largest element after processing all elements.
- Alternatively, using the Quickselect algorithm to find the kᵗʰ largest element in average O(n) time.

---

## Approach
### Min-Heap Approach:
1. Initialize a min-heap.
2. Iterate through each number in `nums`:
    - Add the number to the heap.
    - If the size of the heap exceeds `k`, remove the smallest element (the root).
3. After processing all numbers, the root of the min-heap will be the kᵗʰ largest element.

### Quickselect Approach:
1. Implement a partition function that rearranges elements based on a pivot.
    - Elements greater than the pivot go to the left, and those less go to the right.
2. Use the partition function to recursively narrow down the search space until the kᵗʰ largest element is found.
    - The kᵗʰ largest element corresponds to the element in the k-1 index in a zero-indexed reverse sorted array.

---

## Why This Works
- The min-heap approach efficiently maintains the k largest elements, ensuring that we only keep what is necessary to determine the kᵗʰ largest.
- The Quickselect approach leverages the partitioning logic of QuickSort to efficiently find the desired element without fully sorting the array.
    - Every partition step makes sure the pivot is in its final sorted position, allowing us to check if it is the kᵗʰ largest or if we need to search further by narrowing down onto one side of the partition.

---

## Edge Cases
- If `k` is equal to the length of `nums`, the smallest element in the array is returned.
- If `nums` contains duplicate elements, the algorithm still correctly identifies the kᵗʰ largest unique value.
- Single element array where `k` is 1.

---

## Time & Space Complexity
- Time: 
    - Min-Heap: O(n log k) where n is the number of elements in `nums`.
    - Quickselect: Average O(n), Worst O(n²) in case of poor pivot choices.
- Space:
    - Min-Heap: O(k) for the heap.
    - Quickselect: O(1) additional space (in-place).

---

## Common Mistakes
- Not maintaining the size of the heap correctly, leading to incorrect results.
- Popping from the heap before adding new elements, which can lead to losing potential candidates for the kᵗʰ largest.
    - For example if the newly added element is smaller than the smallest in the heap, it should be the one to be discarded.

---

## Alternative Solutions
- Sorting the entire array and returning the element at index `len(nums) - k`. This is straightforward but has a time complexity of O(n log n), which is less efficient than the other methods.