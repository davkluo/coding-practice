from typing import List

class Solution:
    def generate_parentheses(self, n: int) -> List[str]:
        """
        Description:
        Given n pairs of parentheses, write a function to generate all 
        combinations of well-formed parentheses.

        Example:
        generate_parentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]
        """
        
        combinations = []

        def backtrack(curr, num_open):
            if len(curr) == 2 * n:
                combinations.append("".join(curr))
            
            num_closed = len(curr) - num_open
            if num_open < n:
                curr.append("(")
                backtrack(curr, num_open+1)
                curr.pop()
            
            if num_open > num_closed:
                curr.append(")")
                backtrack(curr, num_open)
                curr.pop()
        
        backtrack([], 0)

        return combinations


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.generate_parentheses(3) == ["((()))","(()())","(())()","()(())","()()()"]
    assert s.generate_parentheses(1) == ["()"]
    print("All tests passed.")