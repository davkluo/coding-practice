from typing import List
import math

class Solution:
    def eval_rpn(self, tokens: List[str]) -> int:
        """
        Description:
        Given an array of string tokens representing an arithmetic expression in
        Reverse Polish Notation, evaluate the expression and return the result.
        Division should truncate towards zero.

        Example:
        eval_rpn(["2", "1", "+", "3", "*"]) == 9
        """
        
        stack = []
        
        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()

                interm_result = None
                if token == "+":
                    interm_result = num_1 + num_2
                elif token == "-":
                    interm_result = num_1 - num_2
                elif token == "*":
                    interm_result = num_1 * num_2
                elif token == "/":
                    interm_result = math.trunc(num_1 / num_2)
                stack.append(interm_result)

        return stack.pop()

if __name__ == "__main__":
    s = Solution()
    assert s.eval_rpn(["6"]) == 6
    assert s.eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert s.eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert s.eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", 
                       "*", "17", "+", "5", "+"]) == 22
    assert s.eval_rpn(["1", "0", "*"]) == 0
    assert s.eval_rpn(["-10", "5", "+"]) == -5
    print("All tests passed.")