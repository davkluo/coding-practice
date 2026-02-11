# 22 – Generate Parentheses

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/generate-parentheses/

---

## Problem Summary

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

---

## Key Insight

- For well-formed parenthesis, at any point in the string, the number of opening parentheses must be greater than or equal to the number of closing parentheses.
  - If we haven't used up all opening parentheses, we can add an opening parenthesis.
  - If we have more opening parentheses than closing parentheses, we can add a closing parenthesis
- When we have n opening parentheses and n closing parentheses, we have a valid combination.

---

## Approach

1. Initialize an empty list to store valid combinations.
2. Define a recursive backtracking function that takes in the current combination (as a list to avoid string concatenation overhead) and the count of opening parentheses used
   - If the length of the current combination is 2\*n, we have a valid combination. Join the list into a string and add it to the result list.
   - If the number of open parentheses used is less than n, we can add an opening parenthesis and recurse.
   - If the number of open parentheses used is greater than the number of closing parentheses (calculated as the length of the current combination minus the number of open parentheses used), we can add a closing parenthesis and recurse.
3. Call the backtracking function with an empty combination and 0 open parentheses used.
4. Return the result list.

---

## Why This Works

- The backtracking approach systematically explores all possible combinations of parentheses while ensuring that only valid combinations are generated.
- By keeping track of the number of opening parentheses used, we can ensure that we never add more closing parentheses than opening parentheses, thus maintaining the validity of the combinations.

---

## Edge Cases

- n = 1: The only valid combination is "()".

---

## Time & Space Complexity

- Time: O(4^n / sqrt(n)) - The number of valid combinations of parentheses is given by the nth Catalan number, which is approximately 4^n / (n^(3/2) \* sqrt(pi)).
- Space: O(4^n / sqrt(n)) - The space complexity is also proportional to the number of valid combinations, as we need to store them in the result list.

---

## Common Mistakes

- Forgetting to check if the number of closing parentheses is less than the number of opening parentheses before adding a closing parenthesis.
- Using string concatenation instead of a list to build the current combination, which can lead to higher time complexity due to repeated string copying.

---

## Alternative Solutions

- Iterative approach using a stack to generate combinations.
- Dynamic programming approach where we build combinations for n pairs based on combinations for fewer pairs.
  - We take the combinations for n-1 pairs and insert a new pair of parentheses in every possible position in those combinations to generate the combinations for n pairs.
