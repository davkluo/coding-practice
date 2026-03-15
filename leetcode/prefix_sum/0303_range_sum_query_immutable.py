class NumArray:
    def __init__(self, nums: list[int]):
        """
        Instantiate a NumArray using the provided list of nums
        """
        
        self.nums = nums
        self.prefix_sums = []

        for i, num in enumerate(nums):
            self.prefix_sums.append(self.prefix_sums[-1] + num if i > 0 else num)

    def sum_range(self, left: int, right: int) -> int:
        """
        Description:
        Sum the elements of nums between indices left and right inclusive and 
        return the sum.
        """
        
        return self.prefix_sums[right] - self.prefix_sums[left] + self.nums[left]


if __name__ == "__main__":
    test_cases = [
        [[1, 2, 3, 4, 5], (0, 2), 6],
        [[1, 2, 3, 4, 5], (1, 3), 9],
        [[1, 2, 3, 4, 5], (0, 4), 15],
    ]
    for nums, (left, right), expected in test_cases:
        num_array = NumArray(nums)
        assert num_array.sum_range(left, right) == expected

    print("All tests passed.")