# 101 – Symmetric Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Binary Tree
**Secondary Pattern:** Breadth-First Search (BFS), Depth-First Search (DFS)
**Link:** https://leetcode.com/problems/symmetric-tree/

---

## Problem Summary

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

---

## Key Insight

- Traversing the tree level by level and checking if each level is a palindrome can determine if the tree is symmetric.
- Alternatively, a recursive approach can compare the left and right subtrees directly.

---

## Approach

### Iterative BFS

1. Initialize two queues for traversal of the tree in opposite directions (left-to-right and right-to-left) with the root node.
2. While both queues are not empty:
   - Pop nodes from both queues.
   - If both nodes are `None`, continue to the next iteration.
   - If one node is `None` and the other is not, return `False`.
   - If the values of the nodes are different, return `False`.
   - Enqueue the children of the first node into the first queue (left child first, then right child) and the children of the second node into the second queue (right child first, then left child).
3. Return `True` if both queues are empty at the end.

### Recursive DFS

1. Define a helper function that takes two nodes as arguments.
2. If both nodes are `None`, return `True`.
3. If one node is `None` and the other is not, return `False`.
4. Return the logical AND of the following:
   - The values of the two nodes are equal.
   - The recursive call on the left child of the first node and the right child of the second node returns `True`.
   - The recursive call on the right child of the first node and the left child of the second node returns `True`.
5. Call the helper function with the left and right children of the root node, or with the root node twice, and return the result.

---

## Why This Works

- The BFS approach checks for symmetry at each level of the tree by performing opposite direction traversals and ensuring that the nodes match.
- The DFS approach compares the left and right subtrees directly by matching the left child of one subtree with the right child of the other subtree, ensuring that the structure and values are symmetric.

---

## Edge Cases

- A tree with only one node is symmetric.
- A tree with two nodes (one parent and one child) is not symmetric.
- A tree with multiple levels where one side has a missing node while the other side has a corresponding node is not symmetric.
- A tree with the same traversal in each direction can be asymmetric if the placement of null nodes is not mirrored.

---

## Time & Space Complexity

- Time: O(n), where n is the number of nodes in the tree, since we need to visit each node once.
- Space: O(n) in the worst case for both approaches, due to the space needed for the queues in BFS or the call stack in DFS.

---

## Common Mistakes

- Not checking for `None` nodes properly, which can lead to incorrect results.
- Forgetting to enqueue the children in the correct order for BFS, which can lead to incorrect symmetry checks.
- In the recursive approach, not ensuring that both the value and the structure of the tree are checked for symmetry.

---

## Alternative Solutions

- Using a stack instead of a queue for the iterative approach can also work, but it may be less intuitive for level order traversal.
  - The stack would consist of pairs of nodes to compare, and we would push onto the stack children pairs in the same way as the recursive approach (left child of one node with the right child of the other node, and vice versa).
