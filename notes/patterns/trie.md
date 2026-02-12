# Pattern: Trie

---

## When to Use

- Problems involving prefix matching, autocomplete, or checking if any word starts with a given prefix.
- Searching for multiple words/patterns simultaneously in a shared search space (e.g., a grid or stream of characters).
- Problems where a hash set of words works but you need to prune based on prefix to avoid exploring invalid paths.

---

## Core Idea

- A trie (prefix tree) stores strings character-by-character in a tree structure, where each node represents a single character and paths from root to marked nodes spell out stored words.
- Shared prefixes share the same path, so lookup and prefix checks are O(L) where L is the string length, independent of how many words are stored.
- Walking the trie in lockstep with another search (e.g., DFS on a grid) lets you prune entire branches the moment the current prefix doesn't match any stored word.

---

## Common Techniques

- **TrieNode structure:** Each node has a `children` dict (char -> TrieNode) and an `is_end_of_word` flag.
- **Insert:** Walk char-by-char from root, creating child nodes as needed, then mark the final node.
- **Search / starts_with:** Walk char-by-char from root; return False if any char is missing from children.
- **Trie + Backtracking:** Build a trie from target words, then DFS through the search space while traversing the trie simultaneously — only explore directions that match a child in the current trie node.
- **Duplicate prevention:** Set `is_end_of_word = False` after finding a word to avoid recording it again.
- **Trie pruning:** Remove leaf nodes after finding their word to shrink the trie and reduce future search space.

---

## Typical Time Complexity

- **Insert / Search / Prefix check:** O(L) per operation, where L is the length of the word.
- **Building a trie from W words:** O(W \* L).
- **Trie + grid DFS:** O(W _ L + m _ n \* 4^L) in the worst case, but the trie pruning makes it much faster in practice.

---

## Common Pitfalls

- Forgetting that the trie only prunes — the DFS backtracking logic (seen set, undo steps) still needs to be correct.
- Not handling duplicates: if the same word can be reached via multiple paths, you need a mechanism to prevent adding it twice (e.g., clearing `is_end_of_word`).
- Inconsistency between the current trie node and the current DFS state — the trie node must always correspond to the last character in the current path.
- Using a flat word set instead of a trie — a set can only check complete words, not prefixes, so it can't prune invalid paths early and ends up exploring a much larger search space.

---

## Canonical Problems

- Implement Trie / Prefix Tree (LeetCode 208)
- Word Search II (LeetCode 212)
