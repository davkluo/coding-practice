# 103 – Binary Tree Zigzag Level Order Traversal

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Breadth-First Search (BFS)
**Link:** https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

---

## Problem Summary
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

---

## Key Insight
- Use BFS to traverse the tree level by level.
- Use a flag to determine the order of insertion for each level.
- A deque can allow us to append and pop in both directions, allowing us to build the zigzag order efficiently.
- Each level is queued up in left-to-right order, but we reverse the traversal order based on the current level.
- Enqueueing happens on the opposite end of the dequeue in both cases, so we can directly enqueue without needing an auxiliary list.

---

## Approach
1. Check for an empty tree. If the root is `None`, return an empty list.
2. Initialize a queue (using `collections.deque`) and add the root node to it.
3. Initialize a result list to store the final zigzag level order traversal.
4. Use a boolean flag `left_to_right` to track the current direction of traversal, starting with `True`.
5. While the queue is not empty:
    - Run a for loop for the number of nodes currently in the queue (this represents one level of the tree).
    - If `left_to_right` is `True`, pop nodes from the left of the queue and append their values to the current level list. Enqueue their children (left, then right) to the right end of the queue.
    - If `left_to_right` is `False`, pop nodes from the right of the queue and append their values to the current level list. Enqueue their children (right, then left) to the left end of the queue.
    - After processing all nodes at the current level, append the current level list to the result list.
    - Toggle the `left_to_right` flag for the next level.
6. Return the result list after processing all levels.

---

## Why This Works
- BFS ensures that we process nodes level by level.
- Using a deque allows us to use the BFS in both directions.
- The flag alternates order of traversal, achieving the zigzag pattern.

---

## Edge Cases
- Empty root
- Single node tree

---

## Time & Space Complexity
- Time: O(n), where n is the number of nodes in the tree. Each node is processed exactly once.
- Space: O(n), in the worst case, the queue will hold all nodes at the last level of the tree.

---

## Common Mistakes
- Forgetting to toggle the `left_to_right` flag after each level.
- Not handling the case where the tree is empty.

---

## Alternative Solutions
- Use two stacks to alternate between levels, pushing nodes onto one stack while popping from the other.