# 543 – Diameter of Binary Tree

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Depth-First Search (DFS)  
**Link:** https://leetcode.com/problems/diameter-of-binary-tree/description/

---

## Problem Summary

Given the root of a binary tree, return the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

---

## Key Insight

- The maximum diameter at any node is equal to the height of the left subtree plus the height of the right subtree
- We can use DFS to compute the height of the tree while updating the diameter at each node if it is larger than the current maximum
- After calculating the diameter at a node, we need to return the height of the current subtree so that its parent can compute its diameter, and so on
- Since the main function returns diameter but we want to return height, we use a helper function

---

## Approach

1. Initialize a variable `diameter` to keep track of the maximum diameter found so far.
2. Define a helper function that:
   - Returns 0 if the current node is null.
   - Recursively computes the height of the left and right subtrees.
   - Updates the `diameter` variable with the maximum of its current value and the sum of the left and right heights.
   - Returns the maximum height of the current subtree (1 + max of left and right heights).
3. Call the helper function with the root node to compute the diameter.
4. Return the `diameter` variable as the final result.

---

## Why This Works

- At every node, we calculate the longest path that goes through that node and keep track of the global maximum
- Since the longest path must pass through some node in the tree, the above approach guarantees that we find the maximum diameter
- Returning the height of each subtree allows us to save computation and calculate diameters for parent nodes

---

## Edge Cases

- Null tree (should return 0)
- Tree with only one node (should return 0)
- Tree with multiple nodes but all in a straight line (should return the number of edges in the longest path)

---

## Time & Space Complexity

- Time: O(n), where n is the number of nodes in the tree, since we visit each node once
- Space: O(n) in the worst case (skewed tree) due to the recursion stack, O(log n) in the best case (balanced tree)

---

## Common Mistakes

- Forgetting to update the diameter at each node
- Returning the diameter instead of the height in the helper function
- Not handling the base case of a null node correctly
- Forgetting to call the helper function with the root node

---

## Alternative Solutions

- Iterative approach using a stack to perform DFS, but it is more complex and less intuitive than the recursive solution
