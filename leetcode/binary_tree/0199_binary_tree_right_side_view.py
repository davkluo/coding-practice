from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def right_side_view(self, root: TreeNode) -> list[int]:
        """
        Description:
        Given the root of a binary tree, imagine yourself standing on the right 
        side of it, return the values of the nodes you can see ordered from top 
        to bottom.

        Example:
        """
        
        if not root:
            return []

        right_view = []
        queue = deque([root])

        while queue:
            nodes_in_level = len(queue)
            for i in range(nodes_in_level):
                curr = queue.popleft()

                if i == nodes_in_level - 1:
                    right_view.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        
        return right_view
    
    def right_side_view_2(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        
        right_view = []

        def dfs(node, depth):
            if depth > len(right_view):
                right_view.append(node.val)
            
            if node.right:
                dfs(node.right, depth + 1)
            if node.left:
                dfs(node.left, depth + 1)
        
        dfs(root, 1)
        return right_view


if __name__ == "__main__":
    s = Solution()
    # test cases
    funcs = [s.right_side_view, s.right_side_view_2]
    for func in funcs:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        assert func(root) == [1, 3, 5]

        # test case 2
        root = TreeNode(1)
        root.right = TreeNode(3)
        assert func(root) == [1, 3]

        assert func(None) == []

    print("All tests passed.")