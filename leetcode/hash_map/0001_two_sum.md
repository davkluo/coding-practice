# 1 – Two Sum

**Platform:** LeetCode 
**Difficulty:** Easy 
**Primary Pattern:** Hash Map  
**Link:** https://leetcode.com/problems/two-sum/description/

---

## Problem Summary
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. There is a unique solution and the same element cannot be used twice.

---

## Key Insight
For each integer we are looking for its complement that will sum up to the target. We can search the integers seen up until that point to ensure no element is used twice. Using a hash map for the check avoids checking all pairs.

---

## Approach
1. Create a hash map to store the seen integers and the indices they appear at.
2. Iterate through the array and check if each integer's complement has been seen.
    - If yes return the complement's index and the current index as a solution
    - If not add the current integer to the hash map

---

## Invariant
Each integer is checked for a pairing with all previous integers.

## Why This Works
- Invariant avoids using the same element twice
- Each element is only processed once
- Hash map lookup takes constant time
- Since there is a unique solution we are guaranteed to find it by the time we encounter the second integer in the unique solution.

---

## Edge Cases
- Duplicate values
- Negative integers in array
- negative target
- Solution uses identical values at different indices

---

## Time & Space Complexity
- Time: O(n)
    - Single iteration over integers
    - Each iteration performs constant time hash map lookup and hash map addition
- Space: O(n)
    - Hash map entries

---

## Common Mistakes
- Inserting integer into hash map before checking for complement
- Using the same element twice
- Returning values instead of indices

---

## Alternative Solutions
- None that are equally or more efficient