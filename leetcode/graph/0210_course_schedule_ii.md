# 210 – Course Schedule II

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Graph, DFS, BFS, Topological Sort
**Link:** https://leetcode.com/problems/course-schedule-ii/

---

## Problem Summary
Given the total number of courses and a list of prerequisite pairs, return an ordering of courses you should take to finish all courses. If it is impossible to finish all courses, return an empty array.

---

## Key Insight
- This is similar to 207. Course Schedule, but with the added requirement of returning the actual order of courses.
- If using DFS, the ordering of when courses are confirmed to be completable can be used to build the order.
- If using BFS (Kahn's Algorithm), the order in which nodes are processed gives the valid course order.
- If using topological sort, we can derive the order directly from the reverse topological sort once we confirm the graph is a DAG.

---

## Approach
### DFS with Cycle Detection
1. Build the adjacency list for the graph.
2. Initialize a set for confirmed courses, a set for courses in the current path, and a list for the course order.
3. Define a recursive DFS function that:
   - Checks if the course is already confirmed; if so, return True.
   - Checks if the course is in the current path; if so, return False (cycle detected).
   - Adds the course to the current path.
   - Recursively visits all prerequisites, short circuiting if a recursive call returns False.
   - After visiting all prerequisites, removes the course from the current path, adds it to confirmed, and appends it to the course order.
4. Iterate through all courses, calling the DFS function.
5. If a cycle is detected, return an empty list.
6. Return the course ordering.

---

## Why This Works
- DFS ensures that we explore all prerequisites before confirming a course can be completed.
- Cycle detection prevents infinite loops and ensures that we only return valid course orders.

---

## Edge Cases
- No prerequisites
- All courses form a cycle
- Self loops
- Two courses are co-dependent

---

## Time & Space Complexity
- Time: O(V + E), where V is the number of courses and E is the number of prerequisite pairs.
- Space: O(V + E) for the adjacency list
    - Recursion stack: O(V)
    - Sets for confirmed and current path: O(V)
    - Course order list: O(V)

---

## Common Mistakes
- Not handling cycles correctly, leading to infinite recursion.
- Forgetting to add courses to the confirmed set after processing.
- Remembering to return a boolean from the DFS function to indicate cycle detection.

---

## Alternative Solutions
- Like 207. Course Schedule, we can also implement this using Kahn's Algorithm (BFS) or topological sort techniques to achieve the same result.