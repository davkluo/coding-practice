class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        """
        Description:
        Given two strings s1 and s2, return true if s2 contains a permutation 
        of s1, or false otherwise. All characters in the strings are lowercase 
        English letters.

        Example:
        check_inclusion("ab", "eidbaooo") == True
        """
        
        n = len(s1)
        m = len(s2)

        if n > m:
            return False
        
        s1_counts = [0] * 26
        for c in s1:
            s1_counts[ord(c) - ord("a")] += 1

        s2_counts = [0] * 26
        window_start = 0
        for i, c in enumerate(s2):
            s2_counts[ord(c) - ord("a")] += 1
            window_length = i - window_start + 1

            if window_length > n:
                s2_counts[ord(s2[window_start]) - ord("a")] -= 1
                window_start += 1

            if s1_counts == s2_counts:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.check_inclusion("ab", "eidbaooo") == True
    assert s.check_inclusion("ab", "eidboaoo") == False
    assert s.check_inclusion("adc", "dcda") == True
    assert s.check_inclusion("hello", "olleh") == True
    print("All tests passed.")