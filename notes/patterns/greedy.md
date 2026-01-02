# Pattern: Greedy

---

## When to Use
- Situations where making local optimal choices leads to a global optimum.
- When keeping track of a single state or a few variables is sufficient.
- When the search is constrained in one direction.

---

## Core Idea
- Make the best choice at each step without reconsidering previous choices.
- Use simple data structures to maintain state.

---

## Common Techniques
- Sorting inputs to facilitate greedy choices.
- Using priority queues to always access the next best option.
- Iterating through data in a single pass.

---

## Typical Time Complexity
- Time Complexity: O(n log n) due to sorting, or O(n) for linear scans.
- Space Complexity: O(1) or O(n) depending on the data structures used.

---

## Common Pitfalls
- Failing to prove that local optimal choices lead to a global optimum.
- Overlooking edge cases where greedy choices may not yield the best solution.

---

## Canonical Problems
- Best Time to Buy and Sell Stock