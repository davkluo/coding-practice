import heapq
from collections import defaultdict

class Solution:
    def network_delay_time(self, times: list[list[int]], n: int, k: int) -> int:
        """
        Description:
        Given a network of n nodes labeled from 1 to n, and a list of travel
        times as directed edges where times[i] = (u, v, w) represents the time
        it takes for a signal to travel from node u to node v, determine the
        time it takes for all nodes to receive the signal starting from node k.
        If it is not possible for all the nodes to receive the signal, return -1.

        Example:
        Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
        Output: 2
        """

        edges = defaultdict(list)
        for (src, dst, weight) in times:
            edges[src].append((dst, weight))

        dist_from_k = { i: float("inf") for i in range(1, n + 1)}
        dist_from_k[k] = 0
        processed = set()

        queue = [(0, k)]

        while queue:
            dist, node = heapq.heappop(queue)
            if node in processed:
                continue

            processed.add(node)

            for neighbor, weight in edges[node]:
                dist_to_neighbor = dist + weight
                if dist_to_neighbor < dist_from_k[neighbor]:
                    dist_from_k[neighbor] = dist_to_neighbor
                    heapq.heappush(queue, (dist_to_neighbor, neighbor))       

        longest_dist = max(dist_from_k.values())

        return longest_dist if longest_dist != float("inf") else -1         


if __name__ == "__main__":
    s = Solution()

    # Example case
    assert s.network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2

    # Single node — signal is already there
    assert s.network_delay_time([], 1, 1) == 0

    # Unreachable node
    assert s.network_delay_time([[1, 2, 1]], 3, 1) == -1

    # All nodes directly connected from source
    assert s.network_delay_time([[1, 2, 3], [1, 3, 5], [1, 4, 1]], 4, 1) == 5

    # Shorter path through intermediate node
    assert s.network_delay_time([[1, 2, 10], [1, 3, 1], [3, 2, 1]], 3, 1) == 2

    # Linear chain
    assert s.network_delay_time([[1, 2, 1], [2, 3, 2], [3, 4, 3]], 4, 1) == 6

    # Multiple paths, pick shortest
    assert s.network_delay_time([[1, 2, 1], [1, 3, 4], [2, 3, 2]], 3, 1) == 3

    print("All tests passed.")