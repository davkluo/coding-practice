# 124 – Binary Tree Maximum Path Sum

**Platform:** LeetCode
**Difficulty:** Hard
**Primary Pattern:** Binary Tree DFS
**Link:** https://leetcode.com/problems/binary-tree-maximum-path-sum/

---

## Problem Summary

Given the root of a binary tree, return the maximum sum of any path, where a path is any sequence of nodes connected by edges with no node repeated. The path must contain at least one node.

---

## Key Insight

- At each node, a path can either pass through it (connecting left and right subtrees) or extend upward to its parent — but not both. So the recursive helper returns the best straight-line gain going downward, while the global max tracks the best "turning" path seen at any node.

---

## Approach

1. Maintain a `max_sum` global variable initialized to `-inf`.
2. Define a helper `_max_path_sum(node)` that returns the best path gain starting at `node` and extending downward (always includes `node.val`).
3. At each node, recursively get `left_max_sum` and `right_max_sum` from children (use `-inf` as a sentinel when a child is absent).
4. Update `max_sum` with all path combinations at this node: node alone, node + left, node + right, node + left + right.
5. Return `max(node.val, node.val + left_max_sum, node.val + right_max_sum)` so the parent can extend this path upward in only one direction.

---

## Why This Works

- The helper's return value always includes `node.val`, so a parent can extend it upward without double-counting. Returning both branches would create a fork, which can't connect to a grandparent.
- `max_sum` is updated at every node during recursion, so any best path entirely within a subtree is captured at the node where it "turns" — it doesn't need to be re-evaluated by an ancestor.
- Because `max_sum` is already updated at the child level with the child's return value as a candidate, the child's return value as a standalone candidate in the parent's `max_sum` update is redundant (though harmless).

---

## Edge Cases

- Single node: the only path is the node itself; must handle all-negative trees by returning the least negative node
- All-negative tree: negative children should be excluded; initialized sentinels of `-inf` ensure absent or negative subtrees don't inflate the result
- Path entirely within one subtree: handled because `max_sum` is updated at every node, not just the root

---

## Time & Space Complexity

- Time: O(n) — each node is visited exactly once
- Space: O(h) — call stack depth equals tree height; O(log n) for balanced, O(n) worst case for skewed

---

## Common Mistakes

- Returning `max(node.val, node.val + left_max_sum, node.val + right_max_sum)` from the helper but forgetting to also consider `left + node + right` as a candidate for `max_sum` — this misses paths that turn at the current node
- Using `0` as a sentinel for absent children instead of `-inf`, which incorrectly treats a missing child as contributing 0 and can cause wrong results when all values are negative

---

## Alternative Solutions

- This is the standard optimal solution.
