from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzag_level_order(self, root: TreeNode) -> list[list[int]]:
        """
        Description:
        Given the root of a binary tree, return the zigzag level order traversal 
        of its nodes' values. Start with left to right, then right to left.
        
        Example:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[20,9],[15,7]]
        """
        
        if not root:
            return []

        is_l_to_r = True
        queue = deque([root])
        traversal = []

        while queue:
            level_traversal = []
            for _ in range(len(queue)):
                if is_l_to_r:
                    curr_node = queue.popleft()
                    if curr_node.left:
                        queue.append(curr_node.left)
                    if curr_node.right:
                        queue.append(curr_node.right)
                else:
                    curr_node = queue.pop()
                    if curr_node.right:
                        queue.appendleft(curr_node.right)
                    if curr_node.left:
                        queue.appendleft(curr_node.left)
                
                level_traversal.append(curr_node.val)

            traversal.append(level_traversal)
            is_l_to_r = not is_l_to_r

        return traversal


if __name__ == "__main__":
    s = Solution()
    # test cases
    assert s.zigzag_level_order(
        TreeNode(3, 
                 TreeNode(9), 
                 TreeNode(20, 
                          TreeNode(15), 
                          TreeNode(7))
                )
    ) == [[3], [20, 9], [15, 7]]
    assert s.zigzag_level_order(None) == []
    assert s.zigzag_level_order([]) == []
    assert s.zigzag_level_order(TreeNode(1)) == [[1]]
    print("All tests passed.")