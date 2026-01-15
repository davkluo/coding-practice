from typing import List
from collections import defaultdict, deque

class Solution:
    def can_finish_dfs(self, num_courses: int, prerequisites: List[List[int]]
                       ) -> bool:
        """
        Description:
        Given courses labeled from 0 to num_courses-1 and a list of prerequisite 
        pairs, determine if it is possible to finish all courses.

        Example:
        can_finish(2, [[1, 0]]) == True
        """

        graph = self.create_graph(prerequisites)
        confirmed = set() # courses confirmed to be possible
        checking = set() # currently visiting on dfs path

        def dfs(course: int) -> bool:
            """ Cycle detection """

            if course in confirmed:
                return True
            elif course in checking: # cycle detected
                return False
            
            checking.add(course)
            
            for prereq in graph[course]:
                if not dfs(prereq): # cycle detected later, propagate up
                    return False
            
            # no cycles detected
            confirmed.add(course)
            checking.remove(course)
            return True

        for course in range(num_courses):
            if not dfs(course):
                return False
        
        return True


    def can_finish_bfs(self, num_courses: int, prerequisites: List[List[int]]
                       ) -> bool:
        graph = self.create_graph(prerequisites)
        graph_r = self.create_reverse_graph(prerequisites)
        indegrees = [0] * num_courses
        num_completed = 0

        for course in graph:
            indegrees[course] = len(graph[course])

        queue = deque()
        for course in range(len(indegrees)):
            if indegrees[course] == 0:
                queue.append(course)
                num_completed += 1

        while queue:
            course = queue.popleft()
            for dependent in graph_r[course]:
                indegrees[dependent] -= 1
                if indegrees[dependent] == 0:
                    queue.append(dependent)
                    num_completed += 1
        
        return num_completed == num_courses
            

    def can_finish_topo(self, num_courses: int, prerequisites: List[List[int]]
                        ) -> bool:
        pass

    def create_graph(self, prerequisites: List[List[int]]
                     ) -> dict[int, List[int]]:
        graph = defaultdict(list)

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        return graph
    
    def create_reverse_graph(self, prerequisites: List[List[int]]
                             ) -> dict[int, List[int]]:
        reverse_graph = defaultdict(list)

        for course, prereq in prerequisites:
            reverse_graph[prereq].append(course)
        
        return reverse_graph
        
        

if __name__ == "__main__":
    s = Solution()
    # test cases
    functions = [
        s.can_finish_dfs,
        s.can_finish_bfs,
        # s.can_finish_topo
    ]
    for func in functions:
        assert func(2, [[1, 0]]) == True
        assert func(2, [[1, 0], [0, 1]]) == False
        assert func(3, [[0, 1], [1, 2], [2, 0]]) == False
        assert func(4, [[0, 1], [1, 2], [2, 3]]) == True
        assert func(1, []) == True
    print("All tests passed.")