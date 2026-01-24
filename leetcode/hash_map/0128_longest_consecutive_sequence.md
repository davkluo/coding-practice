# 128 – Longest Consecutive Sequence

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Hash Map
**Link:** https://leetcode.com/problems/longest-consecutive-sequence/

---

## Problem Summary

Given an unsorted array of integers, return the length of the longest consecutive elements sequence. The algorithm must run in O(n) time.

---

## Key Insight

- We cannot sort (that would be O(n log n)), so we need a different approach.

### Set Approach

- A number is the start of a sequence only if `num - 1` is not in the set.
- By only expanding from sequence starts, each number is visited at most twice (once in the outer loop, once when expanding), maintaining O(n) time.

### Hash Map Approach

- We can use a hash map to track the ranges of consecutive sequences that each number belongs to.
- This is kind of like union-find, where we merge ranges when we find neighbors.

---

## Approach

### Set Approach

1. Insert all numbers into a set for O(1) lookups.
2. Initialize a variable `longest` to track the maximum sequence length.
3. For each number in the set:
   - If `num - 1` is not in the set, it is a sequence start.
   - Count up from `num` while `num + length` is in the set.
4. Update `longest` if the current sequence length is greater.
5. Return `longest`.

### Hash Map Approach

1. Create a hash map `num_to_range` to map each number to its `[start, end]` range.
2. Initialize `longest` to track the maximum sequence length.
3. For each number in `nums`:
   - If the number is already in `num_to_range`, skip it (to handle duplicates).
   - Check for left (`num - 1`) and right (`num + 1`) neighbors in `num_to_range`.
   - Depending on the presence of neighbors, update ranges:
     - No neighbors: Create a new range `[num, num]`.
     - Left neighbor only: Extend the left neighbor's range to include `num`, and create a new entry for `num`.
     - Right neighbor only: Extend the right neighbor's range to include `num`, and create a new entry for `num`.
     - Both neighbors: Merge the two ranges and update the endpoints and `num`.
   - Update `longest` accordingly.
4. Return `longest`.

---

## Why This Works

### Set Approach

- Only sequence starts trigger the inner counting loop.
- Each number belongs to exactly one sequence and is counted exactly once during expansion.
- The set provides O(1) membership checks.
- Total work is O(n) since each element is processed at most twice.

### Hash Map Approach

- Each number is processed once.
- The hash map allows efficient merging of ranges.
- We only need to update the endpoints of ranges, keeping operations efficient.
  - This is because the numbers in between are already captured and no future numbers can latch onto them to extend the range.
- Each number is added to the map only once, ensuring O(n) time complexity.

---

## Edge Cases

- Empty array: Return 0.
- Single element: Return 1.
- All duplicates: Duplicates are collapsed in the set; return 1.
- Negative numbers: The algorithm handles negatives naturally.
- No consecutive elements: Return 1 (each element is its own sequence of length 1).

---

## Time & Space Complexity

- Time: O(n) for both approaches.
  - Set Approach:
    - Building the set is O(n).
    - Each element is visited at most twice (once in iteration, once during sequence expansion).
  - Hash Map Approach:
    - Each element is processed once, with O(1) operations for lookups and updates.
- Space: O(n) for both approaches.
  - Set Approach: O(n) for the set.
  - Hash Map Approach: O(n) for the hash map storing ranges.

---

## Common Mistakes

- Sorting the array (violates the O(n) time requirement).
- Not skipping non-start elements, leading to O(n²) time by re-counting sequences.
- Forgetting to handle duplicates (using a set/hash map naturally handles this).
- In the hash map approach, failing to add an entry for the current number when merging left and right ranges. Even though the number's range is captured by the endpoints, it still needs its own entry so that we can skip duplicate encounters.
  - This is important because the left and right neighbors may become stale via the overall sequence extending in the future, and a repeat encounter of the number will try to act upon stale data.

---

## Alternative Solutions

- Union-Find using a tree structure to manage connected components of consecutive numbers.
  - If the tree has a height of 2 (the root is the range endpoints, and children are the numbers in between), union and find operations can be O(1).
