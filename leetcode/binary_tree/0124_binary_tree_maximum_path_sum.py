from classes import TreeNode

class Solution:
    def max_path_sum(self, root: TreeNode) -> int:
        """
        Description:
        Given the root of a binary tree, return the maximum path sum of any
        path and return it. The path must contain at least one node.

        Example:
        Input: root = [1,2,3]
        Output: 6
        """

        max_sum = float("-inf")

        def _max_path_sum(node: TreeNode) -> None:
            nonlocal max_sum

            left_max_sum, right_max_sum = float("-inf"), float("-inf")

            if node.left:
                left_max_sum = _max_path_sum(node.left)
            
            if node.right:
                right_max_sum = _max_path_sum(node.right)
            
            # every possible path combination of current node, left, and right
            max_sum = max(
                node.val, 
                left_max_sum + node.val,
                right_max_sum + node.val,
                left_max_sum + node.val + right_max_sum,
                max_sum
            )

            # must have node.val to connect to above path
            # can't have both left and right subtrees AND connect to above
            return max(
                node.val,
                node.val + left_max_sum,
                node.val + right_max_sum
            )
        
        _max_path_sum(root)

        return max_sum


if __name__ == "__main__":
    s = Solution()

    # Single node
    assert s.max_path_sum(TreeNode(5)) == 5

    # All negative — must pick the least negative node
    assert s.max_path_sum(TreeNode(-3)) == -3
    assert s.max_path_sum(TreeNode(-1, TreeNode(-2), TreeNode(-3))) == -1

    # Basic path through root: 2 -> 1 -> 3 = 6
    assert s.max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6

    # Path doesn't go through root
    #       -10
    #       /  \
    #      9   20
    #         /  \
    #        15   7
    # Best path: 15 -> 20 -> 7 = 42
    assert s.max_path_sum(TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))) == 42

    # Negative branch should be ignored: 5 -> 4 = 9
    assert s.max_path_sum(TreeNode(5, TreeNode(-2), TreeNode(4))) == 9

    # Left-skewed: best straight path 3 -> 2 -> 1 = 6
    assert s.max_path_sum(TreeNode(1, TreeNode(2, None, TreeNode(3)))) == 6

    print("All tests passed.")