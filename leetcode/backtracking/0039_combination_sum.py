from typing import List
from copy import deepcopy

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Description:
        Given an array of distinct integers candidates and a target integer 
        target, return a list of all unique combinations of candidates where 
        the chosen numbers sum to target. You may return the combinations in 
        any order. The same number may be chosen from candidates an unlimited 
        number of times. Two combinations are unique if the frequency of at 
        least one of the chosen numbers is different. It is guaranteed that the 
        number of unique combinations that sum up to target is less than 150 
        combinations for the given input.

        Example:
        combination_sum([2,3,6,7], 7) == [[7], [2,2,3]]
        """

        combinations = []

        def backtrack(subcombination, i, target):
            if target == 0:
                combinations.append(deepcopy(subcombination))

            # cannot reach target on this path            
            if target <= 0 or i >= len(candidates):
                return
            
            # explore path where we take candidate at i
            subcombination.append(candidates[i])
            backtrack(subcombination, i, target-candidates[i])
            subcombination.pop()

            # explore path where we don't take candidate at i
            backtrack(subcombination, i+1, target)
        
        backtrack([], 0, target)
        return combinations


if __name__ == "__main__":
    s = Solution()
    # test cases
    def compare_lists(list_1, list_2):
        return sorted([sorted(sublist) for sublist in list_1]) == sorted([sorted(sublist) for sublist in list_2])
    
    assert compare_lists(s.combination_sum([2,3,6,7], 7), [[7], [2,2,3]])
    assert compare_lists(s.combination_sum([2,3,5], 8), [[2,2,2,2], [2,3,3], [3,5]])
    assert compare_lists(s.combination_sum([2], 1), [])
    assert compare_lists(s.combination_sum([1], 1), [[1]])
    assert compare_lists(s.combination_sum([1], 2), [[1,1]])
    print("All tests passed.")