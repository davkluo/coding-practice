from collections import defaultdict

class Solution:
    def character_replacement(self, s: str, k: int) -> int:
        """
        Description:
        Given a string and an integer k, you can choose any character of the 
        string and change it to any other uppercase English character. You can 
        perform this operation at most k times. Find the length of the longest 
        substring containing all repeating letters you can get after performing 
        the above operations.

        Example:
        """

        max_length = 0
        l = 0
        counts = defaultdict(int)
        majority_char = None

        for r in range(len(s)):
            c = s[r]
            counts[c] += 1       

            # update majority character
            if not majority_char or counts[c] > counts[majority_char]:
                majority_char = c

            length = r - l + 1
            # shift left pointer if too many modifications used
            if length - counts[majority_char] > k:
                counts[s[l]] -= 1
                l += 1
            else:
                max_length = max(length, max_length)

        return max_length


if __name__ == "__main__":
    s = Solution()
    assert s.character_replacement("ABAB", 2) == 4
    assert s.character_replacement("A", 1) == 1
    assert s.character_replacement("A", 0) == 1
    assert s.character_replacement("AABBCCCC", 0) == 4
    assert s.character_replacement("AABABBA", 1) == 4
    print("All tests passed.")
