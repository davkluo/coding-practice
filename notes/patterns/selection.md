# Pattern: Selection

---

## When to Use
- Problems that require finding the kᵗʰ smallest or largest element in a collection without fully sorting it.
- Scenarios where partial ordering is sufficient, and full sorting would be inefficient.
- Situations where you need to maintain a dynamic set of top-k elements as new data arrives.

---

## Core Idea
- Utilize data structures like heaps (min-heap or max-heap) to efficiently track the k smallest or largest elements.
- Implement selection algorithms like Quickselect that partition the data to isolate the desired element without full sorting
- Leverage properties of ordering to reduce the problem size iteratively.

---

## Common Techniques
- **Heaps:** Use a min-heap to keep track of the k largest elements or a max-heap for the k smallest elements.
- **Quickselect Algorithm:** A selection algorithm that works similarly to QuickSort, partitioning the array around a pivot to find the kᵗʰ smallest or largest element.
- **Partial Sorting:** Techniques that sort only a portion of the data to find the desired element efficiently.

---

## Typical Time Complexity
- O(n log k) for heap-based approaches, where n is the number of elements and k is the number of elements to select.
- O(n) on average for Quickselect, with a worst-case of O(n²) depending on pivot selection.

---

## Common Pitfalls
- Failing to maintain the size of the heap correctly, leading to incorrect results.
- Not handling edge cases such as duplicate elements or when k equals the size of the array.
- Inefficient pivot selection in Quickselect, which can degrade performance to O(n²).

---

## Canonical Problems
- Kth Largest Element in an Array (LeetCode 215)