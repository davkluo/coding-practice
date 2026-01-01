class Solution:
    def is_valid(self, s: str) -> bool:
        """
        Description:
        Given a string containing only brackets and parentheses, determine
        if it is valid.

        Example:
        is_valid("()") == True
        """
        
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for bracket in s:
            if bracket in close_to_open: # Close bracket
                if not stack or close_to_open[bracket] != stack.pop():
                    return False
            else: # Open bracket
                stack.append(bracket)
        
        return len(stack) == 0


if __name__ == "__main__":
    s = Solution()
    assert s.is_valid("()") == True
    assert s.is_valid("()[]{}") == True
    assert s.is_valid("(]") == False
    assert s.is_valid("([)]") == False
    assert s.is_valid("{[]}") == True
    assert s.is_valid("") == True
    assert s.is_valid("[") == False
    assert s.is_valid("]") == False

    print("All tests passed.")
