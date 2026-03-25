class Solution:
    def _calculate(self, lhs: int, rhs: int, operator: str) -> int:
        if operator == "+":
            return lhs + rhs
        elif operator == "-":
            return lhs - rhs
        elif operator == "*":
            return lhs * rhs
        elif operator == "/":
            return lhs // rhs

    def calculate(self, s: str) -> int:
        """
        Description:
        Given a valid mathematical expression as a string, calculate and return
        the result, with integer division truncating towards zero.

        Example:
        calculate("3+2*2") == 7
        """
        
        numbers: list[int] = []
        operators: list[str] = []

        curr_number = ""

        for c in s:
            if c.isnumeric():
                curr_number += c
                continue

            if c == " ":
                continue

            # flush current number
            if operators and operators[-1] in "*/":
                lhs = numbers.pop()
                operator = operators.pop()
                numbers.append(self._calculate(lhs, int(curr_number), operator))
            else:
                numbers.append(int(curr_number))
            curr_number = ""

            operators.append(c)
        
        # handle multiplication and division at the end of the string
        if curr_number:
            if operators and operators[-1] in "*/":
                lhs = numbers.pop()
                operator = operators.pop()
                numbers.append(self._calculate(lhs, int(curr_number), operator))
            else:
                numbers.append(int(curr_number))

        # only + and - left        
        res = numbers[0]

        for i in range(len(operators)):
            res = self._calculate(res, numbers[i+1], operators[i])
        
        return res


if __name__ == "__main__":
    s = Solution()

    # Basic operations
    assert s.calculate("3+2*2") == 7
    assert s.calculate("3/2") == 1
    assert s.calculate("3+5 / 2") == 5

    # Single number
    assert s.calculate("42") == 42

    # All addition/subtraction (left-to-right)
    assert s.calculate("1+1+1") == 3
    assert s.calculate("10-3-2") == 5

    # All multiplication/division
    assert s.calculate("2*3*4") == 24
    assert s.calculate("100/10/2") == 5

    # Mixed precedence
    assert s.calculate("2+3*4-1") == 13
    assert s.calculate("10-2*3+4/2") == 6

    # Truncation toward zero for division
    assert s.calculate("7/2") == 3
    assert s.calculate("14/3/2") == 2

    # Spaces throughout
    assert s.calculate("  3 + 5  ") == 8
    assert s.calculate(" 2 * 3 + 4 / 2 ") == 8

    print("All tests passed.")