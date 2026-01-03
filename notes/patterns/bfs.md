# Pattern: Breadth-First Search (BFS)

---

## When to Use
- Traversing or searching tree or graph data structures level by level.
- Finding the shortest path in unweighted graphs.

---

## Core Idea
- Utilize a queue to explore nodes layer by layer, ensuring all nodes at the current depth are processed before moving to the next depth level.
- This approach is particularly useful for problems that require level order traversal or shortest path calculations.
- Assumes uniform edge weights in graphs for shortest path scenarios.

---

## Common Techniques
- Use a queue data structure to keep track of nodes to be explored.
- Track levels by processing all nodes currently in the queue before moving to the next level.
- Mark nodes as visited to avoid cycles in graph traversals.

---

## Typical Time Complexity
- O(V + E) for graphs, where V is the number of vertices and E is the number of edges.
- O(n) for trees, where n is the number of nodes.

---

## Common Pitfalls
- Forgetting to mark nodes as visited, leading to infinite loops in cyclic graphs.
- Not correctly managing the queue, which can lead to incorrect level processing.
- Misunderstanding the problem requirements, such as needing level order traversal versus depth-first traversal.

---

## Canonical Problems
- Binary Tree Level Order Traversal