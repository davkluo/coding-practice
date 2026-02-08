class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        """
        Description:
        Given the root of a binary tree, return the length of the diameter of 
        the tree. The diameter of a binary tree is the length of the longest 
        path between any two nodes in the tree. This path may or may not pass 
        through the root.

        Example:
        Input: root = [1,2,3,4,5]
        Output: 3 (the path is 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
        """
        
        diameter = 0

        def dfs(root: TreeNode) -> int:
            """ Updates diameter and returns height of subtree """
            nonlocal diameter

            if not root:
                return 0
            
            left_h = dfs(root.left)
            right_h = dfs(root.right)
            d = left_h + right_h
            diameter = max(d, diameter)

            return 1 + max(left_h, right_h)

        dfs(root)

        return diameter
            

if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.diameter_of_binary_tree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))) == 3
    assert s.diameter_of_binary_tree(TreeNode(1)) == 0
    assert s.diameter_of_binary_tree(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    print("All tests passed.")