import math

class Solution:
    def min_eating_speed(self, piles: list[int], h: int) -> int:
        """
        Description:
        Given a list of banana pile sizes and an integer h representing the
        number of hours Koko has to eat all the bananas, return the minimum
        speed (bananas per hour) such that Koko can eat all the bananas within 
        h hours. Koko can only eat from one pile per hour, and h is guaranteed
        to be at least the number of piles.

        Example:
        min_eating_speed([3, 6, 7, 11], 8) == 4
        """

        def is_valid_speed(k):
            time_required = 0
            for pile in piles:
                time_required += math.ceil(pile / k)
                if time_required > h:
                    return False
            return True        
        
        l, r = 1, max(piles) # range of possible values for k (eating speed)

        while l < r:
            m = (l + r) // 2
            
            if is_valid_speed(m):
                r = m # m is in range of possible answers, try slower speeds
            else:
                l = m + 1 # m is not a valid answer

        return l            


if __name__ == "__main__":
    s = Solution()
    # test cases

    # every pile is the same size, h equals number of piles
    assert s.min_eating_speed([5, 5, 5], 3) == 5

    # example from problem
    assert s.min_eating_speed([3, 6, 7, 11], 8) == 4

    # h is much larger than piles, speed of 1 is sufficient
    assert s.min_eating_speed([1, 1, 1], 100) == 1

    # single pile, must finish in exactly h hours
    assert s.min_eating_speed([10], 1) == 10
    assert s.min_eating_speed([10], 10) == 1

    # one very large pile among small ones
    assert s.min_eating_speed([1, 1, 1, 1000000000], 4) == 1000000000

    # h equals number of piles (tightest constraint)
    assert s.min_eating_speed([30, 11, 23, 4, 20], 5) == 30

    # h is slightly more than number of piles
    assert s.min_eating_speed([30, 11, 23, 4, 20], 6) == 23

    print("All tests passed.")