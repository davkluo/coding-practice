# 49 – Group Anagrams

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Hash Map
**Link:** https://leetcode.com/problems/group-anagrams/

---

## Problem Summary
Given an array of strings, group the anagrams together. You can return the answer in any order. All inputs are lowercase English letters.

---

## Key Insight
- Anagrams have the same character counts for each letter.
- A unique fingerprint can be created for each group of anagrams by counting the occurrences of each letter and enforcing a consistent order.
- A consistent order can be achieved by using a fixed-size array (of length 26 for lowercase English letters) to store counts, or by sorting the letters in the string.

---

## Approach
1. Initialize a hash map (dictionary) to store groups of anagrams.
2. For each string in the input array:
   - Count the occurrences of each letter using a fixed-size array of length 26.
   - Convert this array into a tuple (to make it hashable) to use as a key in the hash map.
   - Append the string to the list corresponding to this key in the hash map.
3. Finally, return the values of the hash map as a list of lists.

---

## Why This Works
- Anagrams have identical character counts for each letter.
- By using a fixed-size array to count letters, we create a unique and consistent fingerprint for each group of anagrams without needing to sort.

---

## Edge Cases
- Empty strings: Should be grouped together.
- Single character strings: Each character should be its own group unless duplicates exist.
- Long or short strings: The approach scales well regardless of string length.

---

## Time & Space Complexity
- Time: O(N * K), where N is the number of strings and K is the maximum length of a string (for counting letters).
- Space: O(N) for storing the hash map.
    - Each string is stored as a reference to the input strings in the hash map, hence it is not O(N * K).
    - Each fixed-size array for letter counts uses O(1) space.

---

## Common Mistakes
- Using sorted strings as keys can lead to higher time complexity due to sorting.
- Forgetting to handle edge cases like empty strings or single-character strings.
- Using a fixed-size array is preferable to creating a dictionary and then converting it to a string, due to overhead and instability based on python version.

---

## Alternative Solutions
- Sorting each string and using the sorted string as a key in the hash map. This approach has a time complexity of O(N * K log K) due to sorting.