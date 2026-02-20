# 297 – Serialize and Deserialize Binary Tree

**Platform:** LeetCode
**Difficulty:** Hard
**Primary Pattern:** BFS (Level-Order Traversal)
**Link:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

---

## Problem Summary

Design an algorithm to serialize a binary tree to a string and deserialize that string back to the original tree structure. There is no constraint on the format — just that encode/decode are inverses.

---

## Key Insight

- **Serialize** with BFS: emit each node's value in level-order, using `"null"` as a placeholder whenever a child slot is absent. This records both values and structure in a single linear scan. If a node is null, we still emit `"null"` and enqueue nothing, ensuring the next level's tokens are correctly aligned.
- **Deserialize** with queue-based parent matching: maintain a queue of nodes whose children haven't been assigned yet. Each parent dequeued consumes exactly the next two tokens from the array — left child then right child. If a token is `"null"`, no node is created and nothing is enqueued; otherwise, create the node, attach it, and enqueue it as a future parent.
- The two queues (serialize's BFS queue and deserialize's parent queue) process nodes in the same order, so `child_i` advances in lockstep with which parent is being matched — no index arithmetic needed.

---

## Approach

### Serialize

1. Handle the empty tree: return `"[]"`.
2. Start a BFS queue with the root.
3. Each iteration processes one full level:
   - For each node in the level: append its value (or `"null"` if the slot is `None`) to the result list.
   - Enqueue both children (even `None` children) for non-null nodes so their slots appear in the next level.
   - Track `level_has_children`: if no node in this level has any real child, stop — no need to emit a trailing row of `null`s.
4. Join the list with commas and wrap in `"["..."]"`.

### Deserialize

1. Strip the brackets; if the inner string is empty, return `None`.
2. Split on commas. Build the root from `nodes[0]`; seed the queue with it. Start `child_i = 1`.
3. While the queue is non-empty:
   - Dequeue a parent.
   - **Left child** (`nodes[child_i]`): if not `"null"`, create a node, attach as `parent.left`, enqueue it. Always increment `child_i`.
   - **Right child** (`nodes[child_i]`): same logic. Always increment `child_i`.
4. Return the root.

The invariant is: the k-th node dequeued is the parent of tokens at positions `child_i` and `child_i+1` at the time it is processed.

---

## Why This Works

- **Serialize produces tokens in parent-then-children order**: every non-null node appends its two child slots (real value or `"null"`) immediately after itself in the BFS traversal. This means the token array is a flattened record of "parent at position p has children at the next two available positions."
- **Deserialize replays the same BFS order**: the parent queue dequeues nodes in the exact order they were enqueued during serialization. So when the k-th parent is dequeued, `child_i` is guaranteed to point at that parent's left-child token. Each parent always consumes exactly two tokens, keeping `child_i` in sync automatically.
- **`null` tokens break the chain without breaking the index**: a `"null"` token means "no child node here," so nothing is enqueued — that slot will never itself become a parent. But `child_i` still increments, preserving alignment for all subsequent parents.
- **`level_has_children` early exit**: once a level contains no real children, there are no future parents to match against, so emitting a trailing row of `"null"`s would be wasted. Stopping early keeps the string compact without affecting correctness.

---

## Edge Cases

- Empty tree: `serialize(None)` → `"[]"`, `deserialize("[]")` → `None`.
- Single node: `"[1]"` → no children tokens emitted, deserialized correctly via the `len(nodes) == 1` early return.
- Skewed trees (left-only or right-only chains): the `null` placeholders for missing siblings are required so deserialization knows which side each child belongs to
- Negative values: handled naturally since `str()` and `int()` work with negatives.

---

## Time & Space Complexity

- Time: O(n) for both serialize and deserialize — each node is visited exactly once.
- Space: O(n) for the queue and the encoded string/token list.

---

## Common Mistakes

- **Serialize — not enqueuing `None` children**: if you only enqueue real children, you lose the positional information needed to tell left from right during deserialization.
- **Serialize — enqueueing children for `None` nodes**: this creates a complete binary tree structure which allows for systematic calculation of child indices, but results in much more memory usage since the string would be O(2^h) where h is the height of the tree, instead of O(n).
- **Deserialize — not incrementing `child_i`**: every potential parent node consumes exactly two tokens (left and right child), so `child_i` must be incremented even when a child token is `"null"`.
- **Deserialize — enqueuing null nodes**: null slots must not be enqueued (they have no children), which is handled by only appending real `TreeNode` objects to the queue.

---

## Alternative Solutions

- **Pre-order DFS**: recurse left then right, appending `"null"` at leaf boundaries. Deserialization uses a shared iterator advancing with each recursive call. Simpler to implement recursively; slightly deeper call stack for skewed trees.

```python
def serialize(self, root):
    result = []
    def dfs(node):
        if not node:
            result.append("null")
            return
        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return ",".join(result)

def deserialize(self, data):
    tokens = iter(data.split(","))
    def dfs():
        val = next(tokens)
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
```
