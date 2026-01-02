from typing import List

class Solution:
    def max_profit(self, prices: List[int]) -> int:
        """
        Description:
        Given an array of prices representing stock price on a given day,
        determine the maximum profit from buying on one day and selling on a
        different future date. If no positive profit is possible return 0.

        Example:
        max_profit([7, 1, 5, 3, 6, 4]) == 5
        """
        
        if len(prices) <= 1:
            return 0

        min_price = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            profit = prices[i] - min_price
            max_profit = max(profit, max_profit)
            min_price = min(prices[i], min_price)
        
        return max_profit
    

if __name__ == "__main__":
    s = Solution()
    assert s.max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert s.max_profit([7, 6, 4, 3, 1]) == 0
    assert s.max_profit([1]) == 0
    assert s.max_profit([2, 2]) == 0
    print("All test cases pass")
