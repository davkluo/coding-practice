class Solution:
    def can_complete_circuit(self, gas: list[int], cost: list[int]) -> int:
        """
        Description:
        Given two integer arrays gas and cost, where gas[i] is the amount of gas
        at the i-th gas station, and cost[i] is the cost of gas to travel from
        the i-th station to the next (i + 1)-th station. You begin the journey 
        with an empty tank at one of the gas stations. Return the starting gas 
        station's index if you can travel around the circuit once in the 
        clockwise direction, otherwise return -1.

        Example:
        can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
        """
        
        if sum(gas) < sum(cost):
            return -1
        
        # guaranteed a solution at this point
        candidate = 0
        running_sum = 0
        for i in range(len(gas)):
            running_sum += (gas[i] - cost[i])
            if running_sum < 0:
                running_sum = 0
                candidate = i + 1

        return candidate


if __name__ == "__main__":
    s = Solution()
    # Example from problem
    assert s.can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    # No valid starting point
    assert s.can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
    # Single station, enough gas
    assert s.can_complete_circuit([5], [4]) == 0
    # Single station, not enough gas
    assert s.can_complete_circuit([1], [2]) == -1
    # Start at last index
    assert s.can_complete_circuit([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]) == 4
    # All stations have exactly enough gas
    assert s.can_complete_circuit([1, 1, 1], [1, 1, 1]) == 0
    # Only last station has enough surplus
    assert s.can_complete_circuit([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == 2
    print("All tests passed.")