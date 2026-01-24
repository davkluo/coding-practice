from typing import List

class Solution:
    def longest_consecutive(self, nums: List[int]) -> int:
        """
        Description:
        Given an unsorted array of integers, return the length of the longest
        consecutive elements sequence in O(n) time.

        Example:
        longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
        """
        
        num_to_range = {} # numbers to the consecutive range they are a part of
        longest = 0

        for num in nums:
            if num in num_to_range:
                continue

            l_neighbor, r_neighbor = num - 1, num + 1

            if l_neighbor in num_to_range and r_neighbor in num_to_range:
                # merge ranges and update for ends of the range
                l_neighbor_start = num_to_range[l_neighbor][0]
                r_neighbor_end = num_to_range[r_neighbor][1]
                new_range = [l_neighbor_start, r_neighbor_end]

                num_to_range[l_neighbor_start] = new_range
                num_to_range[num] = new_range
                num_to_range[r_neighbor_end] = new_range

                longest = max(r_neighbor_end - l_neighbor_start + 1,
                              longest)
                
            elif l_neighbor in num_to_range: # extend left neighbor's range
                l_neighbor_start = num_to_range[l_neighbor][0]             
                new_range = [l_neighbor_start, num]

                num_to_range[l_neighbor_start] = new_range
                num_to_range[num] = new_range

                longest = max(num - l_neighbor_start + 1, longest)

            elif r_neighbor in num_to_range: # extend right neighbor's range
                r_neighbor_end = num_to_range[r_neighbor][1]
                new_range = [num, r_neighbor_end]
                
                num_to_range[r_neighbor_end] = new_range
                num_to_range[num] = new_range

                longest = max(r_neighbor_end - num + 1, longest)

            else: # standalone num
                num_to_range[num] = [num, num]

                longest = max(1, longest)

        return longest

    def longest_consecutive_2(self, nums: List[int]) -> int:
        """
        Alternative implementation using a set to track starts of sequences.
        """

        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set:
                current_num = num

                while current_num + 1 in num_set:
                    current_num += 1

                longest = max(current_num - num + 1, longest)

        return longest


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [s.longest_consecutive, s.longest_consecutive_2]
    for f in funcs:
        assert f([100, 4, 200, 1, 3, 2]) == 4  # sequence: 1,2,3,4
        assert f([]) == 0  # empty array
        assert f([1]) == 1  # single element
        assert f([1, 1, 1, 1]) == 1  # duplicates
        assert f([1, 2, 3, 10, 11, 12, 13]) == 4  # two sequences
        assert f([-1, 0, 1, 2]) == 4  # negative numbers
        assert f([10, 30, 50]) == 1  # no consecutive
        assert f([0, -1, 1, 2, -2, -3]) == 6  # mixed negatives
    print("All tests passed.")