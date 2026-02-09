# 733 – Flood Fill

**Platform:** LeetCode
**Difficulty:** Easy
**Primary Pattern:** Graph Traversal (DFS/BFS)  
**Link:** https://leetcode.com/problems/flood-fill/description/

---

## Problem Summary

Given a 2D array representing an image, a starting pixel (sr, sc), and a new color, replace the color of the starting pixel and all adjacent pixels that share its color with the new color.

---

## Key Insight

- This problem is simply a connectivity problem from the starting pixel to all that share the same color
- Either BFS or DFS will work

---

## Approach

1. Store the original color of the starting pixel
2. If the original color is the same as the new color, return the image (no changes needed)
3. Initialize a visited set to keep track of pixels we've already processed
4. Use a queue (for BFS) or stack (for DFS) to explore the image
5. Initialize the queue/stack with the starting pixel
6. While the queue/stack is not empty:
   - Pop a pixel from the queue/stack
   - If the pixel is not visited yet:
     - Mark it as visited
     - Update the pixel's color to the new color
     - Add all adjacent pixels (up, down, left, right) that have the same original color to the queue/stack
7. Return the modified image

---

## Why This Works

- By using BFS or DFS, we ensure that we explore all connected pixels that share the same color as the starting pixel
- The visited set prevents us from processing the same pixel multiple times

---

## Edge Cases

- Old and new colors are the same
- Single pixel image
- Image with all pixels the same color

---

## Time & Space Complexity

- Time: O(n\*m) where n and m are the dimensions of the image (in the worst case, we may need to visit every pixel)
- Space: O(n\*m) in the worst case for the visited set and the queue/stack

---

## Common Mistakes

- Forgetting to check if the original color is the same as the new color, which can lead to infinite loops
- Not marking pixels as visited, which can also lead to infinite loops
- Not checking bounds when adding adjacent pixels to the queue/stack
- Not using the original color of the starting pixel and instead using the current pixel's color, which can lead to incorrect results

---

## Alternative Solutions

- Both DFS and BFS are already efficient.
