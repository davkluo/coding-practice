# 70 – Climbing Stairs

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Dynamic Programming
**Link:** https://leetcode.com/problems/climbing-stairs/

---

## Problem Summary

There are `n` steps to climb. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

---

## Key Insight

- The number of ways to climb `n` steps can be expressed as the sum of the ways to climb `n-1` and `n-2` steps
- This is because to reach the `n`-th step, you could have come from either the `n-1`-th step (taking 1 step) or the `n-2`-th step (taking 2 steps)
- The base case is that there are 0 ways to climb -1 steps (unreachable), and 1 way to climb 0 steps (do nothing)

---

## Approach

1. Initialize two variables to store the number of ways to climb to the last two steps: `one_step_prior` and `two_steps_prior`
2. Iterate `n` times:
   - Calculate the number of ways to climb to the current step as the sum of the last two variables
   - Update the last two variables for the next iteration
3. Return `one_step_prior`, which will hold the number of ways to climb `n` steps after the loop

---

## Why This Works

- The problem can be broken down into smaller subproblems, which is a hallmark of dynamic programming
- By storing the results of the last two steps, we avoid redundant calculations and achieve an efficient solution
- There is a well-defined base case and recurrence relation

---

## Edge Cases

- n = 1: There is only one way to climb (taking one step)

---

## Time & Space Complexity

- Time: O(n) - We compute the number of ways for each step from 1 to n
- Space: O(1) - We only use a constant amount of space to store the last two results

---

## Common Mistakes

- Handling the base cases incorrectly
  - You can either use the base cases of n = -1 and n = 0, or directly initialize the first two steps in the loop

---

## Alternative Solutions

- Recursive approach with memoization: This would involve defining a recursive function that calls itself for `n-1` and `n-2`, while storing results in a dictionary to avoid redundant calculations. However, this approach has higher overhead compared to the iterative solution given the memory usage and function call stack.
