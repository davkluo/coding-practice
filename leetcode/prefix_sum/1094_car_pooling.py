class Solution:
    def car_pooling(self, trips: list[list[int]], capacity: int) -> bool:
        """
        Description:
        Given a list of trips containing the number of passengers, a starting
        location, and a destination, determine if it is possible to pick up and
        drop off all passengers without exceeding the vehicle's capacity at any
        point in time. The vehicle only travels in one direction.

        0 <= location <= 1000

        Example:
        car_pooling([[2, 1, 5], [3, 3, 7]], 4) == False
        """
        
        deltas = [0] * 1001 # location can only be between [0, 1000]

        for (num_passengers, src, dst) in trips:
            deltas[src] -= num_passengers # reduce capacity on board
            deltas[dst] += num_passengers # increase capacity on unload

        for change in deltas:
            if capacity + change < 0:
                return False
            
            capacity += change
        
        return True


if __name__ == "__main__":
    s = Solution()
    # test cases
    # from leetcode problem description
    assert s.car_pooling([[2, 1, 5], [3, 3, 7]], 4) == False
    assert s.car_pooling([[2, 1, 5], [3, 3, 7]], 5) == True
    # single trip, exactly at capacity
    assert s.car_pooling([[5, 0, 10]], 5) == True
    # single trip, over capacity
    assert s.car_pooling([[6, 0, 10]], 5) == False
    # passengers drop off before next batch boards at same stop
    assert s.car_pooling([[3, 0, 5], [3, 5, 10]], 3) == True
    # trips unsorted by start location
    assert s.car_pooling([[3, 3, 7], [2, 1, 5]], 4) == False
    # non-overlapping trips, capacity never exceeded
    assert s.car_pooling([[2, 0, 3], [3, 5, 9]], 3) == True
    # all trips overlap fully
    assert s.car_pooling([[2, 0, 10], [2, 0, 10], [2, 0, 10]], 5) == False
    # single passenger, single trip
    assert s.car_pooling([[1, 0, 1]], 1) == True
    print("All tests passed.")