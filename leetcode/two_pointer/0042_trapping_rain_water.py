from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Description:
        Given n non-negative integers representing an elevation map where the 
        width of each bar is 1, compute how much water it can trap after 
        raining.

        Example:
        trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
        """
        
        if len(height) <= 2:
            return 0

        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)
        water_trapped = [0] * len(height)

        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i-1], height[i-1])

        for i in range(len(height)-2, 0, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i+1])

        for i in range(len(height)):
            contained_height = min(prefix_max[i], suffix_max[i])
            if contained_height > height[i]:
                water_trapped[i] = contained_height - height[i]

        return sum(water_trapped)
    
    def trap_2(self, height: List[int]) -> int:
        """
        Two-pointer approach to solve the trapping rain water problem.
        This method uses O(1) space complexity.
        """

        if len(height) <= 2:
            return 0
        
        l, r = 0, len(height)-1
        left_max, right_max = height[l], height[r]
        trapped_water = 0

        while l < r:
            if left_max < right_max: # left wall is limiting factor
                l += 1
                if left_max >= height[l]: # next l is lower so water is trapped
                    trapped_water += left_max - height[l]
                else: # no water trapped, update left_max
                    left_max = height[l]
            else: # right wall is limiting factor
                r -= 1
                if right_max >= height[r]:
                    trapped_water += right_max - height[r]
                else:
                    right_max = height[r]

        return trapped_water


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [s.trap, s.trap_2]
    for f in funcs:
        assert f([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
        assert f([4,2,0,3,2,5]) == 9
        assert f([1]) == 0
        assert f([2,0,2]) == 2
    print("All tests passed.")