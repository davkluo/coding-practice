# 232 – Implement Queue Using Stacks

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Design / Two Stacks
**Link:** https://leetcode.com/problems/implement-queue-using-stacks/

---

## Problem Summary

Implement a FIFO queue using only two stacks, supporting `push`, `pop`, `peek`, and `empty` operations.

---

## Key Insight

- A single stack reverses order. Two stacks cancel out the reversal: push everything onto a "push stack", then transfer to a "pop stack" to restore FIFO order.
- The key insight for amortized O(1) is that both stacks can hold elements simultaneously. Only refill `pop_stack` from `push_stack` when `pop_stack` runs dry — never transfer back.

---

## Approach

1. Maintain two stacks: `push_stack` for incoming elements, `pop_stack` for outgoing elements.
2. **`push(x)`**: Always append directly to `push_stack`. Never touch `pop_stack`.
3. **`pop()`**: If `pop_stack` is empty, transfer all elements from `push_stack` to `pop_stack` (reversing their order). Then pop from `pop_stack`.
4. **`peek()`**: Return `pop_stack[-1]` if `pop_stack` has elements (top = front of queue), otherwise return `push_stack[0]` (bottom = oldest element).
5. **`empty()`**: Return `True` if both stacks are empty.

---

## Why This Works

- Elements always enter via `push_stack` and leave via `pop_stack`. Transferring push_stack → pop_stack reverses the order, making the oldest element the new top of `pop_stack`, which matches FIFO semantics.
- Both stacks can hold elements simultaneously. `pop_stack` drains completely before being refilled, so a newly pushed element won't be popped before older elements still in `pop_stack`.
- `peek` short-circuits: if `pop_stack` is already populated, the front is at `pop_stack[-1]`; if only `push_stack` is populated, the front is at `push_stack[0]` (the bottom, i.e. the first element ever pushed).

---

## Edge Cases

- `peek` when `pop_stack` is empty (must read `push_stack[0]` instead)
- Single-element queue (same element is both front and back)

---

## Time & Space Complexity

- Time: O(1) amortized per operation. Each element is pushed to `push_stack` once, transferred to `pop_stack` once, and popped once. The cost of an O(n) transfer is amortized across the n preceding O(1) pushes.
- Space: O(n) total across both stacks.

---

## Common Mistakes

- Transferring elements back from `pop_stack` to `push_stack` on `push` (e.g. to keep new elements at the "back"). This causes O(n) per operation on alternating push/pop sequences since elements shuttle back and forth instead of crossing the boundary at most once.
- Calling `shift_push_to_pop` even when `pop_stack` still has elements — this is unnecessary and breaks the amortized guarantee. It also ruins the FIFO property allowing newer items to be popped before older items.

---

## Alternative Solutions

- **Deque**: Python's `collections.deque` supports O(1) append and popleft natively, making it a direct queue implementation — but defeats the purpose of the problem.
