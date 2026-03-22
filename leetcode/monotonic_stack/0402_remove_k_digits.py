class Solution:
    def remove_K_digits(self, num: str, k: int) -> str:
        """
        Remove k digits from the number num to make it the smallest possible.
        Leading zeros should be removed from the result. If the result is an 
        empty string, return "0".

        Example:
        remove_K_digits("1432219", 3) == "1219"
        """
        
        stack = [] # monotonically non-decreasing

        for digit in num:
            while stack and stack[-1] > digit and k > 0:
                stack.pop()
                k -= 1

            stack.append(digit)
        
        # remove from end until k
        while k > 0:
            stack.pop()
            k -= 1
        
        result = "".join(stack)
        result = result.lstrip("0")

        return result if result else "0"


if __name__ == "__main__":
    s = Solution()

    # basic
    assert s.remove_K_digits("1432219", 3) == "1219"  # docstring example

    # non-decreasing — remove from the end
    assert s.remove_K_digits("12345", 3) == "12"
    assert s.remove_K_digits("1111", 2) == "11"

    # leading zeros
    assert s.remove_K_digits("10200", 1) == "200"   # remove 1 → "0200" → strip

    # k = 0 — nothing removed
    assert s.remove_K_digits("9", 0) == "9"

    # k = len(num) — everything removed
    assert s.remove_K_digits("9", 1) == "0"
    assert s.remove_K_digits("10", 2) == "0"

    # single drop at the start
    assert s.remove_K_digits("21", 1) == "1"

    # drop produces leading zero
    assert s.remove_K_digits("100", 1) == "0"      # remove 1 → "00" → "0"... check your stripping

    print("All tests passed.")