# Pattern: Binary Tree

---

## When to Use
- Problems involving hierarchical data structures where each node has at most two children.
- Binary tree is given in the problem.

---

## Core Idea
- Traverse the tree using DFS or BFS to visit each node.
- Perform operations on each node as required by the problem (e.g., swapping children, calculating values).
- Utilizing the left and right pointers to navigate through the tree structure.

---

## Common Techniques
- Depth-First Search (DFS) using recursion or an explicit stack.
- Breadth-First Search (BFS) using a queue.
- Uses a tree node class with left and right pointers.

---

## Typical Time Complexity
- O(n), where n is the number of nodes in the tree, since each node is visited once.

---

## Common Pitfalls
- Forgetting to handle null nodes when traversing the tree.
- Mismanaging the left and right pointers during operations.

---

## Canonical Problems
- Invert Binary Tree (LeetCode 226)