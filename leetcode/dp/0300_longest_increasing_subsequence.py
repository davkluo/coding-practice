class Solution:
    def length_of_LIS(self, nums: list[int]):
        """
        Description:
        Given an integer array nums, return the length of the longest strictly
        increasing subsequence.

        Example:
        length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        """
        
        # let dp[i] be the LIS ending at i and including nums[i]
        dp = [0] * len(nums) 

        for i, num in enumerate(nums):
            longest = 1
            for j in range(0, i):
                if num > nums[j]:
                    longest = max(dp[j] + 1, longest)
            
            dp[i] = longest
        
        return max(dp)

    def length_of_LIS_2(self, nums: list[int]):
        """ 
        Binary search approach based on patience sorting. Included here for
        reference. The idea is to maintain a sorted list of buckets as we 
        traverse the integers (hence O(n log n)), replacing buckets when smaller
        than the ones encountered are found and adding buckets when new maximum
        values are found. The number of buckets at the end is the length of the
        LIS.

        The central idea is that when we find smaller elements, we swap them in
        so that the LIS length does not change, but we allow more opportunity
        for a longer LIS by decreasing the current sequence.

        For full explanation refer to: https://www.geeksforgeeks.org/dsa/longest-monotonically-increasing-subsequence-size-n-log-n/
        """

        buckets = []

        def find_bucket_idx(num: int) -> int:
            """ Returns index of bucket to replace with num """
            l, r = 0, len(buckets)-1
            while l < r:
                m = (l + r) // 2
                if num > buckets[m]:
                    l = m + 1
                else:
                    r = m
            
            return l
                
        for num in nums:
            if not buckets or num > buckets[-1]:
                buckets.append(num)
            else:
                idx_to_replace = find_bucket_idx(num)
                buckets[idx_to_replace] = num
        
        return len(buckets)


if __name__ == "__main__":
    s = Solution()
    # test cases
    for func in [s.length_of_LIS, s.length_of_LIS_2]:
        assert func([10, 9, 2, 5, 3, 7, 101, 18]) == 4
        assert func([0, 1, 0, 3, 2, 3]) == 4
        assert func([7, 7, 7, 7, 7, 7, 7]) == 1
        assert func([1]) == 1
        assert func([1, 2, 3, 4, 5]) == 5
        assert func([5, 4, 3, 2, 1]) == 1
        assert func([3, 1, 4, 1, 5, 9, 2, 6]) == 4
        assert func([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
    print("All tests passed.")