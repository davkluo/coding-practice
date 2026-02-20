from classes import TreeNode
from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return "[]"

        encoding = []
        queue = deque([root])

        while queue:
            level_has_children = False

            for _ in range(len(queue)):
                node = queue.popleft()

                if not node:
                    encoding.append("null")
                    continue

                encoding.append(str(node.val))

                left_child = node.left
                right_child = node.right
                queue.extend([left_child, right_child])

                if left_child or right_child:
                    level_has_children = True

            if not level_has_children:
                break

        return "[" + ",".join(encoding) + "]"
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        nodes = data[1:-1]
        if not nodes:
            return None
        
        nodes = nodes.split(",")      
        root = TreeNode(int(nodes[0]))

        if len(nodes) == 1:
            return root

        queue = deque([root])
        child_i = 1

        while queue:
            parent = queue.popleft()
            if not parent:
                continue

            # left child
            if child_i < len(nodes) and nodes[child_i] != "null":
                left_child = TreeNode(int(nodes[child_i]))
                parent.left = left_child
                queue.append(left_child)
            child_i += 1

            # right child
            if child_i < len(nodes) and nodes[child_i] != "null":
                right_child = TreeNode(int(nodes[child_i]))
                parent.right = right_child
                queue.append(right_child)
            child_i += 1

        return root            


if __name__ == "__main__":
    s = Codec()

    def same_tree(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and same_tree(p.left, q.left) and same_tree(p.right, q.right)

    def roundtrip(root):
        return s.deserialize(s.serialize(root))

    # Empty tree
    assert same_tree(roundtrip(None), None)

    # Single node
    assert same_tree(roundtrip(TreeNode(1)), TreeNode(1))

    # Complete binary tree: [1,2,3]
    assert same_tree(
        roundtrip(TreeNode(1, TreeNode(2), TreeNode(3))),
        TreeNode(1, TreeNode(2), TreeNode(3))
    )

    # LeetCode example: [1,2,3,null,null,4,5]
    tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
    assert same_tree(roundtrip(tree), tree)

    # Left-skewed: [1,2,null,3]
    left_skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert same_tree(roundtrip(left_skewed), left_skewed)

    # Right-skewed: [1,null,2,null,3]
    right_skewed = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert same_tree(roundtrip(right_skewed), right_skewed)

    # Left child only
    assert same_tree(roundtrip(TreeNode(1, TreeNode(2))), TreeNode(1, TreeNode(2)))

    # Right child only
    assert same_tree(roundtrip(TreeNode(1, None, TreeNode(2))), TreeNode(1, None, TreeNode(2)))

    # Negative values
    neg_tree = TreeNode(-1, TreeNode(-2), TreeNode(-3))
    assert same_tree(roundtrip(neg_tree), neg_tree)

    print("All tests passed.")