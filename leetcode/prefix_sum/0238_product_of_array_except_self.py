from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        """
        Description:
        Given an integer array nums, return an array answer such that answer[i] 
        is equal to the product of all the elements of nums except nums[i]. The
        product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
        integer. You must write an algorithm that runs in O(n) time and without 
        using the division operation.

        Example:
        product_except_self([1,2,3,4]) == [24,12,8,6]
        """
        
        prods = [None] * len(nums)

        prefix_prod = 1
        for i in range(len(nums)):
            prods[i] = prefix_prod
            prefix_prod *= nums[i]
        suffix_prod = 1
        for i in range(len(nums)-1, -1, -1):
            prods[i] *= suffix_prod
            suffix_prod *= nums[i]
        
        return prods

if __name__ == "__main__":
    s = Solution()
    assert s.product_except_self([1,2,3,4]) == [24,12,8,6]
    assert s.product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert s.product_except_self([0,0]) == [0,0]
    print("All tests passed.")