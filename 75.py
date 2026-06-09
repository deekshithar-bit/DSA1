class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root, lo=None, hi=None): #Validate Binary Search Tree
    if not root:
        return True

    if (lo is not None and root.val <= lo) or \
       (hi is not None and root.val >= hi):
        return False

    return (isValidBST(root.left, lo, root.val) and
            isValidBST(root.right, root.val, hi))


# Example 1: Valid BST
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)

print("Tree 1:", isValidBST(root1))


# Example 2: Invalid BST
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print("Tree 2:", isValidBST(root2))