# 110 – Balanced Binary Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Binary Tree, Depth-First Search
**Secondary Patterns:** Recursion, Tree Traversal  
**Link:** https://leetcode.com/problems/balanced-binary-tree/

---

## Problem Summary
Given a binary tree, determine if it is height-balanced. A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differs by more than 1.

---

## Key Insight
- A tree is balanced if both its left and right subtrees are balanced, and the difference in their heights is at most 1.
- We can recursively verify this property for each node in the tree.

---

## Approach
1. Define a recursive function `dfs` that returns two values: whether the subtree rooted at the current node is balanced, and its height.
2. For each node, recursively check its left and right children.
3. If either subtree is unbalanced, propagate that information up.
4. Calculate the height of the current node as `1 + max(left_height, right_height)`.
5. Check if the current node is balanced by ensuring the height difference between left and right subtrees is at most 1.
6. Return the balanced status and height for the current node
7. Run the `dfs` function starting from the root and return whether the entire tree is balanced.

---

## Why This Works
- The recursive approach ensures that we check every node in the tree.
- Returning the height allows us to calculate whether a node is balanced.
- Returning whether a subtree is balanced allows us to quickly short-circuit and propagate unbalanced status up the tree.

---

## Edge Cases
- Empty tree is balanced
- Single node tree is balanced

---

## Time & Space Complexity
- Time: O(n), where n is the number of nodes in the tree. We visit each node once.
- Space: O(n) in the worst case for the recursion stack.

---

## Common Mistakes
- Forgetting to check both left and right subtree balance.
- Forgetting to check subtrees for imbalanced short-circuiting.

---

## Alternative Solutions
- Iterative approach using two stacks to achieve postorder traversal and storing heights in a dictionary.