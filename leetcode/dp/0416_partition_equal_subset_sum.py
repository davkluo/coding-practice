class Solution:
    def can_partition(self, nums: list[int]) -> bool:
        """
        Description:
        Given an integer array nums, return True if you can partition the array
        into two subsets of equal sum, and False otherwise.

        Example:
        can_partition([1, 5, 11, 5]) == True
        """

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False

        target_sum = total_sum // 2
        dp = [[False for _sum in range(target_sum + 1)] 
              for _num in range(len(nums) + 1)]
        
        # base cases
        # dp[0, b] = False for 0 < b <= target_sum; can't make target w/o nums
        # dp[i, 0] = True for 0 <= i <= target_sum; can always make target 0
        for i in range(len(nums) + 1):
            dp[i][0] = True

        # recurrence relation
        # dp[i, b] = (dp[i-1, b-nums[i-1]] if nums[i-1] <= b) OR dp[i-1, b]
        for b in range(1, target_sum + 1):
            for i in range(1, len(nums) + 1):
                num = nums[i-1]
                if num <= b and dp[i-1][b-num]:
                    dp[i][b] = True
                else:
                    dp[i][b] = dp[i-1][b]

        # if dp[len(nums), target_sum] = True we have a partition
        # since the total sum is double target_sum, there must be another subset
        # in nums that contains the complementing target_sum
        return dp[-1][-1]
    
    def can_partition_2(self, nums: list[int]) -> bool:
        """ 
        1D space-optimized alternative:
        Note that the above solution only relies on the previous row i-1.
        This means we can condense it to a 1D array simply by overwriting the
        row one at a time.
        """

        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        target_sum = total_sum // 2
        dp = [True] + [False] * target_sum

        for num in nums:
            # backwards to avoid using the same number to build up incrementally
            for b in range(target_sum, num-1, -1):
                dp[b] = dp[b] or dp[b - num] # already meets target or take num
        
        return dp[-1]
    

if __name__ == "__main__":
    s = Solution()

    for func in [s.can_partition, s.can_partition_2]:
        assert func([1, 5, 11, 5]) == True
        assert func([1, 2, 3, 5]) == False
        assert func([1, 1]) == True
        assert func([1, 2, 5]) == False
        assert func([3, 3, 3, 4, 5]) == True
        assert func([1]) == False
        assert func([100]) == False
        assert func([1, 2, 3, 4, 5, 6, 7]) == True

    print("All tests passed.")