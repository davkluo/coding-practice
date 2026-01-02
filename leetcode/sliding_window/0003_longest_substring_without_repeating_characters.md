# 3 – Longest Substring Without Repeating Characters

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## Problem Summary
Given a string, find the length of the longest substring without duplicate characters.

---

## Key Insight
Using a hash map to track the last seen index of each character allows efficient adjustment of the sliding window.

---

## Approach
1. Handle base cases for empty or single-character strings.
2. Initialize a hash map to store the last seen index of characters.
3. Initialize the maximum length variable to track the longest substring found.
4. Use two pointers to represent the sliding window's bounds, initially set to the start of the string.
5. Iterate through the string with the right pointer:
   - If the character at the right pointer has been seen and is within the current window (i.e. its last seen index is >= left pointer), move the left pointer to one position right of the last seen index of that character.
   - Update the last seen index of the character at the right pointer.
    - Calculate the current window size and update the maximum length if it's larger than the previously recorded maximum.
6. Return the maximum length after processing the entire string.

---

## Why This Works
- The sliding window technique allows us to expand and contract the substring efficiently, using the hash map to avoid duplicates.
- The hash map provides O(1) access to character indices, ensuring that we can adjust the left pointer in constant time.
- When we expand until a duplicate is found, that duplicate is guaranteed to be the earliest occurring duplicate within the current window, ensuring that we are trimming as little as necessary. This prevents skipping over potential longer substrings.

---

## Edge Cases
- Empty input
- Single character input
- All characters the same

---

## Time & Space Complexity
- Time: O(n), where n is the length of the string.
    - The right pointer iterates through the string once, and the left pointer moves through the string at most once as well.
    - The hash map operations (insert and lookup) are O(1) on average and occur n times.
- Space: O(min(m, n)), where m is the size of the character set and n is the length of the string.
    - In the worst case, we may store all characters in the hash map if all characters are unique.

---

## Common Mistakes
- Not checking if the last seen index of a character is within the current window before moving the left pointer.
- Failing to update the last seen index of characters correctly.
- Not updating the maximum length after each iteration; it is not the length of the pointers at the end of the loop but the maximum found during the iterations.

---

## Alternative Solutions
- A set can be used for similar runtime and space complexity, but will require more operations as the left pointer will have to remove characters from the set one by one until the duplicate is removed.