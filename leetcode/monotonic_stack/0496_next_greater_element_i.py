from typing import List

class Solution:
    def next_greater_element(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Description:
        Given two arrays nums1 and nums2 where nums1 is a subset of nums2, find 
        the next greater element for each element in nums1 in the array nums2.
        The next greater element of a number x in nums2 is the first greater 
        number to its right in nums2. If it does not exist, return -1 for this 
        number. Each element in nums1 and nums2 is unique.

        Example:
        next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1]
        """
        
        num_to_next_greater = {}
        stack = []

        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            while stack and stack[-1] < num:
                stack.pop()
            
            num_to_next_greater[num] = stack[-1] if stack else -1                
            stack.append(num)
        
        return [num_to_next_greater[num] for num in nums1]


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.next_greater_element([4,1,2], [1,3,4,2]) == [-1,3,-1]
    assert s.next_greater_element([2,4], [1,2,3,4]) == [3,-1]
    print("All tests passed.")