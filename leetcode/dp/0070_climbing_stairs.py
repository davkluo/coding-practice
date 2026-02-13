class Solution:
    def climb_stairs(self, n: int) -> int:
        """
        Description:
        There are n steps to climb. Each time you can either climb 1 or 2 steps. 
        In how many distinct ways can you climb to the top?

        Example:
        climb_stairs(2) == 2
        """
        
        two_steps_prior = 0 # 0 ways to start at step -1
        one_step_prior = 1 # 1 way to start at step 0

        # technically from step 1 to n but only number of loops matters
        for _ in range(n):
            num_ways = two_steps_prior + one_step_prior
            two_steps_prior = one_step_prior
            one_step_prior = num_ways
        
        return one_step_prior


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.climb_stairs(2) == 2
    assert s.climb_stairs(3) == 3
    assert s.climb_stairs(4) == 5
    assert s.climb_stairs(5) == 8
    print("All tests passed.")