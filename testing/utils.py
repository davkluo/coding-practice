from classes import TreeNode

def compare_lists(list1, list2):
    return sorted(list1) == sorted(list2)

def list_to_binary_tree(list):
    if not list:
        return None
    root = TreeNode(list[0])
    queue = [root]
    i = 1
    while queue and i < len(list):
        node = queue.pop(0)
        if list[i] is not None:
            node.left = TreeNode(list[i])
            queue.append(node.left)
        i += 1
        if i < len(list) and list[i] is not None:
            node.right = TreeNode(list[i])
            queue.append(node.right)
        i += 1
    return root

def compare_trees(tree1, tree2):
    if not tree1 and not tree2:
        return True
    if not tree1 or not tree2:
        return False
    return (tree1.val == tree2.val and
            compare_trees(tree1.left, tree2.left) and
            compare_trees(tree1.right, tree2.right))