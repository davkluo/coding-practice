# 424 – Longest Repeating Character Replacement

**Platform:** LeetCode
**Difficulty:** Medium
**Primary Pattern:** Sliding Window
**Secondary Patterns:** Hash Map, String
**Link:** https://leetcode.com/problems/longest-repeating-character-replacement/

---

## Problem Summary
Given a string `s` and an integer `k`, you can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times. Return the length of the longest substring containing the same letter you can get after performing the above operations.

---

## Key Insight
- Use a sliding window to maintain a substring that does not require more than `k` replacements to become uniform.
- There is no need to ever contract the window length because we are only interested in finding longer valid substrings at that point.
    - So when we need to move the left pointer, we simply move the left and right pointers together by one position.
- Keep track of the count of the most frequent character in the current window to determine if the window is valid.
- The number of replacements needed is the size of the window minus the count of the most frequent character.
- When the left pointer moves, we only need to update the count of characters; we do not need to recalculate the maximum frequency character in the window.
    - Instead, when we encounter characters using the right pointer, we update the maximum frequency character by comparing the count of the newly added character with the current count of the maximum frequency character (which is updated when we move the left pointer).
- The idea of "what if the max frequency character changes when we move the left pointer and I have not tracked what the previous max frequency character was?" is not an issue because:
    - Once again, we are only interested in finding longer valid substrings.
    - Even if the majority character changes, the window size will not increase until we encounter more of the new majority character using the right pointer, at which point the maximum frequency character will be updated accordingly with the counts that we have tracked.

---

## Approach
1. Initialize two pointers `left` and `right` to represent the sliding window, a dictionary to count character frequencies, and variables to track the maximum frequency character count and the maximum length found.
2. Iterate the `right` pointer over the string:
   - Update the frequency count of the character at the `right` pointer.
   - Update the maximum frequency character count if necessary.
   - Check if the current window size minus the maximum frequency character count exceeds `k`. If it does, move the `left` pointer to shrink the window and update the frequency counts accordingly.
   - If the number of replacements does not exceed `k`, update the maximum length found if the current window size is larger than the previously recorded maximum length.
3. Return the maximum length found.

---

## Why This Works
- The sliding window approach efficiently explores all possible substrings while maintaining the constraints of the problem.
- We are expanding the window whenever possible while maintaining the fact that only `k` replacements are allowed. The maximum length is only updated when we find a valid window.
- The use of a frequency dictionary allows us to quickly determine how many replacements are needed for the current window.
- The `left` pointer is only moved by 1 alongside the `right` pointer when the window becomes invalid.
    - We do not need to shift it until we "undo a replacement" because we are only interested in finding longer valid substrings.
    - We are simply shifting the window forward to see if there is a longer valid substring ahead.
- If doesn't matter if the majority character changes when we move the left pointer, because the counts are still being tracked.
    - Even if the majority character changes, we don't do anything until we encounter another occurrence of the new majority character using the right pointer, at which point the majority character will be updated and the length of the window can potentially increase again.

---

## Edge Cases
- Single character strings.
- Strings where no replacements are needed.
- No replacements allowed but there are repeated characters.

---

## Time & Space Complexity
- Time: O(n) – Each character is processed at most twice (once by each pointer).
- Space: O(1) – The frequency dictionary will have at most 26 entries for uppercase English letters.

---

## Common Mistakes
- Forgetting to update the counts when moving the pointers
- Not checking the condition for the number of replacements correctly
- Failing to update the maximum length when a valid window is found
- Falling for the trap of "I need to recalculate the max frequency character when moving the left pointer"
- Falling for the trap of "I need to move the left pointer until I regain one of my used replacements"

---

## Alternative Solutions
- None that I can think of that are more efficient than the sliding window approach for this problem.