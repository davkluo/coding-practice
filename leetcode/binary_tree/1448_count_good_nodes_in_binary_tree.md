# 1448 – Count Good Nodes in Binary Tree

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Binary Tree DFS
**Link:** https://leetcode.com/problems/count-good-nodes-in-binary-tree/

---

## Problem Summary

Given a binary tree, count the number of "good" nodes — nodes where no value on the path from the root to that node is greater than the node's own value.

---

## Key Insight

- Carry the running maximum along the path from root to current node. A node is good if and only if it is >= that maximum.

---

## Approach

1. Define a recursive helper `count_good(node, max_on_path)`.
2. If `node` is `None`, return immediately.
3. If `max_on_path <= node.val`, increment the good node count.
4. Recurse on both children, passing `max(node.val, max_on_path)` as the new path maximum.
5. Seed the initial call with `max_on_path = float("-inf")` so the root is always counted.

---

## Why This Works

- The path maximum is monotonically non-decreasing as we go deeper. Passing it down ensures each node only sees the largest value encountered so far on its specific root-to-node path, which is exactly what defines "good".

---

## Edge Cases

- Single node: the root is always good (seeded with `-inf`), returns 1.
- All nodes equal: every node satisfies `max_on_path <= node.val`, so all are counted.
- Strictly decreasing tree: only the root is good; all descendants have a path max greater than their value.

---

## Time & Space Complexity

- Time: O(n) — every node is visited exactly once
- Space: O(h) — recursion stack depth equals tree height; O(log n) for balanced, O(n) for skewed

---

## Common Mistakes

- Forgetting to seed with `-inf`: seeding with `0` would incorrectly miss negative-valued roots.
- Passing `node.val` instead of `max(node.val, max_on_path)` to children — this drops the running maximum from higher ancestors.

---

## Alternative Solutions

- Iterative DFS with an explicit stack storing `(node, max_on_path)` pairs — same complexity, avoids recursion overhead.
