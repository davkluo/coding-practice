from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], 
               newInterval: List[int]) -> List[List[int]]:
        """
        Description:
        Given an array of non-overlapping intervals sorted by start time, 
        insert a new interval into the intervals (merge if necessary to maintain
        non-overlapping property).

        Example:
        insert([[1,3],[6,9]], [2,5]) -> [[1,5],[6,9]]
        """
        
        if not intervals:
            return [newInterval]

        new_intervals = []
        is_merged = False

        i = 0
        while i < len(intervals):
            start, end = intervals[i]
            if end < newInterval[0]: # before merge
                new_intervals.append([start, end])
            elif start > newInterval[1]: # after merge
                if not is_merged: # check if we need to close merge
                    new_intervals.append(newInterval)
                    is_merged = True
                new_intervals.append([start, end])
            else: # merging
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])

            i += 1

        if not is_merged:
            new_intervals.append(newInterval)

        return new_intervals                

if __name__ == "__main__":
    s = Solution()
    assert s.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert s.insert([], [5,7]) == [[5,7]]
    assert s.insert([[1,5]], [2,3]) == [[1,5]]
    assert s.insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert s.insert([[1,5],[6,9]], [0,10]) == [[0,10]]
    print("All tests passed.")