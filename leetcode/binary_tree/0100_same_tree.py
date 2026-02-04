class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_same_tree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Description:
        Given the roots of two binary trees p and q, write a function to check 
        if they are the same or not. Two binary trees are considered the same 
        if they are structurally identical, and the nodes have the same value.

        Example:
        Input: p = [1,2,3], q = [1,2,3]
        Output: true
        """
        
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.is_same_tree(p.left, q.left) and 
                self.is_same_tree(p.right, q.right))


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.is_same_tree(
        TreeNode(1, TreeNode(2), TreeNode(3)),
        TreeNode(1, TreeNode(2), TreeNode(3))
    ) == True
    assert s.is_same_tree(
        TreeNode(1, TreeNode(2)),
        TreeNode(1, None, TreeNode(2))
    ) == False
    assert s.is_same_tree(
        TreeNode(1, TreeNode(2), TreeNode(1)),
        TreeNode(1, TreeNode(1), TreeNode(2))
    ) == False
    assert s.is_same_tree(
        None, None) == True
    assert s.is_same_tree(
        TreeNode(1), None) == False
    print("All tests passed.")