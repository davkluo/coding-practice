from collections import deque

class Solution:
    def is_bipartite(self, graph: list[list[int]]) -> bool:
        """
        Description:
        Given a graph of n nodes labelled from 0 to n - 1, and a list of 
        undirected edges, determine if it is a bipartite graph.

        The graph is given in the form of an adjacency list, where graph[u] is a
        list of nodes that are adjacent to node u. The graph has the following
        properties:
        - There are no self edges (graph[u] does not contain u).
        - There are no parallel edges (graph[u] does not contain duplicate 
            values).
        - If v is in graph[u], then u is in graph[v] (the graph is undirected).
        - The graph may not be connected, meaning there may be isolated nodes.

        Example:
        is_bipartite([[1,3], [0,2], [1,3], [0,2]]) == True
        """
        
        assignments = [0] * len(graph)
        processed = set()

        def bfs(node: int) -> bool:
            queue = deque([node])

            while queue:
                curr = queue.popleft()
                if curr in processed:
                    continue
                processed.add(curr)

                if not assignments[curr]:
                    assignments[curr] = 1

                opp_assignment = 2 if assignments[curr] == 1 else 1
                for neighbor in graph[curr]:
                    if not assignments[neighbor]:
                        assignments[neighbor] = opp_assignment
                    elif assignments[neighbor] == assignments[curr]:
                        return False
                    
                    queue.append(neighbor)

            return True
    
        for node in range(len(graph)):
            if not bfs(node):
                return False
        
        return True


if __name__ == "__main__":
    s = Solution()

    # Example from problem: bipartite (two-colorable even cycle)
    assert s.is_bipartite([[1, 3], [0, 2], [1, 3], [0, 2]]) == True

    # Odd cycle (triangle): not bipartite
    assert s.is_bipartite([[1, 2], [0, 2], [0, 1]]) == False

    # Single node, no edges: bipartite
    assert s.is_bipartite([[]]) == True

    # Two disconnected nodes: bipartite
    assert s.is_bipartite([[], []]) == True

    # Two connected nodes: bipartite
    assert s.is_bipartite([[1], [0]]) == True

    # Disconnected graph: one component is odd cycle
    # Nodes 0-1-2 form a triangle; node 3 is isolated
    assert s.is_bipartite([[1, 2], [0, 2], [0, 1], []]) == False

    # Disconnected graph: both components are bipartite
    # 0-1 and 2-3 are separate edges
    assert s.is_bipartite([[1], [0], [3], [2]]) == True

    # Even cycle of length 6: bipartite
    assert s.is_bipartite([[1, 5], [0, 2], [1, 3], [2, 4], [3, 5], [4, 0]]) == True

    # Odd cycle of length 5: not bipartite
    assert s.is_bipartite([[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]]) == False

    # Star graph (one center connected to all): bipartite
    assert s.is_bipartite([[1, 2, 3], [0], [0], [0]]) == True

    assert s.is_bipartite([[1],[0,3],[3],[1,2]]) == True

    print("All tests passed.")