class Solution:
    def majority_element(self, nums: list[int]) -> int:
        """
        Description:
        Given a list of integers, find the majority element. There is always a
        majority element in the list, which is the element that appears more 
        than n/2 times.

        Example:
        majority_element([3, 2, 3]) == 3
        """
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1
        
        return candidate


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.majority_element([3, 2, 3]) == 3
    assert s.majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majority_element([1]) == 1
    assert s.majority_element([1, 1, 1, 2, 2]) == 1
    print("All tests passed.")