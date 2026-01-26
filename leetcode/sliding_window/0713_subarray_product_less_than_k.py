from typing import List

class Solution:
    def num_subarray_product_less_than_k(self, nums: List[int], k: int) -> int:
        """
        Description:
        Given an array of positive integers nums and a positive integer k, 
        return the number of contiguous subarrays where the product of all the 
        elements in the subarray is strictly less than k.

        Example:
        num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8
        """
        
        if k <= 1: # no products < 1 possible with positive integers
            return 0
        
        num_subarrays = 0
        l = 0
        curr_product = 1

        for r in range(len(nums)):
            curr_product *= nums[r]
            while curr_product >= k:
                curr_product /= nums[l]
                l += 1
            # l is now the smallest index it can be with subarray ending at r
            # handles nums[r] >= k since l = r + 1 and curr_product = 1
            num_subarrays += r - l + 1

        return num_subarrays


if __name__ == "__main__":
    s = Solution()

    # Example from problem description
    assert s.num_subarray_product_less_than_k([10, 5, 2, 6], 100) == 8

    # Edge case: k <= 1 means no valid subarrays (all elements are positive)
    assert s.num_subarray_product_less_than_k([1, 2, 3], 0) == 0
    assert s.num_subarray_product_less_than_k([1, 2, 3], 1) == 0

    # Single element cases
    assert s.num_subarray_product_less_than_k([5], 10) == 1
    assert s.num_subarray_product_less_than_k([5], 5) == 0
    assert s.num_subarray_product_less_than_k([5], 1) == 0

    # All elements are 1
    assert s.num_subarray_product_less_than_k([1, 1, 1], 2) == 6  # all subarrays valid

    # Large k - all subarrays valid
    assert s.num_subarray_product_less_than_k([1, 2, 3], 1000) == 6

    # No valid subarrays (all products >= k)
    assert s.num_subarray_product_less_than_k([10, 10, 10], 5) == 0

    # Mixed case
    assert s.num_subarray_product_less_than_k([1, 2, 3, 4], 10) == 7

    # Two elements
    assert s.num_subarray_product_less_than_k([10, 5], 100) == 3  # [10], [5], [10,5]
    assert s.num_subarray_product_less_than_k([10, 5], 50) == 2   # [10], [5]

    print("All tests passed.")