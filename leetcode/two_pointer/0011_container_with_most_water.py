from typing import List

class Solution:
    def max_area(self, height: List[int]) -> int:
        """
        Description:
        Given an array of non-negative heights, corresponding to vertical lines
        at the associated index, find the maximum area of water that can be
        contained between two lines.

        Example:
        max_area([1,8,6,2,5,4,8,3,7]) -> 49
        """

        l, r = 0, len(height) - 1
        max_water_area = 0

        while l < r:
            water_area = (r - l) * min(height[l], height[r])
            max_water_area = max(water_area, max_water_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_water_area


if __name__ == "__main__":
    s = Solution()
    assert s.max_area([1,8,6,2,5,4,8,3,7]) == 49
    assert s.max_area([1,1]) == 1
    print("All tests passed.")