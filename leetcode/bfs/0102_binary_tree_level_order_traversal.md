# 102 – Binary Tree Level Order Traversal

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Breadth-First Search (BFS)
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/

---

## Problem Summary
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

---

## Key Insight
- Use a queue to facilitate level-by-level traversal.
- At each level, process all nodes currently in the queue (using the current queue length) to capture their values and enqueue their children for the next level.

---

## Approach
1. If the root is null, return an empty list.
2. Initialize a queue and add the root node to it.
3. While the queue is not empty:
    - Initialize an empty list to hold the values of nodes at this level.
    - Determine the number of nodes at the current level (the current size of the queue).
    - For each node at this level:
        - Dequeue the node, add its value to the level list.
        - Enqueue its left and right children if they exist.
    - Append the level list to the result list.
4. Return the result list after processing all levels.

---

## Why This Works
- The queue structure ensures that nodes are processed in the order they are encountered, which is essential for level order traversal.
- Processing all nodes at the current level before moving to the next ensures that we capture the correct grouping of node values.

---

## Edge Cases
- Empty input
- Single node tree

---

## Time & Space Complexity
- Time: O(n), where n is the number of nodes in the tree. Each node is processed exactly once.
- Space: O(m), where m is the maximum number of nodes at any level in the tree. This corresponds to the maximum size of the queue.

---

## Common Mistakes
- Appending the node itself instead of its value to the level list.
- Not handling the case where the tree is empty.
- Forgetting to check for null children before enqueuing.

---

## Alternative Solutions
- BFS is the ideal approach for this problem. A DFS approach could be used, but it would require additional logic to track levels and is less intuitive for level order traversal.