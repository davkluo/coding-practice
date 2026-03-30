from typing import Optional
from classes import TreeNode
from testing.utils import list_to_binary_tree, compare_trees

class Solution:
    def build_tree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        Description:
        Given the preorder and inorder traversal of a binary tree, reconstruct
        the binary tree and return it. All values in the traversals are unique.

        Example:
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]
        """
        
        val_to_inorder_idx = {val: idx for idx, val in enumerate(inorder)}

        def _build_tree(preorder_range: tuple[int, int], inorder_range: tuple[int, int]) -> Optional[TreeNode]:
            pre_l, pre_r = preorder_range
            in_l, in_r = inorder_range

            if pre_l > pre_r or in_l > in_r:
                return None
            
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            inorder_idx = val_to_inorder_idx[root_val]

            l_subtree_size = inorder_idx - in_l
                                             
            l_child_preorder_range = (pre_l + 1, pre_l + l_subtree_size)
            r_child_preorder_range = (l_child_preorder_range[1] + 1, pre_r)

            l_child_inorder_range = (in_l, inorder_idx - 1)
            r_child_inorder_range = (inorder_idx + 1, in_r)

            root.left = _build_tree(l_child_preorder_range, 
                                    l_child_inorder_range)
            root.right = _build_tree(r_child_preorder_range, 
                                     r_child_inorder_range)
            
            return root
        
        return _build_tree((0, len(preorder) - 1), (0, len(inorder) - 1))


if __name__ == "__main__":
    s = Solution()

    # [3,9,20,null,null,15,7]: preorder=[3,9,20,15,7], inorder=[9,3,15,20,7]
    assert compare_trees(
        s.build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]),
        list_to_binary_tree([3, 9, 20, None, None, 15, 7])
    )

    # Single node
    assert compare_trees(
        s.build_tree([1], [1]),
        list_to_binary_tree([1])
    )

    # Left-skewed tree: preorder=[1,2,3], inorder=[3,2,1]
    assert compare_trees(
        s.build_tree([1, 2, 3], [3, 2, 1]),
        list_to_binary_tree([1, 2, None, 3])
    )

    # Right-skewed tree: preorder=[1,2,3], inorder=[1,2,3]
    assert compare_trees(
        s.build_tree([1, 2, 3], [1, 2, 3]),
        list_to_binary_tree([1, None, 2, None, 3])
    )

    # Two nodes, root with left child
    assert compare_trees(
        s.build_tree([1, 2], [2, 1]),
        list_to_binary_tree([1, 2])
    )

    # Two nodes, root with right child
    assert compare_trees(
        s.build_tree([1, 2], [1, 2]),
        list_to_binary_tree([1, None, 2])
    )

    print("All tests passed.")