from typing import List

class Solution:
    def check_subarray_sum(self, nums: List[int], k: int) -> bool:
        """
        Description:
        Given an integer array nums and an integer k, return true if nums has a
        continuous subarray of size at least two whose elements sum up to a 
        multiple of k.

        Example:
        check_subarray_sum([23, 2, 4, 6, 7], 6) == True
        """
        
        mod_to_idx = {}
        mod_to_idx[0] = -1

        curr_sum = 0
        for i, num in enumerate(nums):
            curr_sum += num
            mod = curr_sum % k
            if mod in mod_to_idx:
                if i - mod_to_idx[mod] >= 2:
                    return True
            else:
                mod_to_idx[mod] = i

        return False


if __name__ == "__main__":
    s = Solution()
    # test cases

    # Basic cases from problem examples
    assert s.check_subarray_sum([23, 2, 4, 6, 7], 6) == True  # 2+4=6 is multiple of 6
    assert s.check_subarray_sum([23, 2, 6, 4, 7], 6) == True  # 2+6+4=12 is multiple of 6

    # No valid subarray exists
    assert s.check_subarray_sum([23, 2, 6, 4, 7], 13) == False

    # Edge case: consecutive zeros (0+0=0 is multiple of any k)
    assert s.check_subarray_sum([0, 0], 1) == True
    assert s.check_subarray_sum([0, 0], 7) == True

    # Edge case: zeros in array
    assert s.check_subarray_sum([1, 0, 0], 5) == True  # 0+0=0 is multiple of 5
    assert s.check_subarray_sum([0, 1, 0], 5) == False  # no valid subarray

    # k=1: every sum is a multiple of 1
    assert s.check_subarray_sum([1, 2, 3], 1) == True

    # Single element array (subarray must be size >= 2)
    assert s.check_subarray_sum([5], 5) == False

    # Two element array
    assert s.check_subarray_sum([5, 0], 5) == True  # 5+0=5 is multiple of 5
    assert s.check_subarray_sum([1, 2], 5) == False  # 1+2=3 is not multiple of 5

    # Entire array sums to multiple of k
    assert s.check_subarray_sum([1, 2, 3], 6) == True  # 1+2+3=6

    # Large k value
    assert s.check_subarray_sum([1, 2], 100) == False

    # Negative scenario with larger array
    assert s.check_subarray_sum([1, 2, 12], 6) == False

    print("All tests passed.")