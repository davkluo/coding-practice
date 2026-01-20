from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Description:
        Given an integer array nums representing the amount of money of each 
        house, return the maximum amount of money you can rob tonight without 
        alerting the police (i.e., you cannot rob two adjacent houses).

        Example:
        rob([1,2,3,1]) == 4
        """
        
        two_prior = 0
        one_prior = 0

        for num in nums:
            best_choice = max(num + two_prior, one_prior)
            two_prior = one_prior
            one_prior = best_choice
        
        return one_prior


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([2,1,1,2]) == 4
    assert s.rob([0]) == 0
    assert s.rob([1]) == 1
    assert s.rob([1,2]) == 2
    print("All tests passed.")