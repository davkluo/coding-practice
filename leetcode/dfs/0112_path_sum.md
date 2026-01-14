# 112 – Path Sum

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Depth-First Search (DFS)
**Secondary Patterns:** Tree Traversal  
**Link:** https://leetcode.com/problems/path-sum/

---

## Problem Summary
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

---

## Key Insight
- A root-to-leaf path means we need to check the sum of values leading up to every leaf node. This is a natural base case for a DFS traversal.

---

## Approach
1. Check if the current node is null. If it is, return false.
2. Create a stack to hold pairs of (node, current_sum) and initialize it with the root and a sum of 0.
3. While the stack is not empty:
   - Pop a node and its associated sum from the stack.
   - Add the node's value to the current sum.
   - If the node is a leaf (no left or right children), check if the current sum equals targetSum. If it does, return true.
   - If the node has a left child, push it onto the stack with the updated sum.
   - If the node has a right child, push it onto the stack with the updated sum.
4. If we exit the while loop without finding the path sum, return false.

---

## Why This Works
- All paths are explored using DFS, ensuring that every root-to-leaf path is checked.

---

## Edge Cases
- Empty root
- Single node tree where the node's value equals targetSum

---

## Time & Space Complexity
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(n) in the worst case for the stack.

---

## Common Mistakes
- Forgetting to check if the current node is a leaf before comparing sums.

---

## Alternative Solutions
- Recursive DFS approach.
- BFS is equally viable as long as we track the current sum in the queue, but perhaps less intuitive.