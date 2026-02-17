# 146 – LRU Cache

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Hash Map + Doubly Linked List
**Link:** https://leetcode.com/problems/lru-cache/

---

## Problem Summary

Design a data structure that supports `get` and `put` operations in O(1) time, evicting the least recently used item when the cache exceeds its capacity.

---

## Key Insight

- A hash map gives O(1) lookup but can't track usage order. A linked list tracks order but has O(n) lookup.
- Combining a hash map (key -> node) with a doubly linked list gives O(1) for both lookup and order maintenance.

---

## Approach

1. Create a `DoublyLinkedList` class that supports `insert_at_end`, `remove_at_head`, and `shift_to_end` operations. The head of the list is the least recently used, and the tail is the most recently used.
2. Maintain a hash map (`node_map`) from key to the corresponding linked list node.
3. **`get(key)`**: If the key exists in `node_map`, shift its node to the end of the list (marking it as most recently used) and return its value. Otherwise return -1.
4. **`put(key, value)`**: If the key already exists, update the node's value and shift it to the end. If the key is new and the list is at capacity, remove the head node (LRU entry) and delete its key from `node_map`. Then create a new node and insert it at the end.

---

## Why This Works

- Every access (`get` or `put`) shifts the touched node to the end of the list, so the head is always the least recently used.
- The hash map ensures every lookup is O(1), and the doubly linked list ensures every insertion, removal, and reordering is O(1).
- Storing the `key` on each node allows us to delete the correct entry from `node_map` when evicting from the head.

---

## Edge Cases

- `put` on an existing key (update value, don't double-count capacity)
- Cache capacity of 1 (every new `put` evicts the previous entry)
- `get` on a non-existent key (return -1, no side effects)

---

## Time & Space Complexity

- Time: O(1) per `get` and `put` operation.
- Space: O(capacity), for the hash map and linked list nodes.

---

## Common Mistakes

- Forgetting to remove the old key from the hash map when evicting the LRU node.
- Not shifting a node to the end on `put` for an existing key (which would leave the recency order stale).
- When implementing `shift_to_end`, not handling the special cases where the node is the current head or tail of the list.
- Removing the LRU entry when all that is needed is a node update, even if the cache is at capacity
- Errors in tracking the length of the doubly linked list implementation

---

## Alternative Solutions

- **Sentinel nodes**: Using dummy head/tail nodes eliminates null-check edge cases in `shift_to_end`, `remove_at_head`, and `insert_at_end`, at the cost of a slightly less intuitive setup.
- **`OrderedDict` (Python)**: `collections.OrderedDict` provides `move_to_end()` and `popitem(last=False)` out of the box, making the implementation trivial. Interviewers typically want the manual approach.
