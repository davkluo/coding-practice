from collections import deque

class Solution:
    def total_fruits(self, fruits: list[int]) -> int:
        """
        Description:
        Given an array of integers fruits where fruits[i] is the type of fruit 
        the i-th tree produces, you start at any tree and collect one fruit from
        each tree while moving to the right until you cannot anymore. You can
        only have at most two types of fruits in your baskets. Return the most
        amount of fruit you can collect.

        Example:
        total_fruits([1, 2, 1]) == 3
        """
        
        # store types and last indices                
        fruit_types = deque()
        fruits_to_idx = {}
        l = -1
        most_fruit = 0
        for r, fruit in enumerate(fruits):
            # extend window only
            if fruit in fruit_types:
                most_fruit = max(r - l, most_fruit)
                fruits_to_idx[fruit] = r
                if fruit == fruit_types[0]:
                    # swap to most recently used if it was next for eviction
                    fruit_types.append(fruit_types.popleft())
            else:
                # add fruit from next tree
                fruit_types.append(fruit)
                fruits_to_idx[fruit] = r

                # prune baskets to 2 fruit types
                if len(fruit_types) > 2:
                    removed = fruit_types.popleft()
                    l = fruits_to_idx[removed]

            most_fruit = max(r - l, most_fruit)
        
        return most_fruit


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.total_fruits([1, 2, 1]) == 3
    assert s.total_fruits([0, 1, 2, 2]) == 3
    assert s.total_fruits([1, 2, 3, 2]) == 3
    assert s.total_fruits([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert s.total_fruits([1, 0, 1, 4, 1, 4, 1, 2, 3]) == 5
    print("All tests passed.")