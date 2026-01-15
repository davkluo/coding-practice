# 207 – Course Schedule

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Graph, Topological Sort, DFS, BFS
**Link:** https://leetcode.com/problems/course-schedule/

---

## Problem Summary
You are given the number of courses and a list of prerequisite pairs. Each pair [a, b] indicates that to take course a, you must first complete course b. Determine if it is possible to finish all courses given these prerequisites.

---

## Key Insight
- The problem can be reframed as a cycle detection problem in a directed graph. If there is a cycle, it is impossible to complete all courses.
- Topological sorting can be used to determine if a valid order of courses exists.
- BFS or DFS can also be used to detect cycles in the graph.

---

## Approach
### DFS Cycle Detection
1. Construct a directed graph from the prerequisites.
2. Initialize a visited set to track courses on the current DFS path.
3. Use DFS to explore each node, keeping track of the courses in the current path. If you revisit a course in the current path, a cycle exists.
4. If a cycle is detected during the DFS, return False. If all nodes are processed without detecting a cycle, return True.

### BFS with Kahn's Algorithm
1. Construct a directed graph and compute the in-degree for each course.
2. Construct also the reverse graph to track which courses depend on each course.
3. Initialize a counter for the number of courses that can be completed.
4. Initialize a queue with all courses that have an in-degree of 0 (no prerequisites).
5. Process each course in the queue, reducing the in-degree of its dependent courses. If any dependent course's in-degree reaches 0, add it to the queue.
6. If all courses are processed, return True; otherwise, return False.

### Topological Sort using DFS
1. Construct a directed graph from the prerequisites.
2. Perform a DFS to generate a postorder traversal of the graph.
3. The postorder traversal can be used to derive a topological sort of the courses.
4. Each prerequisite pair represents a directed edge in the graph. We must ensure that for each edge (b -> a), course b appears before course a in the topological order. In other words, course b should have a higher postorder number than course a.
5. Since the DFS topological sort does not consider self-loops, we simultaneously check for any edges that form a self-loop. If a self-loop is detected, return False.
6. If no self-loops are found and all edges satisfy the topological order condition, return True.

---

## Why This Works
- DFS cycle detection works because revisiting a node in the current path indicates a back edge, which forms a cycle.
- Kahn's algorithm works because if we can process all nodes (courses) by continually removing nodes with zero in-degrees, it indicates that there are no cycles.
- Topological sorting works because a valid topological order can only exist in a Directed Acyclic Graph (DAG).

---

## Edge Cases
- No prerequisites: If there are no prerequisites, all courses can be completed.
- Self-loops: A course that requires itself as a prerequisite makes it impossible to complete.
- Loops involving multiple courses: Ensure that cycles involving multiple nodes are detected.
- Loop between two courses

---

## Time & Space Complexity
- Time: O(V + E) where V is the number of courses and E is the number of prerequisite pairs.
- Space: O(V + E) for storing the graph and auxiliary data structures.

---

## Common Mistakes
- Not handling self-loops correctly in the topological sort approach.
- Forgetting to backtrack the visited set in DFS cycle detection. If we instead use a separate set for each helper function call, we increase space complexity unnecessarily.

---

## Alternative Solutions
- 3 different approaches are provided above