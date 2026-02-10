# 17 – Letter Combinations of a Phone Number

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Backtracking
**Link:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

---

## Problem Summary

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent based on the mapping of digits to letters on a phone keypad. Return the answer in any order.

---

## Key Insight

- Backktracking is a natural fit for this problem since we need to explore all possible combinations of letters for the given digits.
- We can use a mapping of digits to their corresponding letters to generate combinations recursively.

---

## Approach

1. Create a mapping of digits to their corresponding letters based on a phone keypad.
2. Initialize a list to store the results.
3. Define a recursive backtracking function that takes the current index and the current combination of letters as a list.
   - If the index is equal to the length of the input digits, add the current combination to the results list and return.
   - Otherwise, iterate through the letters corresponding to the current digit and for each one:
     - Append the letter to the current combination.
     - Recursively call the backtracking function with the next index.
     - Backtrack by removing the last letter added to the current combination.
4. Call the backtracking function starting from index 0 and an empty combination.
5. Return the results list.

---

## Why This Works

- The backtracking approach systematically explores all possible combinations of letters for the given digits, ensuring that we do not miss any valid combinations.
- We explore every possible letter for each digit, and for each letter we explore all possible downstream combinations, which guarantees that we cover the entire solution space.

---

## Edge Cases

- Single digit input (e.g., "2") should return the corresponding letters.

---

## Time & Space Complexity

- Time: O(4^n) where n is the length of the input digits, since each digit can map to up to 4 letters.
- Space: O(n) for the recursion stack, where n is the length of the input digits.
  - The output list takes O(4^n) space in the worst case, but we typically consider the space complexity of the algorithm itself, which is O(n).

---

## Common Mistakes

- Not backtracking properly (e.g., forgetting to remove the last letter after exploring a path).
- Forgetting to return after adding a complete combination to the results list.

---

## Alternative Solutions

- Iterative approach using a queue to build combinations level by level. The downside is that the size of the queue is O(4^n) in the worst case, which can be less efficient than backtracking in terms of space.
