from typing import Optional

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def clone_graph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Description:
        Given a reference of a node in a connected undirected graph, return a
        deep copy of the graph. Each node in the graph contains a value (int) 
        and a list (List[Node]) of its neighbors. Each node's index is the same
        as its value. The given node will always be the first node with val = 1.
        The return must be a copy of the given node.

        Example:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        """
        
        if not node:
            return None
        
        node_clones = {}
        stack = [node]

        while stack:
            current = stack.pop()

            # never seen as neighbor of another node
            if current not in node_clones:
                node_clones[current] = Node(current.val)

            neighbor_clones = []
            for neighbor in current.neighbors:
                # add neighbor to stack only on first encounter
                if neighbor not in node_clones:
                    node_clones[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                neighbor_clones.append(node_clones[neighbor])
            
            node_clones[current].neighbors = neighbor_clones

        return node_clones[node]

if __name__ == "__main__":
    s = Solution()
    assert s.clone_graph(None) is None
    assert s.clone_graph(Node(1, [Node(2), Node(3)])) is not None
    print("All tests passed.")
