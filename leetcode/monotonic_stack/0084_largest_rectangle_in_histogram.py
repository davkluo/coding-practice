from typing import List

class Solution:
    def largest_rectangle_area(self, heights: List[int]) -> int:
        """
        Description:
        Given an array of integers heights representing the histogram's bar 
        height where the width of each bar is 1, return the area of the largest 
        rectangle in the histogram.

        Example:
        largest_rectangle_area([2,1,5,6,2,3]) == 10
        """
        
        def get_prev_smaller(heights):
            prev_smaller = {}
            stack = [] # monotonic increasing stack
            for i in range(len(heights)):
                curr_height = heights[i]
                while stack and heights[stack[-1]] >= curr_height:
                    stack.pop()
                prev_smaller[i] = stack[-1] if stack else -1
                stack.append(i)
            
            return prev_smaller

        def get_next_smaller(heights):
            next_smaller = {}
            stack = [] # monotonic increasing stack
            for i in range(len(heights)-1, -1, -1):
                curr_height = heights[i]
                while stack and heights[stack[-1]] >= curr_height:
                    stack.pop()
                next_smaller[i] = stack[-1] if stack else len(heights)
                stack.append(i)
            return next_smaller

        prev_smaller = get_prev_smaller(heights)
        next_smaller = get_next_smaller(heights)

        largest_area = 0
        for i in range(len(heights)):
            width = (next_smaller[i] - 1) - prev_smaller[i]
            curr_area = heights[i] * width
            largest_area = max(curr_area, largest_area)
        
        return largest_area
    

if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.largest_rectangle_area([2,1,5,6,2,3]) == 10
    assert s.largest_rectangle_area([2,4]) == 4
    assert s.largest_rectangle_area([0, 0, 0]) == 0
    assert s.largest_rectangle_area([10]) == 10
    print("All tests passed.")