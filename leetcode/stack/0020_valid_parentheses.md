# 20 – Valid Parentheses

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Stack  
**Link:** https://leetcode.com/problems/valid-parentheses/description/

---

## Problem Summary
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if:
1. Open brackets are closed by the same type of brackets.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Key Insight
A stack provides a natural way to ensure that brackets are closed in the correct order, since it is LIFO and brackets match the most recently opened one first.

---

## Approach
1. Initialize a stack to keep track of opening brackets.
2. Create a mapping of closing brackets to their corresponding opening brackets.
3. Iterate through each character in the string:
   - If the character is a closing bracket, check if the stack is not empty and if the top of the stack matches the corresponding opening bracket. If not, return false.
   - If the character is an opening bracket, push it onto the stack.
4. After processing all characters, check if the stack is empty. If it is, return true; otherwise, return false.

---

## Why This Works
Using a stack ensures that we always match the most recently opened bracket first, which is essential for maintaining the correct order of bracket closure. The mapping allows for quick verification of matching pairs.

---

## Edge Cases
- Empty input
- Nested brackets
- Mismatched pairs
- Excess closing or opening brackets
- Single open bracket
- Single close bracket

---

## Time & Space Complexity
- Time: O(n)
    - We traverse the string once, performing O(1) operations for each character.
- Space: O(n)
    - In the worst case, we may store all opening brackets in the stack.

---

## Common Mistakes
- Not checking if the stack is empty before popping.
- Forgetting to check if the stack is empty at the end.

---

## Alternative Solutions
- Recursive approach is less efficient because of increased call stack usage and more complex than using a stack.
