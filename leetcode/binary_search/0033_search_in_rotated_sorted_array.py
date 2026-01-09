from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Description:
        Given an integer array nums sorted in ascending order, and an integer 
        target, write a function to search target in nums. If target exists, 
        then return its index. Otherwise, return -1. You must write an algorithm 
        with O(log n) runtime complexity.

        Example:
        search([4,5,6,7,0,1,2], 0) -> 4
        """
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] > target:
                # large numbers rotated in front or target larger than l
                # = target is in left partition
                if nums[l] > nums[m] or nums[l] <= target:
                    r = m - 1
                else:
                    l = m + 1 

            else:
                # small numbers rotated to rear or target smaller than r
                # = target is in right partition
                if nums[m] > nums[r] or target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

if __name__ == "__main__":
    s = Solution()
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    assert s.search([4,5,6,7,0,1,2], 3) == -1
    assert s.search([1], 0) == -1
    print("All tests passed.")