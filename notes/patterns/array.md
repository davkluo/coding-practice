# Pattern: Array

---

## When to Use
- Problems involving traversal, search, or transformation of a sequence of elements.
- When the problem asks for in-place modification without extra space.
- When contiguous subarrays or ranges are involved.

---

## Core Idea
- Exploit index relationships and the contiguous memory layout of arrays to avoid extra allocations.
- Many problems reduce to a single pass with a few tracked variables (pointers, running sums, etc.).

---

## Common Techniques
- **Prefix Sums:** precompute a running sum so any subarray sum `[i, j]` is O(1) as `prefix[j+1] - prefix[i]`.
- **Sliding Window:** maintain a window `[l, r]`, expanding `r` and contracting `l` to satisfy a constraint.
- **Two Pointers:** two indices converging or co-moving to reduce an O(n²) search to O(n).
- **Kadane's Algorithm:** `curr = max(nums[i], curr + nums[i])` for maximum subarray sum.
- **In-Place Modification:** swaps, reversal, or cyclic replacements to rearrange without extra space.
  - *Three-Reversal:* reverse whole array, then reverse each sub-range (e.g. rotation).
  - *Cyclic Replacements:* each element moves directly to its final index; handle multiple cycles when `gcd(n, shift) > 1`.
  - *Slice Assignment:* `nums[:] = nums[i:] + nums[:i]` — O(n) space but C-level fast in Python.
- **Sorting + Index Tricks:** sort to enable greedy sweeps, binary search, or deduplication.

---

## Typical Time Complexity
- Time Complexity: O(n) for single-pass techniques; O(n log n) when sorting is involved.
- Space Complexity: O(1) for in-place approaches; O(n) for prefix sums or slice-based methods.

---

## Common Pitfalls
- Forgetting `k % n` before using `k` as an index or shift.
- Off-by-one errors in range boundaries for reversal, partitioning, or prefix sum indexing.
- Not handling multiple independent cycles in cyclic replacements (`gcd(n, shift) > 1`).
- Mutating the input array when the caller expects it to be preserved.
- In Python: pure-Python loops over arrays are slower than C-level builtins (`list.reverse()`, slicing, `deque`) even when the loop has better space complexity — prefer builtins where possible.

---

## Canonical Problems
- Rotate Array (189)
