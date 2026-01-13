# 150 – Evaluate Reverse Polish Notation

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Stack
**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/

---

## Problem Summary
Given an array of string tokens representing an arithmetic expression in Reverse Polish Notation, evaluate the expression and return the result. Division should truncate towards zero.

---

## Key Insight
- Each operand affects the two most recent operands, so the LIFO structure of a stack is ideal.

---

## Approach
1. Initialize an empty stack.
2. Iterate through each token in the input array:
   - If the token is a number, convert it to an integer and push it onto the stack.
   - If the token is an operator (`+`, `-`, `*`, `/`), pop the top two numbers from the stack, apply the operator, and push the result back onto the stack.
   - Make sure to truncate division towards zero using either `int()` or `math.trunc()`.
3. After processing all tokens, the stack will contain one element, which is the result of the expression. Pop and return this element.

---

## Why This Works
- The stack structure allows us to easily access the most recent operands needed for each operation.

---

## Edge Cases
- Smallest input size (no operations).
- All operations.
- Multiplication and division with negative numbers.
- Result is negative.
- Multiplication with zero.

---

## Time & Space Complexity
- Time: O(n), where n is the number of tokens. Each token is processed once.
- Space: O(n), in the worst case, the stack can hold all the operands.

---

## Common Mistakes
- Not handling division truncation correctly.
- Popping operands in the wrong order for non-commutative operations (subtraction and division).

---

## Alternative Solutions
- Using recursion to evaluate the expression, though this is less efficient and more complex than using a stack, especially for non-commutative operations.