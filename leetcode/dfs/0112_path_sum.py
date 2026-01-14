class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def has_path_sum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Description:
        Given the root of a binary tree and an integer targetSum, return true 
        if the tree has a root-to-leaf path such that adding up all the values 
        along the path equals targetSum.

        Example:
        Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
        Output: true
        """
        
        if not root:
            return False
        
        stack = [(root, 0)]
        while stack:
            curr_node, accrued_sum = stack.pop()
            curr_sum = curr_node.val + accrued_sum

            if (not curr_node.left and not curr_node.right 
                and curr_sum == targetSum):
                return True
            
            if curr_node.left:
                stack.append((curr_node.left, curr_sum))
            if curr_node.right:
                stack.append((curr_node.right, curr_sum))
        
        return False


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.has_path_sum(
        TreeNode(5,
                 TreeNode(4,
                          TreeNode(11,
                                   TreeNode(7),
                                   TreeNode(2))),
                 TreeNode(8,
                          TreeNode(13),
                          TreeNode(4,
                                   None,
                                   TreeNode(1)))),
        22
    ) == True
    assert s.has_path_sum(
        TreeNode(1,
                 TreeNode(2),
                 TreeNode(3)),
        5
    ) == False
    assert s.has_path_sum(TreeNode(1), 1) == True
    assert s.has_path_sum(None, 0) == False
    print("All tests passed.")