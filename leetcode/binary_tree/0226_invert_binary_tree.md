# 226 – Invert Binary Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Binary Tree 
**Link:** https://leetcode.com/problems/invert-binary-tree/

---

## Problem Summary
Given the root of a binary tree, invert the tree, and return its root.

---

## Key Insight
- Inverting a binary tree means swapping the left and right children of every node in the tree.

---

## Approach
1. Check if root is None. If it is, return None.
2. Initialize a stack with the root node.
3. While the stack is not empty:
   - Pop a node from the stack.
   - Swap its left and right children.
   - If the left child is not None, push it onto the stack.
   - If the right child is not None, push it onto the stack.
4. Return the root of the inverted tree.

---

## Why This Works
- It uses DFS to traverse every node in the tree, ensuring that all nodes are visited and their children swapped.

---

## Edge Cases
- Null root
- Single node tree

---

## Time & Space Complexity
- Time: O(n), where n is the number of nodes in the tree.
- Space: O(n) in the worst case for the stack.

---

## Common Mistakes
- Forgetting to check for None nodes before pushing them onto the stack.

---

## Alternative Solutions
- Recursive DFS is a similar approach.
- BFS using a queue instead of a stack to traverse the tree level by level. Swapping children functions the same.