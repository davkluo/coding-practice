class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """
        Description:
        Given a list of daily temperatures, return a list mapping each day to
        the number of days until a warmer temperature. If there is no future
        day with a warmer temperature, put 0 instead.

        Example:
        daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
        """
        
        days_til_warmer_temp = [0] * len(temperatures)
        stack = [] # tuples of (day, temperature)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_day, _prev_temp = stack.pop()
                days_til_warmer_temp[prev_day] = i - prev_day     

            stack.append((i, temp))

        return days_til_warmer_temp       


if __name__ == "__main__":
    s = Solution()

    # Basic example from problem
    assert s.daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Strictly decreasing — all zeros
    assert s.daily_temperatures([90, 80, 70, 60]) == [0, 0, 0, 0]

    # Strictly increasing — each day waits 1
    assert s.daily_temperatures([60, 70, 80, 90]) == [1, 1, 1, 0]

    # Single element
    assert s.daily_temperatures([50]) == [0]

    # All same temperature — no warmer day
    assert s.daily_temperatures([70, 70, 70]) == [0, 0, 0]

    # Warmer day is far away
    assert s.daily_temperatures([30, 29, 28, 31]) == [3, 2, 1, 0]

    # Last element always 0
    assert s.daily_temperatures([70, 71]) == [1, 0]

    print("All tests passed.")