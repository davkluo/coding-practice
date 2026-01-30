from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Description:
        Given an array of integers nums which is sorted in ascending order, and 
        an integer target, write a function to search target in nums. If target 
        exists, then return its index. Otherwise, return -1.
        
        Example:
        search([-1,0,3,5,9,12], 9) == 4
        """
        
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.search([-1,0,3,5,9,12], 9) == 4
    assert s.search([-1,0,3,5,9,12], 2) == -1
    assert s.search([1], 1) == 0
    assert s.search([1, 2, 3, 4, 5], 3) == 2
    print("All tests passed.")