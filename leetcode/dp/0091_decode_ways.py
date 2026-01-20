class Solution:
    def num_decodings(self, s: str) -> int:
        """
        Description:
        Given a secret message encoded as a string of numbers, return the total 
        number of ways to decode it. The mapping is as follows: 'A' -> 1, 
        'B' -> 2, ..., 'Z' -> 26.

        Example:
        num_decodings("226") == 3
        """
        
        if s[0] == "0":
            return 0
        
        prev_ways, curr_ways = 1, 1 # tracks ways up to 2 and 1 char prior
        
        for i in range(len(s)):
            ways = 0
            if s[i] in "123456789": # valid single char decode
                ways += curr_ways

            if i == 0:
                continue

            # valid 2 char decode
            if ((s[i-1] == "1" and s[i] in "0123456789")
                or s[i-1] == "2" and s[i] in "0123456"):
                ways += prev_ways
            
            prev_ways = curr_ways
            curr_ways = ways
        
        return curr_ways


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.num_decodings("12") == 2
    assert s.num_decodings("226") == 3
    assert s.num_decodings("0") == 0
    assert s.num_decodings("06") == 0
    assert s.num_decodings("10") == 1
    assert s.num_decodings("27") == 1
    print("All tests passed.")