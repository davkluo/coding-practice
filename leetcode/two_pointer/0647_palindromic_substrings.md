# 647 – Palindromic Substrings

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Two Pointer
**Secondary Patterns:** Dynamic Programming
**Link:** https://leetcode.com/problems/palindromic-substrings/

---

## Problem Summary
Given a string `s`, return the number of palindromic substrings in it.

---

## Key Insight
- We can use two pointers to expand around potential centers of palindromes.
- Odd length palindromes have a single center, while even length palindromes have a center between two characters.

---

## Approach
1. Initialize a counter to zero.
2. Define a helper function that takes two indices (left and right) and expands outwards while the characters at these indices are equal. For each valid palindrome found, increment the counter.
3. For each character in the string, call the helper function twice: once for odd-length palindromes (left and right both at the current index) and once for even-length palindromes (left at current index and right at current index + 1).
4. Return the counter after processing all characters.

---

## Why This Works
- By expanding around each character (and between characters), we ensure that we count all possible palindromic substrings.

---

## Edge Cases
- Single character strings (always a palindrome).
- Strings with all identical characters should return the number of substrings.

---

## Time & Space Complexity
- Time: O(n^2), where n is the length of the string, since we potentially expand around each character for all characters.
- Space: O(1), as we are using a constant amount of extra space.

---

## Common Mistakes
- Forgetting to check for even-length palindromes.
- Not handling the boundaries of the string correctly when expanding.

---

## Alternative Solutions
- Dynamic Programming: Use a 2D table to keep track of whether substrings are palindromic, but this uses O(n^2) space.
    - Requires going through the table and counting at the end.