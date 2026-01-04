# Pattern: Two Pointer

---

## When to Use
- Situations where you need to process a sequence with two indices.
- Problems involving searching, partitioning, or comparing elements in a linear structure.
- Problems that deal with a window or subarray between the two pointers.

---

## Core Idea
Use two pointers to traverse a data structure, often moving them at different speeds or directions to achieve a specific goal.

---

## Common Techniques
- **Opposite Direction Pointers**: One pointer starts at the beginning and the other at the end, moving towards each other.
- **Same Direction Pointers**: Both pointers start at the same position and move forward, often at different speeds.
- **Sliding Window**: One pointer marks the start of a window while the other marks the end, adjusting the window size as needed.

---

## Typical Time Complexity
O(n) - Each element is processed at most twice -- once by each pointer.

---

## Common Pitfalls
- Not updating pointers correctly, leading to infinite loops.
- Failing to handle edge cases, such as empty arrays or single-element arrays.

---

## Canonical Problems
- Container With Most Water (LeetCode 11)