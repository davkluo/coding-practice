from typing import List

class Solution:
    def min_sub_array_len(self, target: int, nums: List[int]) -> int:
        """
        Description:
        Given an array of positive integers and a positive integer target,
        find the minimal length of a subarray whose sum is greater than or equal
        to the target. If there is no such subarray, return a zero.

        Example:
        max_sub_array_len(7, [2,3,1,2,4,3]) -> 2
        """
        
        l, r = 0, 0 # subarray bounds; inclusive
        curr_sum = nums[0]
        min_len = len(nums) + 1

        while l <= r and r < len(nums):
            if curr_sum >= target:
                min_len = min(r - l + 1, min_len)
                # shorten subarray
                curr_sum -= nums[l]
                l += 1
            else: # lengthen subarray
                r += 1
                if r < len(nums):
                    curr_sum += nums[r]
        
        return min_len if min_len < len(nums) + 1 else 0


if __name__ == "__main__":
    s = Solution()
    assert s.min_sub_array_len(7, [2,3,1,2,4,3]) == 2
    assert s.min_sub_array_len(4, [1,4,4]) == 1
    assert s.min_sub_array_len(11, [1,1,1,1,1,1,1,1]) == 0
    assert s.min_sub_array_len(1, [1]) == 1
    assert s.min_sub_array_len(2, [1]) == 0
    assert s.min_sub_array_len(1, [2]) == 1
    print("All tests passed.")
