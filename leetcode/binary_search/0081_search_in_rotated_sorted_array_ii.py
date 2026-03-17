class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        Description:
        Given an integer array nums sorted in non-decreasing order and then 
        rotated at an unknown pivot, and an integer target, return true if 
        target is in nums, or false if it is not.

        Example:
        search([5, 6, 7, 0, 1, 2], 0) == True
        """
        
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return True
            
            if nums[m] > target:
                # target in [l, m)
                if nums[l] <= target or nums[l] > nums[m]:
                    r = m - 1
                elif nums[l] == nums[m]:
                    l += 1
                else:
                    l = m + 1
            else:
                # target in (m, r]
                if nums[r] >= target or nums[r] < nums[m]:
                    l = m + 1
                elif nums[r] == nums[m]:
                    r -= 1
                else:
                    r = m - 1
        
        return False


if __name__ == "__main__":
    s = Solution()
    # test cases

    # target is in the array
    # assert s.search([5, 6, 7, 0, 1, 2], 0) == True

    # target is not in the array
    # assert s.search([5, 6, 7, 0, 1, 2], 3) == False

    # array is not rotated
    # assert s.search([1, 2, 3, 4, 5], 3) == True

    # array has duplicates
    # assert s.search([2, 5, 6, 0, 0, 1, 2], 0) == True
    # assert s.search([2, 5, 6, 0, 0, 1, 2], 3) == False

    # target is the smallest element
    # assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == True

    # target is the largest element
    # assert s.search([4, 5, 6, 7, 0, 1, 2], 7) == True

    assert s.search([1, 0, 1, 1, 1], 0) == True

    print("All tests passed.")