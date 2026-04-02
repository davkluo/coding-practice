# 785 – Is Graph Bipartite?

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Graph / BFS
**Link:** https://leetcode.com/problems/is-graph-bipartite/

---

## Problem Summary

Given an undirected graph as an adjacency list, determine whether it can be colored with two colors such that no two adjacent nodes share the same color (i.e., is it bipartite).

---

## Key Insight

- A graph is bipartite if and only if it contains no odd-length cycle.
- Equivalently, it is 2-colorable: you can assign every node to one of two groups such that every edge crosses between groups, never within one.
- BFS naturally propagates color assignments level by level, so a conflict (neighbor has the same color as the current node) is immediately detectable.

---

## Approach

1. Initialize an `assignments` array of length `n` with all zeros (unassigned), as well as a set to track processed nodes.
2. For each unvisited node, launch a BFS from it to handle disconnected components.
3. In the BFS, if a node has no assignment yet, assign it color 1.
4. For each neighbor of the current node, compute the opposite color.
   - If the neighbor is unassigned, assign the opposite color and enqueue it.
   - If the neighbor is already assigned the **same** color as the current node, return `False`.
5. If BFS completes without conflict, return `True`.
6. If any BFS call returns `False`, the graph is not bipartite; if they all succeed, it is.

---

## Why This Works

- Bipartiteness requires every edge to connect nodes in opposite sets. BFS explores the graph in layers, so by the time we process a node's neighbors we know exactly which color they must be. A same-color collision means an odd cycle exists, which makes 2-coloring impossible.
- The outer loop over all nodes ensures disconnected components are all checked — a graph is only bipartite if every component is.

---

## Edge Cases

- Isolated nodes (no edges): trivially bipartite; the BFS assigns them a color and terminates with no conflicts.
- Disconnected graph: must check every component; a single non-bipartite component makes the whole graph non-bipartite.
- Two-node graph with one edge: bipartite.
- Even cycle: bipartite.
- Odd cycle: not bipartite.

---

## Time & Space Complexity

- Time: O(V + E) — each node and edge is visited once across all BFS calls
- Space: O(V) — the `assignments` array and the BFS queue each hold at most V entries

---

## Common Mistakes

- **Processing neighbors before checking if they're already visited:** in this solution, neighbors are enqueued unconditionally and the `processed` set guards against re-processing. An alternative is to only enqueue unvisited neighbors, which avoids the set entirely.
- **Forgetting disconnected components:** only looping until the first visited node would miss isolated or separately connected components.

---

## First Attempt: Linear Scan (Wrong)

The initial idea was to iterate over nodes in index order, assign color 1 to any unassigned node, then assign the opposite color to all of its neighbors listed in the adjacency list — without doing a full traversal.

This fails because the adjacency list order is arbitrary with respect to graph connectivity. When you encounter a node that is already a neighbor of a previously colored node but hasn't been assigned yet, you might assign it the wrong color before you've processed its own neighbors. More critically, two nodes that appear sequentially in the index list might actually be in the same connected component and already constrained by each other — a linear scan has no way to know this without following edges.

BFS fixes this by respecting the actual connectivity: every node is colored in relation to its graph neighbors, not its index neighbors.

---

## Alternative Solutions

- DFS: functionally equivalent to BFS for this problem; propagate color assignments recursively and check for same-color conflicts.
- Union-Find: for each node `u`, union all of its neighbors together. Then check that `u` and each of its neighbors are in different sets. Requires a bipartite-aware union-find (grouping the "opposite" side together).
