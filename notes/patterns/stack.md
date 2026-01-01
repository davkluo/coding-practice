# Pattern: Stack

---

## When to Use
- When you need to process elements in a Last In First Out (LIFO) order.
- When you need to keep track of nested structures, such as parentheses or HTML tags.
- When you need to reverse the order of elements.
- When you need to backtrack, such as in depth-first search algorithms.

---

## Core Idea
A stack is a linear data structure that follows the LIFO principle, meaning the last element added to the stack is the first one to be removed. This property makes stacks ideal for problems that require tracking of recent elements or nested structures.

---

## Common Techniques
- Push and Pop: Add elements to the top of the stack and remove elements from the top.
- Peek: View the top element without removing it.
- Use a stack to track opening elements (like brackets) and match them with closing elements.

---

## Typical Time Complexity
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Overall traversal of n elements: O(n)

---

## Common Pitfalls
- Forgetting to check if the stack is empty before popping or peeking.
- Mismanaging the order of operations, leading to incorrect results.
- Not handling edge cases, such as unbalanced structures or empty inputs.

---

## Canonical Problems
- Valid Parentheses (LeetCode 20)