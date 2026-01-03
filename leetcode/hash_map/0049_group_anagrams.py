from typing import List, Tuple
from collections import defaultdict

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Description:
        Given an array of strings, group anagrams together and return them as a
        list of lists. All strings consist of lowercase letters.

        Example:
        group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) ==
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
        """

        groupings = defaultdict(list)

        for s in strs:
            counts = self.count_letters(s)
            groupings[counts].append(s)

        return list(groupings.values())
    

    def count_letters(self, s) -> Tuple[int, ...]:
        """ 
        Return a tuple of length 26 that contains the counts for the letters in 
        str.
        """

        counts = [0] * 26 # including a-z avoids sorting of present letters
        for c in s:
            counts[ord(c) - ord("a")] += 1
        
        return tuple(counts)


if __name__ == "__main__":
    s = Solution()
    assert s.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == \
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
    assert s.group_anagrams(["racecar", "carer", "racer", "hello"]) == \
        [["racecar"], ["carer", "racer"], ["hello"]]
    assert s.group_anagrams([""]) == [[""]]
    assert s.group_anagrams(["a"]) == [["a"]]
    print("All tests passed.")
