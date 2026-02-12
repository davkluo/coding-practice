from classes import Trie, TrieNode
from testing import compare_lists

class Solution:
    def find_words(self, board: list[list[str]], words: list[str]) -> list[str]:
        """
        Description:
        Given an m x n board of characters and a list of strings words, return 
        all words on the board. Each word must be constructed from letters of 
        sequentially adjacent cells, where adjacent cells are horizontally or 
        vertically neighboring. The same letter cell may not be used more than 
        once in a word.

        Example:
        find_words([["o","a","a","n"],
                    ["e","t","a","e"],
                    ["i","h","k","r"],
                    ["i","f","l","v"]],
                   ["oath","pea","eat","rain"]) == ["eat","oath"]
        """
        
        max_word_len = 0
        word_set = set()
        found_words = set()

        for word in words:
            word_set.add(word)
            max_word_len = max(len(word), max_word_len)

        def backtrack(i: int, j: int, substr: list[str], seen: set):
            candidate = "".join(substr)
            if candidate in word_set:
                found_words.add(candidate)
            
            if len(substr) == max_word_len:
                return
            
            adjacent = [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]
            for r, c in adjacent:
                if (0 <= r < len(board) and 0 <= c < len(board[0])
                    and (r, c) not in seen):
                    seen.add((r, c))
                    substr.append(board[r][c])
                    backtrack(r, c, substr, seen)
                    substr.pop()
                    seen.discard((r, c))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, [board[i][j]], set([(i, j)]))

        return list(found_words)
    
    def find_words_trie(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Trie()

        for word in words:
            trie.insert(word)

        found_words = []

        def backtrack(curr: TrieNode, i: int, j: int, 
                      substr: list[str], seen: set[tuple[int, int]]):

            if len(found_words) == len(words): # terminate early if all found
                return            
            if curr.is_end_of_word:
                found_words.append("".join(substr))
                curr.is_end_of_word = False # prevent duplicates of this word

            adjacent = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for r, c in adjacent:
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]): continue
                if (r, c) in seen: continue

                adjacent_char = board[r][c]
                if adjacent_char not in curr.children: continue

                seen.add((r, c))
                substr.append(board[r][c])
                backtrack(curr.children[adjacent_char], r, c, substr, seen)
                substr.pop()
                seen.discard((r, c))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                char = board[i][j]
                if char in trie.root.children:
                    backtrack(trie.root.children[char], i, j, [char], set([(i, j)]))

        return found_words
            

if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [s.find_words_trie]
    for func in funcs:
        assert compare_lists(func([["o","a","a","n"],
                            ["e","t","a","e"],
                            ["i","h","k","r"],
                            ["i","f","l","v"]],
                            ["oath","pea","eat","rain"]), ["eat","oath"])
        assert compare_lists(func([["a","b"],
                            ["c","d"]],
                            ["abcb"]), [])
        assert compare_lists(func([["a", "a"]], ["aaa"]), [])
    print("All tests passed.")