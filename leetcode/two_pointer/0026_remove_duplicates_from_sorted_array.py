from typing import List

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Description:
        Given an integer array in non-decreasing order, remove the duplicates 
        in-place while maintaining the relative order. If there are k unique
        elements in nums, the result should have the first k elements be unique
        numbers in sorted order. The remainder of the elements do not matter, so
        there is no need to remove them.

        Example:
        remove_duplicates([1,1,2]) == [1,2,_]
        """
        
        swap_idx = 0
        i = 0

        while i < len(nums):
            curr = nums[i]
            nums[i], nums[swap_idx] = nums[swap_idx], nums[i]
            swap_idx += 1

            i += 1
            while i < len(nums) and nums[i] == curr:
                i += 1            
        
        return swap_idx


if __name__ == "__main__":
    s = Solution()

    # Test case 1: LeetCode example 1
    nums1 = [1, 1, 2]
    k1 = s.remove_duplicates(nums1)
    assert k1 == 2, f"Expected k=2, got {k1}"
    assert nums1[:k1] == [1, 2], f"Expected [1, 2], got {nums1[:k1]}"

    # Test case 2: LeetCode example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = s.remove_duplicates(nums2)
    assert k2 == 5, f"Expected k=5, got {k2}"
    assert nums2[:k2] == [0, 1, 2, 3, 4], f"Expected [0, 1, 2, 3, 4], got {nums2[:k2]}"

    # Test case 3: Single element
    nums3 = [1]
    k3 = s.remove_duplicates(nums3)
    assert k3 == 1, f"Expected k=1, got {k3}"
    assert nums3[:k3] == [1], f"Expected [1], got {nums3[:k3]}"

    # Test case 4: All same elements
    nums4 = [5, 5, 5, 5, 5]
    k4 = s.remove_duplicates(nums4)
    assert k4 == 1, f"Expected k=1, got {k4}"
    assert nums4[:k4] == [5], f"Expected [5], got {nums4[:k4]}"

    # Test case 5: No duplicates
    nums5 = [1, 2, 3, 4, 5]
    k5 = s.remove_duplicates(nums5)
    assert k5 == 5, f"Expected k=5, got {k5}"
    assert nums5[:k5] == [1, 2, 3, 4, 5], f"Expected [1, 2, 3, 4, 5], got {nums5[:k5]}"

    # Test case 6: Negative numbers
    nums6 = [-3, -1, -1, 0, 0, 0, 2]
    k6 = s.remove_duplicates(nums6)
    assert k6 == 4, f"Expected k=4, got {k6}"
    assert nums6[:k6] == [-3, -1, 0, 2], f"Expected [-3, -1, 0, 2], got {nums6[:k6]}"

    print("All tests passed.")