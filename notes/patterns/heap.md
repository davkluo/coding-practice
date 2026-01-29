# Pattern: Heap

---

## When to Use

- Problems that require efficient retrieval of the top k elements from a dynamic dataset.
- Situations where you need to maintain a running list of the largest or smallest elements.
- Scenarios where you need to efficiently merge multiple sorted lists or streams of data.

---

## Core Idea

- Utilize a heap data structure (min-heap or max-heap) to efficiently manage and retrieve the top k elements.
- Min-heap is typically used for finding the k largest elements, while max-heap is used for finding the k smallest elements.
- Heaps allow for O(log k) insertion and deletion operations, making them suitable for dynamic datasets.

---

## Common Techniques

- Use a priority queue (heap) to maintain the top k elements while iterating through the dataset.
- Implement custom comparison logic for complex data types to ensure correct ordering in the heap.
- Use a hash map in conjunction with a heap to count frequencies or aggregate data before pushing to the heap.

---

## Typical Time Complexity

- O(n log k) for maintaining a heap of size k while processing n elements.

---

## Common Pitfalls

- Not maintaining the heap size to k, leading to increased time and space complexity.
- Confusion between min-heap and max-heap usage based on the problem requirements.

---

## Canonical Problems

- Top K Frequent Elements
- Kth Largest Element in an Array
- Merge K Sorted Lists
