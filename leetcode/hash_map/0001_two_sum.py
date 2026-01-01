from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Description:
        Given an array of integers and a target, return the indices of two 
        numbers that sum up to the target. There is a unique solution. 

        Example:
        two_sum([2, 7, 11, 15], 9) == [0, 1]
        """
        
        nums_to_idx = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_to_idx:
                return [nums_to_idx[complement], i]
            
            nums_to_idx[num] = i


if __name__ == "__main__":
    # Optional local test
    s = Solution()
    assert s.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert s.two_sum([3, 2, 4], 6) == [1, 2]
    assert s.two_sum([3, 3], 6) == [0, 1]

    print("All tests passed.")
