from typing import List
import heapq

class Solution:
    def find_kth_largest(self, nums: List[int], k: int) -> int:
        """
        Description:
        Given an integer array nums and an integer k, return the kth largest 
        element in the array. Try to solve it without sorting.

        Example:
        find_kth_largest([3,2,1,5,6,4], 2) == 5
        """

        heap = []

        # store k largest elements in min-heap
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        # next pop from min-heap will be the kth largest
        return heapq.heappop(heap)

if __name__ == "__main__":
    s = Solution()
    assert s.find_kth_largest([3,2,1,5,6,4], 2) == 5
    assert s.find_kth_largest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert s.find_kth_largest([2, 2, 2, 1, 1, 1], 2) == 2
    assert s.find_kth_largest([1], 1) == 1
    print("All tests passed.")