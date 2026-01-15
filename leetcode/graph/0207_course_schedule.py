from typing import List
from collections import defaultdict

class Solution:
    def can_finish_dfs(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        Description:
        Given courses labeled from 0 to num_courses-1 and a list of prerequisite 
        pairs, determine if it is possible to finish all courses.

        Example:
        can_finish(2, [[1, 0]]) == True
        """

        graph = self.create_graph(prerequisites)
        confirmed = set() # courses confirmed to be possible
        visiting = set() # currently visiting on dfs path

        def dfs(course: int) -> bool:
            """ Cycle detection """

            if course in confirmed:
                return True
            elif course in visiting: # cycle detected
                return False
            
            visiting.add(course)
            
            for neighbor in graph[course]:
                if not dfs(neighbor): # cycle detected later, propagate up
                    return False
            
            # no cycles detected
            confirmed.add(course)
            visiting.remove(course)
            return True

        for course in range(num_courses):
            if not dfs(course):
                return False
        
        return True


    def can_finish_bfs(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        pass

    def can_finish_topo(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        pass

    def create_graph(self, prerequisites: List[List[int]]) -> dict[int, List[int]]:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        return graph
        

if __name__ == "__main__":
    s = Solution()
    # test cases
    functions = [
        s.can_finish_dfs,
        # s.can_finish_bfs,
        # s.can_finish_topo
    ]
    for func in functions:
        assert func(2, [[1, 0]]) == True
        assert func(2, [[1, 0], [0, 1]]) == False
        assert func(3, [[0, 1], [1, 2], [2, 0]]) == False
        assert func(4, [[0, 1], [1, 2], [2, 3]]) == True
        assert func(1, []) == True
    print("All tests passed.")