# 91 – Decode Ways

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Dynamic Programming
**Link:** https://leetcode.com/problems/decode-ways/

---

## Problem Summary
Given a string of digits, determine the total number of ways to decode it into letters using the mapping 'A' -> 1, 'B' -> 2, ..., 'Z' -> 26.

---

## Key Insight
- Each digit or pair of digits can represent a letter if it falls within the valid range (1-26).
- Use dynamic programming to build up the solution by considering one or two digits at a time.
- We build up the number of ways to decode a prefix of the string based on the last one or two digits, as well as the previously computed results.
- We can save on memory by keeping track of only the last two computed values instead of the entire DP array (similar to Fibonacci).

---

## Approach
1. Initialize two variables to keep track of the number of ways to decode up to the previous two positions. For the -1 and -2 positions, we can initialize them to 1 (base case).
2. Iterate through the string from the first character to the last:
   - Initialize a variable to store the current number of ways to decode up to this position to 0.
   - For each character, check if it can form a valid single-digit decode (1-9). If so, add the number of ways to decode up to the previous position.
   - If we are at the first character, skip the following two-digit check.
   - Check if the current character and the previous character can form a valid two-digit decode (10-26). If so, add the number of ways to decode up to two positions back.
   - Update the two tracking variables for the next iteration.
3. Return the number of ways stored in the variable representing the last position.

---

## Why This Works
- We incrementally build up the solution by considering valid single and double digit decodes, and carrying forward the previous computations.
- Initializing the local count to 0 ensures that if neither condition is met, the count remains 0, correctly indicating no valid decodes for that position. This will propagate through the rest of the string, resulting in a final count of 0 since no valid decodes exist.

---

## Edge Cases
- Strings that start with '0' should return 0 since '0' does not map to any letter.
- Strings with consecutive '0's should also return 0.
- Single character strings that are '0' should return 0, while any other single character should return 1.

---

## Time & Space Complexity
- Time: O(n), where n is the length of the input string. We iterate through the string once.
- Space: O(1), as we only use a fixed amount of extra space for the two tracking variables.

---

## Common Mistakes
- Forgetting to handle the case where the string starts with '0'.
- Not initializing the local count to 0 at each iteration, which can lead to incorrect accumulation of decode ways. Particularly when neither single-digit nor two-digit conditions are met (i.e. consecutive '0's), the count should remain 0.
- Failing to check the validity of two-digit combinations properly.

---

## Alternative Solutions
- A full DP array can be used instead of two variables, but this increases space complexity to O(n).