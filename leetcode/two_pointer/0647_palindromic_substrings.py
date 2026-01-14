class Solution:
    def count_substrings(self, s: str) -> int:
        """
        Description:
        Given a string s, return the number of palindromic substrings in it.

        Example:
        count_substrings("aaa") == 3
        """
        
        num_palindromes = 0

        def expand(l: int, r: int):
            nonlocal num_palindromes

            while l >= 0 and r < len(s) and s[l] == s[r]:
                num_palindromes += 1
                l -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i, i)
            if i < len(s)-1:
                expand(i, i+1)
        
        return num_palindromes


if __name__ == "__main__":
    s = Solution()
    assert s.count_substrings("aaa") == 6
    assert s.count_substrings("abc") == 3
    assert s.count_substrings("aba") == 4
    assert s.count_substrings("a") == 1
    print("All tests passed.")