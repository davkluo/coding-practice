from typing import List

class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        Description:
        Given an integer array coins representing coins of different 
        denominations and an integer amount representing a total amount of 
        money, return the fewest number of coins that you need to make up that 
        amount. If that amount of money cannot be made up by any combination of 
        the coins, return -1.

        Example:
        coin_change([1, 2, 5], 11) == 3
        """
        
        coins_needed = [0] # base case: 0 coins to make up a sum of 0
        coins_needed += [float("inf")] * amount

        for i in range(1, amount+1):
            for coin in coins:
                if i >= coin:
                    coins_needed[i] = min(1 + coins_needed[i-coin], 
                                          coins_needed[i])
            
        return coins_needed[-1] if coins_needed[-1] != float("inf") else -1


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.coin_change([1, 2, 5], 11) == 3
    assert s.coin_change([2], 3) == -1
    assert s.coin_change([1], 0) == 0
    assert s.coin_change([1], 1) == 1
    assert s.coin_change([1], 2) == 2
    print("All tests passed.")