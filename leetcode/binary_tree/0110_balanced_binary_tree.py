from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_balanced(self, root: Optional[TreeNode]) -> bool:
        """
        Description:
        Given a binary tree, determine if it is height-balanced. This means that
        for every node in the tree, the height difference between its left and 
        right subtrees is at most 1.

        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: True
        """
        
        def dfs(root: Optional[TreeNode]) -> tuple[bool, int]:
            """ Returns whether a tree is height balanced and its height """

            if not root:
                return (True, 0)
            
            left_height = 0
            right_height = 0

            if root.left:
                is_left_balanced, left_height = dfs(root.left)
                if not is_left_balanced:
                    return (False, 0)
            
            if root.right:
                is_right_balanced, right_height = dfs(root.right)
                if not is_right_balanced:
                    return (False, 0)
            
            is_balanced = abs(left_height - right_height) <= 1
            return (is_balanced, max(left_height, right_height) + 1)
    
        is_root_balanced, _tree_height = dfs(root)
        return is_root_balanced


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.is_balanced(
        TreeNode(3, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15), 
                          TreeNode(7))
                )
    ) == True
    assert s.is_balanced(
        TreeNode(1, 
                 TreeNode(2, 
                          TreeNode(3, 
                                   TreeNode(4), 
                                   TreeNode(4)
                                  ), 
                          TreeNode(3)
                         ), 
                 TreeNode(2)
                )
    ) == False
    assert s.is_balanced(None) == True
    print("All tests passed.")