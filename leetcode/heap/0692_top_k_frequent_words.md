# 692 – Top K Frequent Words

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Heap
**Secondary Patterns:** Hash Map, Sorting, Bucket Sort
**Link:** https://leetcode.com/problems/top-k-frequent-words/

---

## Problem Summary

Given a list of words and an integer k, return the k most frequent words. The answer should be sorted by frequency from highest to lowest. If two words have the same frequency, the word with the lower alphabetical order comes first.

---

## Key Insight

- Use a hash map to count the frequency of each word.
- Use a min-heap to keep track of the top k frequent words, ensuring that the heap size does not exceed k in order to optimize space and time complexity.
- We need custom sorting criteria because frequency and lexicographical order are compared in opposite directions.

---

## Approach

1. Define a custom class to represent entries in the heap, implementing comparison methods to handle frequency and lexicographical order.
   - Frequency is compared in ascending order (lower frequency is "smaller").
   - Lexicographical order is compared in descending order (higher alphabetical order is "smaller").
   - Overrides the `__lt__` method for heap comparisons.
2. Count the frequency of each word using a hash map.
3. Use a min-heap to store the top k frequent words. The heap will store entries of the custom class.
4. Iterate through the words and their frequencies:
   - Push each entry into the min-heap.
   - If the heap size exceeds k, pop the smallest entry.
5. Pop the remaining `k` entries from the heap; they will be in reverse order
6. Reverse the list to get the correct order and return it.

---

## Why This Works

- The hash map efficiently counts word frequencies in O(n) time.
- The min-heap ensures that we only keep the top k frequent words, maintaining a size of k, which optimizes both time and space complexity.
- The custom comparison logic ensures that the heap maintains the correct order based on the problem's requirements.

---

## Edge Cases

- All words are unique: The function should return the first k words in alphabetical order.
- All words are the same: The function should return that word k times.
- k is equal to the number of unique words: The function should return all words sorted by frequency and lexicographical order.

---

## Time & Space Complexity

- Time: O(n log k), where n is the number of words. Counting frequencies takes O(n), and each insertion into the heap takes O(log k).
- Space: O(n) for the frequency map and O(k) for the heap.

---

## Common Mistakes

- Not implementing the custom comparison logic correctly, leading to incorrect ordering in the heap.
- Forgetting to reverse the final list of results after popping from the heap, resulting in incorrect order.

---

## Alternative Solutions

- Sorting: Count frequencies and sort the list of unique words based on frequency and lexicographical order. This approach has a time complexity of O(n log n) and is less efficient for large datasets compared to the heap approach.
- Max-Heap: Use a max-heap to store all words and their negated frequencies, then pop the top k elements. This approach is less efficient than using a min-heap of size k.
- Bucket Sort: Use bucket sort to group words by frequency and then collect the top k frequent words. This approach can be more complex to implement but can achieve O(n) time complexity in certain scenarios.
  - To sort words in the same bucket, we can either use a simple sort, a min-heap, a trie, or a balanced BST.
