from collections import deque

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Reverse technique
        O(1) space, O(n) time

        Description:
        Given an array, rotate the array to the right by k steps

        Example:
        rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
        """

        if k == 0:
            return
        
        def reverse_range(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        n = len(nums)
        shift = k % n

        # reverse nums in place
        reverse_range(0, n - 1)

        # reverse first k for rollover elements
        reverse_range(0, shift - 1)

        # reverse remaining
        reverse_range(shift, n - 1)


    def rotate_2(self, nums: list[int], k: int) -> None:
        """
        Cyclic replacements
        O(1) space, O(n) time, but a lot of overhead
        """

        if k == 0:
            return
        
        n = len(nums)
        shifts = k % n
        num_rotated = 0
        start_idx = 0
        curr = 0 # next index to swap into place
        tmp = nums[curr]

        while num_rotated < n:
            next_pos = (curr + shifts) % n            
            tmp, nums[next_pos] = nums[next_pos], tmp
            num_rotated += 1
            curr = next_pos

            if curr == start_idx: # offset for common denominator
                start_idx = (start_idx + 1) % n
                curr = start_idx
                tmp = nums[curr]           


    def rotate_3(self, nums: list[int], k: int) -> None:
        """
        Array slicing
        O(n) space, O(n) time
        """
        
        if k == 0:
            return
        
        n = len(nums)
        shifts = k % n
        nums[:] = nums[n-shifts:] + nums[:n-shifts]


    def rotate_4(self, nums: list[int], k: int) -> None:
        """
        Deque
        O(n) space, O(n) time
        """

        if k == 0:
            return
        
        n = len(nums)
        shifts = k % n
        queue = deque(nums)

        for _ in range(shifts):
            queue.appendleft(queue.pop())

        for i in range(n):
            nums[i] = queue.popleft()


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [
        s.rotate, 
        s.rotate_2, 
        s.rotate_3, 
        s.rotate_4
    ]

    inputs_outputs = [
        (([1, 2, 3, 4, 5, 6, 7], 3), [5, 6, 7, 1, 2, 3, 4]),
        (([-1, -100, 3, 99], 2), [3, 99, -1, -100]),
        (([1, 2, 3, 4, 5], 0), [1, 2, 3, 4, 5]),
        (([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
    ]

    for func in funcs:
        for (nums, k), expected in inputs_outputs:
            copy_nums = nums.copy() # so we don't modify inputs_outputs
            func(copy_nums, k)
            assert copy_nums == expected
    print("All tests passed.")