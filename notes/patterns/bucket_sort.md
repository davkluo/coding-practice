# Pattern: Bucket Sort

---

## When to Use
- When you need to sort or group elements based on a limited range of values (e.g., frequencies, scores).
- When the maximum value (or frequency) is known and not significantly larger than the number of elements.
- When you want to achieve linear time complexity O(n) for sorting or grouping.

---

## Core Idea
- Create "buckets" (lists or arrays) where each bucket corresponds to a specific range or value.
- Distribute the elements into these buckets based on their value or frequency.
- Finally, concatenate or process the buckets in order to achieve the desired result.

---

## Common Techniques
- Use a hash map to count frequencies or categorize elements.
- Create an array of lists (buckets) where the index represents the frequency or value.
- Iterate through the buckets in a specific order (e.g., from highest to lowest frequency) to gather results.

---

## Typical Time Complexity
- O(n) for distributing elements into buckets.
- O(n) for collecting elements from the buckets.
- Overall: O(n) under ideal conditions.

---

## Common Pitfalls
- Initializing buckets incorrectly (e.g., using `[[]] * n` which creates references to the same list).
- Not accounting for edge cases where all elements have the same frequency.

---

## Canonical Problems
- Top K Frequent Elements (LeetCode 347)