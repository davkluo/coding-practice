from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level_order(self, root: TreeNode) -> List[List[int]]:
        """
        Description:
        Given the root of a binary tree, return the level order traversal of its 
        nodes' values. (i.e., from left to right, level by level).

        Example:
        level_order([3,9,20,null,null,15,7]) -> [[3],[9,20],[15,7]]
        """
        
        if not root:
            return []

        traversal = []
        queue = deque([root])
        while queue:
            level_traversal = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level_traversal.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            traversal.append(level_traversal)

        return traversal


if __name__ == "__main__":
    s = Solution()
    assert s.level_order(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        ) == [[3], [9, 20], [15, 7]]
    assert s.level_order(None) == []
    assert s.level_order(TreeNode(1)) == [[1]]
    print("All tests passed.")