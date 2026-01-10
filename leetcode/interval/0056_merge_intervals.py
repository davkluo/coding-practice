from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Description:
        Given an array of intervals represented as [start, end], merge all
        overlapping intervals and return an array of the non-overlapping 
        intervals.

        Example:
        merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
        """

        merged_intervals = []
        intervals_by_start = sorted(intervals)

        current_start = intervals_by_start[0][0]
        current_end = intervals_by_start[0][1]
        for start, end in intervals_by_start:
            # sorting intervals omits check if start >= current_start
            if start <= current_end:
                current_end = max(end, current_end)
            else: 
                merged_intervals.append([current_start, current_end])
                current_start = start
                current_end = end

        # add last interval
        merged_intervals.append([current_start, current_end])

        return merged_intervals


if __name__ == "__main__":
    s = Solution()
    assert s.merge([[1,3],[2,6],[8,10],[15,18]]) == [[1,6],[8,10],[15,18]]
    assert s.merge([[1,4],[4,5]]) == [[1,5]]
    assert s.merge([[4,7],[1,4]]) == [[1,7]]
    assert s.merge([[1,6]]) == [[1,6]]
    print("All tests passed.")