# 743 – Network Delay Time

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Graph (Dijkstra's / Shortest Path)
**Link:** https://leetcode.com/problems/network-delay-time/

---

## Problem Summary

Given a directed, weighted graph of n nodes and a source node k, find the minimum time for a signal to reach all nodes. Return -1 if any node is unreachable.

---

## Key Insight

- The time for all nodes to receive the signal is the maximum shortest-path distance from k to any node — this is exactly what Dijkstra's algorithm computes.

---

## Approach

1. Build an adjacency list from the edge list.
2. Initialize a distance map with infinity for all nodes, setting the source node k to 0.
3. Use a min-heap seeded with `(0, k)`.
4. Pop the smallest-distance node; skip if already processed.
5. For each neighbor, relax the edge: if the new distance is shorter, update and push to the heap.
6. After the heap is exhausted, return the max value in the distance map. If it's infinity, return -1.

---

## Why This Works

- Dijkstra's greedy property guarantees that when a node is popped from the heap, its shortest distance is finalized — all non-negative edge weights mean no future path can improve it.
- The answer is `max(dist)` because the signal propagates in parallel along all paths; the bottleneck is the node that takes longest to reach.

---

## Edge Cases

- Single node, no edges: answer is 0 (signal is already at the source)
- Disconnected node: distance stays infinity, return -1
- Multiple paths to the same node: relaxation ensures the shortest is kept

---

## Time & Space Complexity

- Time: O(E log V) — each edge may cause a heap push, each push/pop is O(log V)
  - Each edge can potentially introduce a heap push and subsequent pop
  - There are up to E elements in the heap, since a node can be pushed multiple times with different distances, meaning each operation is O(log E)
  - For a simple graph, E can be up to V^2 in the worst case, but typically E is much less than V^2
  - O(E log E) is therefore bounded by O(E log V) since E is at most V^2, and log E is at most 2 log V. The factor of 2 gets dropped.
- Space: O(V + E) — adjacency list and distance map

---

## Common Mistakes

- Forgetting to skip already-processed nodes (leads to redundant work or incorrect results with stale entries)
- Returning the max distance without checking for infinity (unreachable nodes)

---

## Alternative Solutions

- **Bellman-Ford**: O(V·E), handles negative weights but slower here since all weights are positive
