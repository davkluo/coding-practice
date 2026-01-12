from typing import List

class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        """
        Description:
        Given an integer array nums, find the subarray with the largest sum, 
        and return its sum.

        Example:
        max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6
        """
        
        max_sum = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(current_sum, max_sum)

        return max_sum            

if __name__ == "__main__":
    s = Solution()
    assert s.max_sub_array([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert s.max_sub_array([1]) == 1
    assert s.max_sub_array([5,4,-1,7,8]) == 23
    assert s.max_sub_array([-1,-2,-3,-4]) == -1
    print("All tests passed.")