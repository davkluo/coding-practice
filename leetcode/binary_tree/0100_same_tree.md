# 100 – Same Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Binary Tree
**Secondary Patterns:** Tree Traversal, Recursion  
**Link:** https://leetcode.com/problems/same-tree/

---

## Problem Summary

Given the roots of two binary trees, determine if they are identical in structure and node values.

---

## Key Insight

- We can use recursion to compare corresponding nodes in both trees, by first comparing the current nodes, then recursively checking their left and right children.
- The base case is when both nodes are null (trees are identical up to this point) or when one is null and the other is not (trees differ).
- Before we invoke the recursive calls, we should also check if the current nodes have the same value.
- Both children subtrees must also be identical for the trees to be considered the same.

---

## Approach

1. Check if both nodes are null. If so, return true.
2. If one node is null and the other is not, return false.
3. If the values of the current nodes differ, return false.
4. Recursively check the left children of both nodes and the right children of both nodes.
5. Return true only if both recursive checks return true.

---

## Why This Works

- This approach systematically checks each corresponding node in both trees, ensuring that both structure and values are identical.
- The recursive nature of the solution allows us to break down the problem into smaller subproblems, making it easier to manage and reason about.
- If both children of a node and the current node is the same, then the current subtree is the same.

---

## Edge Cases

- Both trees are empty (null).
- One tree is empty, and the other is not.
- Trees with only one node.

---

## Time & Space Complexity

- Time: O(min(n, m)) where n and m are the number of nodes in the two trees. In the worst case, we may need to traverse all nodes of the smaller tree.
- Space: O(h) where h is the height of the tree, due to the recursion stack. In the worst case (skewed tree), this could be O(n).

---

## Common Mistakes

- Forgetting to check for null nodes before accessing their values.
- Not checking the values of the nodes before making recursive calls.
- Forgetting to use a logical AND when combining the results of left and right subtree checks.

---

## Alternative Solutions

- Iterative approach using a stack or queue to perform a breadth-first or depth-first traversal of both trees simultaneously.
