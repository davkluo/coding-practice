# 5 – Longest Palindromic Substring

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Two Pointer
**Secondary Patterns:** Dynamic Programming, Expand Around Center
**Link:** https://leetcode.com/problems/longest-palindromic-substring/

---

## Problem Summary
Given a string `s`, find the longest palindromic substring in `s`.

---

## Key Insight
- We can use the two-pointer technique to expand around potential centers of palindromes.
- Palindromes can be of odd or even length, so we need to consider both cases.

---

## Approach
1. Initialize variables to track the start and end indices of the longest palindrome found, as well as the maximum length.
2. Define a helper function that expands around a given center and updates the above variables if a longer palindrome is found.
3. Iterate through each character in the string, running the helper function twice for each character:
   - Once treating the character as the center of an odd-length palindrome.
   - Once treating the current character and the next as the center of an even-length palindrome.
4. After checking all centers, return the substring defined by the start and end indices.

---

## Why This Works
- By expanding around each character (and pairs of adjacent characters), we ensure that we check all possible palindromic centers.
- The two-pointer expansion efficiently checks for palindromic properties without needing to check every possible substring explicitly.

---

## Edge Cases
- Single character strings
- Strings with all identical characters
- Strings with no palindromic substrings longer than 1 character
- Two character strings that are either the same or different
- Entire string is a palindrome

---

## Time & Space Complexity
- Time: O(n^2) in the worst case, where n is the length of the string, due to the nested expansion for each character.
- Space: O(1) for the pointers and indices used, not counting the input and output storage.

---

## Common Mistakes
- Failing to consider both odd and even length palindromes.
- Not updating the start and end indices correctly when a longer palindrome is found.
- Failing to check pointers going out of bounds during expansion and when checking even length palindromes.
- Comparing pointers instead of the characters they point to.

---

## Alternative Solutions
- Dynamic Programming: Create a 2D table to store whether substrings are palindromic, and build up from shorter to longer substrings.
    - The variables of DP table would be `dp[i][j]` indicating whether the substring from index `i` to `j` is a palindrome.
- Manacher's Algorithm: A more complex algorithm that finds the longest palindromic substring in linear time O(n).