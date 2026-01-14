class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invert_tree(self, root: TreeNode) -> TreeNode:
        """
        Description:
        Given the root of a binary tree, invert the tree, and return its root.

        Example:
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
        """
        
        if not root:
            return None
        
        stack = [root]
        while stack:
            curr_node = stack.pop()
            curr_node.left, curr_node.right = curr_node.right, curr_node.left

            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
        
        return root


if __name__ == "__main__":
    s = Solution()
    # helpers for tests: build tree from level-order list and serialize back
    from collections import deque

    def build_tree(vals):
        if not vals:
            return None
        it = iter(vals)
        root = TreeNode(next(it))
        q = deque([root])
        for v in it:
            node = q.popleft()
            if v is not None:
                node.left = TreeNode(v)
                q.append(node.left)
            try:
                v = next(it)
            except StopIteration:
                break
            if v is not None:
                node.right = TreeNode(v)
                q.append(node.right)
        return root

    def tree_to_list(root):
        if not root:
            return []
        q = deque([root])
        out = []
        while q:
            node = q.popleft()
            if node:
                out.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                out.append(None)
        # trim trailing Nones
        while out and out[-1] is None:
            out.pop()
        return out

    # test cases compare values/structure, not object references
    cases = [
        ([], []),
        ([1], [1]),
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([1,2,None,3], [1,None,2,None,3]),
    ]

    for inp, expected in cases:
        root = build_tree(inp)
        res = s.invert_tree(root)
        assert tree_to_list(res) == expected, f"Failed for {inp}: got {tree_to_list(res)}, expected {expected}"

    print("All tests passed.")