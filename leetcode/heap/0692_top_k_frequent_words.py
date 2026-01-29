from typing import List
from collections import defaultdict
import heapq

# Custom comparator class to sort by increasing frequency and decreasing 
# alphabetical order
class Entry:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word


class Solution:
    def top_k_frequent(self, words: List[str], k: int) -> List[str]:
        """
        Description:
        Given an array of words and an integer k, return the k most frequent 
        words. The answer should be sorted by frequency from highest to lowest.
        If two words have the same frequency, then the word with the lower 
        alphabetical order comes first.

        Example:
        top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
            == ["i", "love"]
        """
        
        freqs = defaultdict(int)
        for word in words:
            freqs[word] += 1

        min_heap = []
        
        for word, freq in freqs.items():
            heapq.heappush(min_heap, Entry(freq, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap).word)

        return res[::-1]

if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
    assert s.top_k_frequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
    assert s.top_k_frequent(["a", "b", "c", "a", "b", "a"], 2) == ["a", "b"]
    assert s.top_k_frequent(["apple", "apple", "banana", "banana", "cherry", "cherry"], 2) == ["apple", "banana"]
    print("All tests passed.")