# Pattern: Union Find

---

## When to Use
- Grouping elements into disjoint sets based on equivalence or connectivity.
- Problems asking for connected components, whether two elements are in the same group, or merging groups.
- When relationships are given incrementally and you need efficient "same group?" queries.

---

## Core Idea
- Maintain a forest where each tree represents a group. Each element has a parent pointer; the root of the tree identifies the group.
- **Find**: follow parent pointers to the root to determine which group an element belongs to.
- **Union**: merge two groups by linking one root to the other.
- Two optimizations make both operations nearly O(1) amortized:
  - **Path compression**: during `find`, point every visited node directly to the root.
  - **Union by rank**: attach the shorter tree under the taller one to keep trees shallow.

---

## Common Techniques
- Union all related elements pairwise (e.g., union every email in an account with the first email).
- After all unions, group elements by their `find()` root to extract connected components.
- Use a hash map for parent/rank when elements are not simple integers (e.g., strings).
- Track extra metadata per group (size, name, etc.) on the root node.

---

## Typical Time Complexity
- Time: O(n * α(n)) per operation where α is the inverse Ackermann function — effectively O(1) amortized.
- Space: O(n) for parent and rank storage.

---

## Common Pitfalls
- Reading the stored parent directly instead of calling `find()` — a node's immediate parent may not be the true root after unions.
- Forgetting path compression, leading to O(n) worst-case find operations on skewed trees.
- Off-by-one with rank: initializing rank inconsistently with the comparison logic.

---

## Canonical Problems
- 721 Accounts Merge
- 200 Number of Islands
- 128 Longest Consecutive Sequence
- 684 Redundant Connection
