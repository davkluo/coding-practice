# Pattern: Graph Traversal

---

## When to Use
- Problems involving graphs where you need to visit all nodes or edges, such as searching, pathfinding, or connectivity checks.
- Situations where you need to explore all possible states or configurations represented as a graph.

---

## Core Idea
- Systematically visit all nodes and edges in a graph using either Depth-First Search (DFS) or Breadth-First Search (BFS).
- Maintain a record of visited nodes to avoid cycles and redundant work.

---

## Common Techniques
- **Depth-First Search (DFS):** Explore as far down a branch as possible before backtracking. Can be implemented using recursion or an explicit stack.
- **Breadth-First Search (BFS):** Explore all neighbors at the present depth prior to moving on to nodes at the next depth level. Typically implemented using a queue.
- **Visited Set:** Use a hash set or map to track visited nodes to prevent infinite loops in cyclic graphs.
- **Graph Representation:** Use adjacency lists, adjacency matrices, or edge lists to represent the graph structure.

---

## Typical Time Complexity
- O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

---

## Common Pitfalls
- Failing to mark nodes as visited, leading to infinite loops in cyclic graphs.
- Incorrectly handling disconnected graphs when the problem requires visiting all components.
- Mismanaging the data structure used for traversal (stack vs. queue) leading to incorrect traversal order.

---

## Canonical Problems
- Clone Graph (LeetCode 133)