# 387 – First Unique Character in a String

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Hash Map
**Link:** https://leetcode.com/problems/first-unique-character-in-a-string/

---

## Problem Summary

Given a string, find the index of the first non-repeating character. Return -1 if no unique character exists.

---

## Key Insight

- We need to know the frequency of each character before we can determine which one is unique. A hash map lets us count frequencies in one pass, then check uniqueness in a second pass.

---

## Approach

1. First pass: Count the frequency of each character using a hash map
2. Second pass: Iterate through the string in order and return the index of the first character with count == 1
3. If no unique character is found, return -1

---

## Why This Works

- By counting all characters first, we have complete information about which characters are unique.
- The second pass preserves the original order, so the first character we find with count 1 is guaranteed to be the first unique character in the string.

---

## Edge Cases

- Single character string → return 0
- All characters repeat → return -1
- All characters unique → return 0 (first one)
- Empty string → return -1

---

## Time & Space Complexity

- Time: O(n) – two passes through the string
- Space: O(1) – at most 26 lowercase letters in the hash map

---

## Common Mistakes

- Returning the character instead of its index
- Using only one pass and missing characters that appear later
- Not preserving order when iterating (e.g., iterating over hash map keys instead of the original string)

---

## Alternative Solutions

- Use `Counter` from collections for cleaner frequency counting
- Use an array of size 26 instead of a hash map for slightly better constant factors
