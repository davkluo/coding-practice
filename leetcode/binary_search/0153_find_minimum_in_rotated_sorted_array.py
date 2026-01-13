from typing import List

class Solution:
    def find_min(self, nums: List[int]) -> int:
        """
        Description:
        Given a rotated sorted array of unique elements, return the minimum
        element in the array. The solution must run in O(log n) time complexity.

        Example:
        find_min([3,4,5,1,2]) == 1
        """

        l, r, = 0, len(nums) - 1
        while l <= r:
            # window is sorted
            if nums[l] <= nums[r]:
                return nums[l] 
        
            # window contains rotation
            m = (l + r) // 2
            if nums[m] >= nums[l]: # rotation is on right, m can't be min
                l = m + 1
            else: # rotation is on left, m could be min
                r = m

if __name__ == "__main__":
    s = Solution()
    assert s.find_min([3,4,5,1,2]) == 1
    assert s.find_min([4,5,6,7,0,1,2]) == 0
    assert s.find_min([11,13,15,17]) == 11
    assert s.find_min([2,1]) == 1
    assert s.find_min([1]) == 1
    print("All tests passed.")