# 105 – Construct Binary Tree from Preorder and Inorder Traversal

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Depth-First Search (DFS)
**Link:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

---

## Problem Summary

Given the preorder and inorder traversals of a binary tree with unique values, reconstruct and return the binary tree.

---

## Key Insight

- The first element of preorder is always the root of the current subtree
- Finding that root value in inorder splits it into left and right subtrees — everything to the left is the left subtree, everything to the right is the right subtree
- The size of the left subtree in inorder tells you exactly how many elements in preorder belong to the left subtree, letting you derive the preorder range for each child

---

## Approach

1. Build a hashmap from value to index over the inorder array for O(1) root lookups.
2. Define a recursive helper that takes `(preorder_range, inorder_range)` as index pairs.
3. Base case: if either range is empty (`pre_l > pre_r` or `in_l > in_r`), return `None`.
4. The root is `preorder[pre_l]`. Look up its index in the inorder map.
5. Compute `l_subtree_size = inorder_idx - in_l`.
6. Derive child ranges:
   - Left preorder: `(pre_l + 1, pre_l + l_subtree_size)`
   - Right preorder: `(pre_l + l_subtree_size + 1, pre_r)`
   - Left inorder: `(in_l, inorder_idx - 1)`
   - Right inorder: `(inorder_idx + 1, in_r)`
7. Recurse for left and right children, attach to root, and return root.

---

## Why This Works

- Preorder guarantees the first element is the root; inorder guarantees the root separates left and right subtrees
- Because all values are unique, the inorder index lookup is unambiguous
- The left subtree size is the same in both traversals, so we can precisely partition the preorder array without any ambiguity

---

## Edge Cases

- Single node — both arrays have one element; `l_subtree_size` is 0, both child ranges are empty
- Left-skewed tree — `l_subtree_size` equals the full remaining range, right child range is always empty
- Right-skewed tree — `l_subtree_size` is always 0, left child range is always empty

---

## Time & Space Complexity

- Time: O(n) — each node is visited once; inorder lookup is O(1) with the hashmap
- Space: O(n) — O(n) for the hashmap plus O(n) recursion stack depth in the worst case (skewed tree), O(log n) for a balanced tree

---

## Common Mistakes

- Forgetting to build the inorder hashmap and doing a linear scan instead, making it O(n²)
- Off-by-one errors in the preorder range — the right subtree starts at `pre_l + l_subtree_size + 1`, not `pre_l + l_subtree_size`
- Passing array slices instead of index ranges, which creates O(n) copies at each level

---

## Alternative Solutions

- Pass array slices instead of index ranges — simpler to reason about but O(n²) time and space due to copying at each recursive call
