from typing import List
from collections import defaultdict

class Solution:
    def find_order(self, num_courses: int, prerequisites: List[List[int]]
                   ) -> List[int]:
        """
        Description:
        Given the total number of courses and a list of prerequisite pairs,
        return an ordering of courses you should take to finish all courses.
        If it is impossible to finish all courses, return an empty array.

        Example:
        find_order(2, [[1,0]]) == [0,1]
        """

        graph = self.create_graph(prerequisites)
        confirmed = set()
        ordering = []
        checking = set()

        def dfs(course):
            if course in confirmed:
                return True
            elif course in checking:
                return False
            
            checking.add(course)

            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            
            checking.remove(course)
            confirmed.add(course)
            ordering.append(course)
            return True
        
        for course in range(num_courses):
            if not dfs(course):
                return []
        
        return ordering

    def create_graph(self, prerequisites: List[List[int]]
                     ) -> dict[int, List[int]]:
        graph = defaultdict(list)
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        return graph


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.find_order(2, [[1, 0]]) == [0, 1]
    assert (s.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3] 
            or s.find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3])
    assert s.find_order(1, []) == [0]
    assert s.find_order(2, [[0, 1], [1, 0]]) == []
    print("All tests passed.")