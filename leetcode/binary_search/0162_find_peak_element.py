from typing import List

class Solution:
    def find_peak_element(self, nums: List[int]) -> int:
        """
        Description:
        A peak element is an element that is strictly greater than its 
        neighbors. Given an integer array nums, find a peak element, and return 
        its index. If the array contains multiple peaks, return the index to 
        any of the peaks. Out of bounds elements are considered to be negative 
        infinity. The algorithm must run in O(log n) time. No two consecutive 
        elements are equal.

        Example:
        find_peak_element([1,2,3,1]) == 2
        """
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            curr = nums[m]
            prev = nums[m-1] if m-1 >= 0 else float("-inf")
            next = nums[m+1] if m+1 < len(nums) else float("-inf")

            if curr > prev and curr > next:
                return m
            elif prev > curr:
                r = m - 1
            else: # next > curr
                l = m + 1


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.find_peak_element([1, 2, 3, 1]) == 2
    assert s.find_peak_element([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
    assert s.find_peak_element([1]) == 0
    assert s.find_peak_element([2, 1]) == 0
    assert s.find_peak_element([1, 2]) == 1
    print("All tests passed.")