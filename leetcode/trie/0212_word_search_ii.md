# 212 – Word Search II

**Platform:** LeetCode
**Difficulty:** Hard
**Primary Pattern:** Trie + Backtracking
**Link:** https://leetcode.com/problems/word-search-ii/

---

## Problem Summary

Given an m x n board of characters and a list of words, return all words that can be formed by tracing a path of sequentially adjacent (horizontal/vertical) cells on the board, without reusing any cell in a single path.

---

## Key Insight

- This is Word Search (79) extended to multiple words.
- Backtracking DFS from every starting cell is the natural approach, but it can be very inefficient if we have many words or long words.
- By constructing a trie from the list of words, we can prune the search space by only exploring paths that match valid prefixes of the target words.

---

## Approach

### Brute Force (find_words)

1. Put all words into a set and track the maximum word length.
2. From every cell, run backtracking DFS building up a substring, checking the set at each step.
3. Cap path length at `max_word_len` to avoid unbounded exploration.
4. Collect matches in a `found_words` set to avoid duplicates.

### Trie-Optimized (find_words_trie)

1. Insert all words into a trie.
2. From every cell whose character exists as a child of the trie root, run backtracking DFS while simultaneously traversing the trie.
3. At each step, only explore neighbors whose character is a child of the current trie node — this prunes invalid prefixes immediately.
4. When `is_end_of_word` is reached, record the word and set the flag to `False` to prevent duplicate results.
5. Terminate early if all words have been found.

---

## Why This Works

- The trie encodes every valid prefix of the target words. By checking `adjacent_char not in curr.children` at each DFS step, we never explore a path that can't lead to any target word.
- This is a massive improvement over the brute force, which must build every possible substring up to `max_word_len` and look it up in the set — it cannot prune based on prefix.
- Setting `is_end_of_word = False` after finding a word prevents duplicates without needing a separate set

---

## Edge Cases

- No words can be formed from the board (return empty list).
- A word requires a cell that appears multiple times on the board but only once in the word — the `seen` set prevents reuse within a single path.
- Board contains a word's characters but not in a connected path

---

## Time & Space Complexity

### Brute Force

- Time: O(m*n*4^L), where L is `max_word_len`. Every cell starts a DFS that branches 4 ways up to depth L, and each step does an O(L) string join + set lookup.
- Space: O(W \* L) for the set of words, plus O(L) for the recursion stack and seen set.

### Trie-Optimized

- Time: O(W _ L + m _ n \* 4^L), where the first term is trie construction and the second is the board DFS. In practice much faster because the trie prunes most branches early.
- Space: O(W \* L) for the trie, plus O(L) for the recursion stack and seen set.

---

## Common Mistakes

- Not preventing duplicate words in the result (the brute force uses a set; the trie solution clears `is_end_of_word`).
- Forgetting to backtrack properly — must remove the cell from `seen` and pop from `substr` after recursing.
- Building the full substring at every DFS step (expensive); building incrementally with a list and joining only when needed is more efficient.
- Not pruning the search early — without the trie's prefix check or at least a `max_word_len` cap, the DFS can explore far too many paths.
- Not prepopulating the seen set with the starting cell, which allows it to be reused immediately in the next step.
- Inconsistency with the current node
  - You can either treat it as including the current cell or not, but the surrounding variables (seen set, substr, adjacent cell checks) must be consistent with that choice.

---

## Alternative Solutions

- **Trie node pruning:** After finding a word, prune leaf nodes from the trie to further reduce the search space on subsequent DFS calls.
- **Using board mutation** (e.g., replacing visited cells with `#`) instead of a `seen` set, which saves space but modifies the input.
