from typing import List
from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Description:
        Given an integer array nums of unique elements, return all possible 
        subsets (the power set). The solution set must not contain duplicate 
        subsets. Return the solution in any order.

        Example:
        subsets([1, 2, 3]) == [
            [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
        ]
        """
        
        power_set = [[]]

        def backtrack(curr, i):
            if i >= len(nums):
                return
            
            curr.append(nums[i])
            power_set.append(deepcopy(curr))
            backtrack(curr, i+1) # include element at i
            curr.pop()
            # no copy needed here because an earlier path would have added it
            backtrack(curr, i+1) # don't include element at i

        backtrack([], 0)

        return power_set
    
    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        power_set = []

        def backtrack(curr, i):
            power_set.append(deepcopy(curr))

            # each loop skips over some quantity of the following numbers
            for i in range(i, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i+1)
                curr.pop()
        
        backtrack([], 0)

        return power_set


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs_to_test = [s.subsets, s.subsets_2]
    for f in funcs_to_test:
        assert sorted(f([1, 2, 3])) == sorted([
            [], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]
        ])
        assert sorted(f([0])) == sorted([[], [0]])
    print("All tests passed.")