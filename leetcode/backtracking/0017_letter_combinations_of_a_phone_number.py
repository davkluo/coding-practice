from typing import List

class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        """
        Description:
        Given a string containing digits from 2-9 inclusive, return all possible 
        letter combinations that the number could represent based on the mapping 
        of digits to letters on a phone keypad. Return the answer in any order.

        Example:
        letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = []

        def dfs(i: int, substr: List[str]):
            if i == len(digits):
                combinations.append("".join(substr))
                return
            
            for c in mapping[digits[i]]:
                substr.append(c)
                dfs(i+1, substr)
                substr.pop()
        
        dfs(0, [])

        return combinations


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.letter_combinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert s.letter_combinations("2") == ["a","b","c"]
    print("All tests passed.")