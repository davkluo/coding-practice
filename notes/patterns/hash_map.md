# Pattern: Hash Map

---

## When to Use
Situations where you need to store and quickly lookup previously seen elements, especially when checking for complements or pairs.

---

## Core Idea
Utilize a hash map to store elements as you iterate through a collection, allowing for O(1) average time complexity lookups to find complements or related values.

---

## Common Techniques
- Storing indices or counts of elements in the hash map.
- Checking for the existence of a complement before inserting the current element.

---

## Typical Time Complexity
- O(n) for single-pass solutions where n is the number of elements in the input collection.

---

## Common Pitfalls
- Insertion vs. lookup order, which can cause missed matches or incorrect results.
- Reusing the same entry improperly (e.g., using one element for multiple roles).
- Failing to handle duplicates, null/undefined or special values, and the semantics of equality for complex keys.
- Overlooking hash collisions, load factors, or resizing costs that can affect performance.
- Assuming constant-time operations in all cases without accounting for implementation-specific behavior.

---

## Canonical Problems
- Two Sum (LeetCode 1)