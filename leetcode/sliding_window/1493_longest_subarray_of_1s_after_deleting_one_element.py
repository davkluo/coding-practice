class Solution:
    def longest_subarray(self, nums: list[int]) -> int:
        """
        Description:
        Given a binary array nums, return the length of the longest subarray
        containing only 1's after deleting one element from the array. You must
        delete exactly one element.

        Example:
        longest_subarray([1, 1, 0, 1]) == 3
        """
        
        l = -1
        has_used_delete = False
        deleted_idx = None
        longest_ones = 0

        for r, num in enumerate(nums):
            if num == 1:
                ones_length = (r - l) - (1 if has_used_delete else 0)
                longest_ones = max(ones_length, longest_ones)
                continue

            if not has_used_delete:
                has_used_delete = True
            else:
                l = deleted_idx
 
            deleted_idx = r
        
        # if longest_ones is equal to original list length, we have to remove one
        return longest_ones if longest_ones < len(nums) else longest_ones - 1                            


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.longest_subarray([1, 1, 0, 1]) == 3
    assert s.longest_subarray([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 5
    assert s.longest_subarray([1, 1, 1]) == 2
    print("All tests passed.")