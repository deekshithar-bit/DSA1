class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#Symmetric Tree Recursive Approach

def isMirror(left, right):
    if not left and not right:
        return True
    if not left or not right:
        return False

    return (left.val == right.val and
            isMirror(left.left, right.right) and
            isMirror(left.right, right.left))


def isSymmetric(root):
    if root is None:
        return True
    return isMirror(root.left, root.right)


# Example symmetric tree:
#         1
#       /   \
#      2     2
#     / \   / \
#    3  4  4  3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(isSymmetric(root))