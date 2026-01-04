# 104 – Maximum Depth of Binary Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Depth-First Search (DFS)
**Link:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

---

## Problem Summary
Given the root of a binary tree, return its maximum depth.

---

## Key Insight
- The maximum depth of a binary tree can be found by recursively calculating the depth of its left and right subtrees and taking the maximum of the two, adding one for the current node.
- Alternatively, an iterative approach using a stack or queue can also be employed to traverse the tree level by level.

---

## Approach
### Recursive DFS
1. If the root is `None`, return 0 (base case).
2. Recursively call the function on the left and right children to get their depths.
3. Return the maximum of the two depths plus one.
### Iterative DFS
1. If the root is `None`, return 0.
2. Use a stack to keep track of nodes along with their current depth.
3. Initialize the maximum depth to 0.
4. While the stack is not empty:
   - Pop a node and its depth from the stack.
   - Update the maximum depth if the current depth is greater.
    - If the node has left or right children, push them onto the stack with an incremented depth.
5. Return the maximum depth.

---

## Why This Works
- The recursive approach effectively explores all paths from the root to the leaves, ensuring that the maximum depth is captured.
- The iterative approach simulates the same process using a stack, allowing for depth tracking without recursion

---

## Edge Cases
- Null tree (should return 0).
- Tree with only one node (should return 1).

---

## Time & Space Complexity
- Time: O(N), where N is the number of nodes in the tree, as we visit each node once.
- Space: O(H), where H is the height of the tree, due to the recursion stack in the worst case (for a skewed tree) or the stack used in the iterative approach.

---

## Common Mistakes
### General
- Forgetting to handle the base case of an empty tree.
- Forgetting to check for null nodes before processing them.
### Recursive Approach
- Not returning the correct depth when reaching a leaf node.
- Forgetting to add one for the current node when returning depth.
- Not initializing the left and right subtree depths to zero when the child nodes are null.
### Iterative Approach
- Not pushing child nodes onto the stack with the correct depth.
- Not correctly updating the maximum depth during traversal.

---

## Alternative Solutions
- Breadth-First Search (BFS) using a queue to traverse the tree level by level, counting the number of levels to determine the maximum depth.