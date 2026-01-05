from typing import List
from collections import defaultdict

class Solution:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
        """
        Description:
        Given an array of integers and an integer k, return the k most frequent
        elements in any order. The algorithm should have a time complexity
        better than O(n log n).

        Example:
        top_k_frequent([1,1,1,2,2,3], 2) -> [1,2]
        """
        
        if len(nums) == 1:
            return [nums[0]]
        
        top_k = []
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        
        buckets = [[] for _ in range(len(nums))]
        for num, count in counts.items():
            buckets[count-1].append(num)

        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                top_k.append(num)
                if len(top_k) == k:
                    return top_k


if __name__ == "__main__":
    s = Solution()
    assert s.top_k_frequent([1,1,1,2,2,3], 2) == [1,2]
    assert s.top_k_frequent([1], 1) == [1]
    assert s.top_k_frequent([4,1,-1,2,-1,2,3], 2) == [-1,2]
    assert s.top_k_frequent([1,2,1,2,1,2,3,1,3,2], 2) == [1,2]
    print("All tests passed.")