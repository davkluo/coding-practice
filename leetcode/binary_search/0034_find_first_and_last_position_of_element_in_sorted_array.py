class Solution:
    def search_range(self, nums: list[int], target: int) -> list[int]:
        """
        Description:
        Given a non-decreasing array of integers and a target value, return the
        starting and ending position of the target value in the array. If it is
        not in the array, return [-1, -1].

        Example:
        search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
        """

        target_range = [-1, -1]
        
        # find start
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                target_range[0] = m
                r = m - 1
        
        # short circuit check for end if not found
        if target_range[0] == -1:
            return target_range

        # find end; no need to look at elements before target range start
        l, r = target_range[0], len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                target_range[1] = m
                l = m + 1

        return target_range


if __name__ == "__main__":
    s = Solution()
    # test cases
    # target value repeated
    assert s.search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    # target value not in array
    assert s.search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    # target value not repeated
    assert s.search_range([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    # target value at beginning
    assert s.search_range([8, 8, 8, 9, 10], 8) == [0, 2]
    # target value at end
    assert s.search_range([1, 2, 3, 8, 8], 8) == [3, 4]

    print("All tests passed.")