from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        """
        Description:
        Given the root of a binary tree, return its maximum depth.
        A binary tree's maximum depth is the number of nodes along the longest 
        path from the root node down to the farthest leaf node.

        Example:
        max_depth([3,9,20,null,null,15,7]) -> 3
        """
        
        if not root:
            return 0

        left_depth, right_depth = 0, 0        
        if root.left:
            left_depth = self.max_depth(root.left)
        if root.right:
            right_depth = self.max_depth(root.right)
        
        return max(left_depth, right_depth) + 1

    def max_depth_stack(self, root: Optional[TreeNode]) -> int:
        """ Non-recursive alternative """
        if not root:
            return 0
        
        max_depth = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()

            max_depth = max(depth, max_depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth


if __name__ == "__main__":
    s = Solution()
    assert s.max_depth(
        TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        ) == 3
    assert s.max_depth(None) == 0
    assert s.max_depth(TreeNode(1)) == 1
    assert s.max_depth(
        TreeNode(1, None, TreeNode(2))
        ) == 2
    print("All tests passed.")