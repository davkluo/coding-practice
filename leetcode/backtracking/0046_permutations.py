from typing import List
from copy import deepcopy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Description:
        Given an array nums of distinct integers, return all the possible 
        permutations. You can return the answer in any order.

        Example:
        permute([1,2,3]) == [
            [1,2,3],
            [1,3,2],
            [2,1,3],
            [2,3,1],
            [3,1,2],
            [3,2,1]
        ]
        """
        
        permutations = []

        def backtrack(subarr, remaining):
            if len(subarr) == len(nums):
                permutations.append(deepcopy(subarr))
                return
            
            for i, is_available in enumerate(remaining):
                if is_available:
                    subarr.append(nums[i])
                    remaining[i] = False

                    backtrack(subarr, remaining)

                    remaining[i] = True
                    subarr.pop()

        # start with empty subarr, all numbers available for use
        backtrack([], [True] * len(nums))

        return permutations


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.permute([1,2,3]) == [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
    assert s.permute([0,1]) == [[0,1], [1,0]]
    assert s.permute([1]) == [[1]]
    print("All tests passed.")