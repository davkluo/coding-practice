from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_symmetric(self, root: TreeNode) -> bool:
        """
        Description:
        Given the root of a binary tree, check whether it is a mirror of itself 
        (i.e., symmetric around its center).

        Example:
        Input: root = [1,2,2,3,4,4,3]
        Output: true
        """

        queue = deque([root])
        rev_queue = deque([root])

        while queue and rev_queue:
            curr = queue.popleft()
            rev_curr = rev_queue.popleft()

            if not curr and not rev_curr:
                continue
            elif not curr or not rev_curr: # one is None and the other isn't
                return False
            elif curr.val != rev_curr.val:
                return False
            
            queue.append(curr.left)
            queue.append(curr.right)

            # enqueue in reverse order
            rev_queue.append(rev_curr.right)
            rev_queue.append(rev_curr.left)
            
        return not queue and not rev_queue

    def is_symmetric_2(self, root: TreeNode) -> bool:
        def dfs(node_1, node_2):
            if not node_1 and not node_2:
                return True
            elif not node_1 or not node_2:
                return False
            
            return ((node_1.val == node_2.val) and 
                    dfs(node_1.left, node_2.right) and 
                    dfs(node_1.right, node_2.left))
    
        return dfs(root, root)


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [s.is_symmetric, s.is_symmetric_2]
    for func in funcs:
        assert func(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), 
                                   TreeNode(2, TreeNode(4), TreeNode(3)))) == True
        assert func(TreeNode(1, TreeNode(2, None, TreeNode(3)), 
                                   TreeNode(2, None, TreeNode(3)))) == False
        assert func(TreeNode(1)) == True
    print("All tests passed.")