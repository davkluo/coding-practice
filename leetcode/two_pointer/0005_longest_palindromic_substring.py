class Solution:
    def longest_palindrome(self, s: str) -> str:
        """
        Description:
        Given a string s, return the longest palindromic substring in s.

        Example:
        longest_palindrome("cbbd") == "bb"
        """

        max_length = 0
        longest_l, longest_r = 0, 0

        def expand(start_l: int, start_r: int) -> None:
            """ 
            Expand outwards and find longest palindrome from starting pointers 
            """

            nonlocal max_length, longest_l, longest_r

            l, r = start_l, start_r
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curr_length = r - l + 1
                if curr_length > max_length:
                    max_length = curr_length
                    longest_l, longest_r = l, r
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i) # odd length
            if i < len(s) - 1:
                expand(i, i+1) # even length

        return s[longest_l:longest_r+1]            

if __name__ == "__main__":
    s = Solution()
    assert s.longest_palindrome("babad") in ["bab", "aba"]
    assert s.longest_palindrome("cbbd") == "bb"
    assert s.longest_palindrome("a") == "a"
    assert s.longest_palindrome("ac") in ["a", "c"]
    assert s.longest_palindrome("forgeeksskeegfor") == "geeksskeeg"
    assert s.longest_palindrome("bb") == "bb"
    assert s.longest_palindrome("abccba") == "abccba"
    print("All tests passed.")