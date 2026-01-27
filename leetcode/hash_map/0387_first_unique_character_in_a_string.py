from collections import defaultdict

class Solution:
    def first_uniq_char(self, s: str) -> int:
        """
        Description:
        Given a string, return the index of the first non-repeating character.
        If it does not exist, return -1. All characters are lowercase letters.

        Example:
        first_uniq_char("leetcode") == 0
        """
        
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        for i, c in enumerate(s):
            if counts[c] == 1:
                return i
        
        return -1


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.first_uniq_char("leetcode") == 0  # 'l' is first unique
    assert s.first_uniq_char("loveleetcode") == 2  # 'v' is first unique
    assert s.first_uniq_char("aabb") == -1  # no unique character
    assert s.first_uniq_char("a") == 0  # single character
    assert s.first_uniq_char("aadadaad") == -1  # all characters repeat
    assert s.first_uniq_char("abcdef") == 0  # all unique, return first
    print("All tests passed.")