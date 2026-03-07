class Solution:
    def sort_colors(self, nums: list[int]) -> None:
        """
        Description:
        Given an array nums with integers 0, 1, 2 representing the colors red,
        white, and blue respectively, sort the array in-place so that objects
        of the same color are adjacent, with the colors in the order red, white,
        and blue.

        Example:
        sort_colors([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
        """

        swap_r, swap_b = 0, len(nums)-1

        i = 0
        while i <= swap_b: # everything after swap_b is already in place
            color = nums[i]

            if color == 0:
                nums[swap_r], nums[i] = nums[i], nums[swap_r]
                swap_r += 1
                i = swap_r # everything before swap_r is already in place
            elif color == 2:
                nums[swap_b], nums[i] = nums[i], nums[swap_b]
                swap_b -= 1
            else:
                # even if the white color gets swapped later on, it will never 
                # be swapped beyond swap_r or swap_b
                i += 1


if __name__ == "__main__":
    s = Solution()
    # test cases
    nums_1 = [2, 0, 2, 1, 1, 0]
    s.sort_colors(nums_1)
    assert nums_1 == [0, 0, 1, 1, 2, 2]

    nums_2 = [0, 1, 2]
    s.sort_colors(nums_2)
    assert nums_2 == [0, 1, 2]

    nums_3 = [2, 1, 0]
    s.sort_colors(nums_3)
    assert nums_3 == [0, 1, 2]

    nums_4 = [0, 0, 0]
    s.sort_colors(nums_4)
    assert nums_4 == [0, 0, 0]

    nums_5 = [1, 1, 1]
    s.sort_colors(nums_5)
    assert nums_5 == [1, 1, 1]

    nums_6 = [2, 2, 2]
    s.sort_colors(nums_6)
    assert nums_6 == [2, 2, 2]

    print("All tests passed.")