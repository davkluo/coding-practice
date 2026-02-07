# 199 – Binary Tree Right Side View

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Breadth-First Search (BFS)
**Secondary Pattern:** Tree Traversal, Depth-First Search (DFS)
**Link:** https://leetcode.com/problems/binary-tree-right-side-view/

---

## Problem Summary

Given the root of a binary tree, return the values of the nodes you can see ordered from top to bottom when looking at the tree from the right side.

---

## Key Insight

- This is essentially the rightmost node at each level of the tree.
- We can use a level-order traversal (BFS) to capture the last node of each level, or we can use a depth-first traversal (DFS) prioritizing the right child to capture the first node at each depth.

---

## Approach

1. Check if the root is null. If it is, return an empty list.
2. Initialize a queue for BFS and a list to store the right side view.
3. Perform a level-order traversal:
   - For each level, iterate through the nodes in the queue and add their children to the queue for the next level.
   - Add the value of the last node in the level to the right side view list.
4. Return the right side view list.

---

## Why This Works

- By traversing level by level and capturing the last node of each level, we ensure that we are getting the rightmost node visible from that level.

---

## Edge Cases

- Null tree (should return an empty list).
- Tree with only one node (should return a list with that single node).
- Tree with multiple levels where some levels have only one node (should still capture the rightmost node correctly).

---

## Time & Space Complexity

- Time: O(n), where n is the number of nodes in the tree, since we need to visit each node once.
- Space: O(n) in the worst case either to store the queue (in case of a complete binary tree) or to store the right side view (in case of a skewed tree).

---

## Common Mistakes

- Forgetting to check for null root at the beginning.
- Not correctly identifying the last node of each level in the BFS traversal.

---

## Alternative Solutions

- Using DFS with a helper function that takes the current depth and updates the right side view list when it encounters a new depth for the first time (prioritizing the right child).
  - Requires an additional parameter to track the maximum depth and a check to ensure we only add the first node encountered at each depth.
  - Initial depth would be 0, and we would call the helper function on the root node with a depth of 1.
  - When we encounter a new depth, we add the node's value to the right side view list and update the maximum depth seen so far.
