from typing import List

class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """
        Description:
        Given an integer array, return all triplets such that elements are not
        reused and the sum of each triplet equals zero. The solution set must
        not contain duplicate triplets

        Example:
        three_sum([-1,0,1,2,-1,4]) == [[-1,-1,2],[-1,0,1]]
        """

        nums.sort()
        triplets = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break

            j, k = i+1, len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum > 0:
                    k -= 1
                elif curr_sum < 0:
                    j += 1
                else:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                
                    # skip duplicate matches
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return triplets


if __name__ == "__main__":
    s = Solution()
    # test cases

    # Example case
    assert s.three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]

    # Empty array
    assert s.three_sum([]) == []

    # Array with less than 3 elements
    assert s.three_sum([0, 1]) == []

    # No solution
    assert s.three_sum([1, 2, 3]) == []

    # All zeros
    assert s.three_sum([0, 0, 0]) == [[0, 0, 0]]

    # Multiple zeros with other numbers
    assert s.three_sum([0, 0, 0, 0]) == [[0, 0, 0]]

    # Single solution
    assert s.three_sum([-1, 0, 1]) == [[-1, 0, 1]]

    # Multiple solutions
    assert s.three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]

    # Large numbers
    assert s.three_sum([-4, -1, -1, 0, 1, 2]) == [[-1, -1, 2], [-1, 0, 1]]

    # All negative numbers
    assert s.three_sum([-5, -4, -3, -2, -1]) == []

    print("All tests passed.")