class Solution:
    def length_of_longest_substring(self, s: str) -> int:
        """
        Description:
        Given a string, find the length of the longest substring without
        duplicate characters

        Example:
        length_of_longest_substring("abcabcbb") == 3
        """
        
        if len(s) <= 1:
            return len(s)
        
        l = 0
        seen_at = {} # mapping of character to index last seen at
        longest_substring = 0

        for r in range(len(s)):
            c = s[r]
            # exclude earlier occurrence if in substring window
            if c in seen_at and seen_at[c] >= l:
                l = seen_at[c] + 1
            seen_at[c] = r
            longest_substring = max(r - l + 1, longest_substring)

        return longest_substring


if __name__ == "__main__":
    s = Solution()
    assert s.length_of_longest_substring("abcabcbb") == 3
    assert s.length_of_longest_substring("bbbbb") == 1
    assert s.length_of_longest_substring("pwwkew") == 3
    assert s.length_of_longest_substring("") == 0
    assert s.length_of_longest_substring("a") == 1
    print("All tests passed.")