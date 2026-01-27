# 523 – Continuous Subarray Sum

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Prefix Sum + Hash Map
**Link:** https://leetcode.com/problems/continuous-subarray-sum/

---

## Problem Summary

Given an integer array `nums` and an integer `k`, return `true` if there exists a continuous subarray of size at least two whose elements sum to a multiple of `k`.

---

## Key Insight

- If two prefix sums have the same remainder when divided by `k`, then the subarray between those two indices sums to a multiple of `k`.
- After that we just need to check that the subarray length is at least two.
- Tracking the remainders and their earliest indices allows us to efficiently check for valid subarrays in a single pass.
- Note that we don't need to calculate all subarrays -- finding the same remainder is equivalent to having considered the subarray between the two indices (think of how we use prefix sums to find subarray sums).

---

## Approach

1. Use a hash map to store the first index where each remainder (prefix_sum % k) was seen
2. Initialize the map with `{0: -1}` to handle subarrays starting at index 0
   - Note that if a sum has remainder 0 we don't necessarily need an earlier occurrence.
3. Iterate through the array, maintaining a running sum
4. At each index, compute `curr_sum % k`
5. If this remainder was seen before and the indices are at least 2 apart, return `True`
6. Otherwise, store the remainder with its index (only if not already present—we want the earliest index)

---

## Why This Works

-For prefix sums `prefix[i]` and `prefix[j]` where `j > i`: - The subarray sum from `i+1` to `j` equals `prefix[j] - prefix[i]` - If `prefix[i] % k == prefix[j] % k`, then `(prefix[j] - prefix[i]) % k == 0` - This means the subarray between them sums to a multiple of `k`

- By storing only the first occurrence of each remainder, we maximize the subarray length, making it easier to satisfy the "size at least two" requirement.

---

## Edge Cases

- Single element array: must return `False` (subarray needs size ≥ 2)
- Consecutive zeros: `[0, 0]` is valid for any `k` since `0` is a multiple of everything
- `k = 1`: any subarray of size ≥ 2 works since every integer is a multiple of 1
- Subarray starting at index 0: handled by initializing `{0: -1}` in the map

---

## Time & Space Complexity

- Time: O(n) — single pass through the array
- Space: O(min(n, k)) — at most `k` distinct remainders possible

---

## Common Mistakes

- Forgetting to initialize the map with `{0: -1}` for subarrays starting at index 0
- Updating the map even when the remainder already exists (we need the earliest index)
- Not checking that the subarray length is at least 2 (`i - mod_to_idx[mod] >= 2`)

---

## Alternative Solutions

- None as efficient as the prefix sum + hash map approach for this problem.
