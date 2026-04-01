from classes import TreeNode
from testing import list_to_binary_tree

class Solution:
    def good_nodes(self, root: TreeNode) -> int:
        """
        Description:
        Given a binary tree root, return the number of good nodes in the tree.
        A node is good if the path from the root to the node does not contain
        any node with a value greater than the node.

        Example:
        Input: root = [3,1,4,3,null,1,5]
        Output: 4
        """
        
        num_good = 0

        def count_good(node: TreeNode, max_on_path: int) -> None:
            nonlocal num_good

            if not node:
                return
            
            if max_on_path <= node.val:
                num_good += 1
            
            count_good(node.left, max(node.val, max_on_path))
            count_good(node.right, max(node.val, max_on_path))

        count_good(root, float("-inf"))

        return num_good


if __name__ == "__main__":
    s = Solution()

    # [3,1,4,3,null,1,5] -> 4 (good: 3, 4, 3, 5)
    assert s.good_nodes(list_to_binary_tree([3, 1, 4, 3, None, 1, 5])) == 4

    # single node -> 1 (root is always good)
    assert s.good_nodes(list_to_binary_tree([1])) == 1

    # all same values -> all good
    assert s.good_nodes(list_to_binary_tree([1, 1, 1])) == 3

    # strictly decreasing -> only root is good
    assert s.good_nodes(list_to_binary_tree([3, 2, None, 1])) == 1

    # strictly increasing path -> all good
    assert s.good_nodes(list_to_binary_tree([1, 2, None, 3])) == 3

    # negative values: [-1,-2,-3] -> only root is good
    assert s.good_nodes(list_to_binary_tree([-1, -2, -3])) == 1

    print("All tests passed.")