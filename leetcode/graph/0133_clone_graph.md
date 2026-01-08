# 133 – Clone Graph

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Graph Traversal
**Secondary Patterns:** Depth-First Search (DFS), Breadth-First Search (BFS) 
**Link:** https://leetcode.com/problems/clone-graph/

---

## Problem Summary
Given a reference of a node in a connected undirected graph, return a deep copy of the graph. Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

---

## Key Insight
- Graphs can be traversed using DFS or BFS.
- Use a hash map to keep track of cloned nodes to avoid cycles and duplicate work.
- Create a node copy when first encountered either by processing its neighbors or when visiting it.
- Populate the neighbors of the cloned nodes when they are processed/traversed.
- The map of cloned nodes can also play the part of a visited set to prevent re-processing nodes.

---

## Approach
1. If the input node is `None`, return `None`.
2. Initialize a hash map to store the mapping from original nodes to their clones.
3. Initialize a stack for DFS (or a queue for BFS) and add the input node to it.
4. While the stack/queue is not empty:
   - Pop a node from the stack/queue.
   - If the node is not in the hash map, create a clone and add it to the map.
   - For each neighbor of the current node:
     - If the neighbor is not in the hash map, create a clone and add it to the map, then push it onto the stack/queue.
     - Add the cloned neighbor to the neighbors list of the cloned current node.
5. Return the clone of the input node from the hash map.

---

## Why This Works
- The algorithm ensures that each node is cloned exactly once and that all connections (edges) are preserved.
- Using a hash map to track traversal prevents infinite loops in cyclic graphs and ensures that each node's neighbors are correctly linked to their respective clones.

---

## Edge Cases
- Input graph is empty (i.e., the input node is `None`).
- Graph with a single node and no edges.

---

## Time & Space Complexity
- Time: O(V + E), where V is the number of vertices (nodes) and E is the number of edges in the graph.
- Space: O(V), for storing the cloned nodes in the hash map.
    - The stack or queue can also take up to O(V) space in the worst case.
    - The edges are not auxiliary space since they are part of the output graph.

---

## Common Mistakes
- Forgetting to check if a node has already been cloned before creating a new clone.
- Not properly initializing clones when populating neighbors, and instead using the original nodes.
- Failing to handle the case where the input node is `None`.
- Not considering cycles in the graph, leading to infinite loops.

---

## Alternative Solutions
- BFS can be used instead of DFS for graph traversal.
- Recursive DFS can be implemented instead of iterative DFS using a stack.