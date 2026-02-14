class Solution:
    def can_jump(self, nums: list[int]):
        """
        Description:
        Given an integer array nums, you are initially positioned at the array's
        first index, and each element represents the maximum jump length at that
        position. Return true if you can reach the last index, or false
        otherwise


        Example:
        can_jump([2, 3, 1, 1, 4]) == True
        """
        
        max_reachable = 0

        for i in range(len(nums)):
            if max_reachable < i:
                return False
            
            max_reachable = max(i + nums[i], max_reachable)
        
        return True


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.can_jump([2, 3, 1, 1, 4]) == True
    assert s.can_jump([3, 2, 1, 0, 4]) == False
    assert s.can_jump([0]) == True
    assert s.can_jump([1]) == True
    assert s.can_jump([0, 1]) == False
    assert s.can_jump([1, 0]) == True
    assert s.can_jump([2, 0, 0]) == True
    assert s.can_jump([1, 1, 1, 0]) == True
    assert s.can_jump([1, 0, 1, 0]) == False
    assert s.can_jump([5, 0, 0, 0, 0, 0]) == True
    print("All tests passed.")