class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root): # Inverting a Binary Tree
    if not root:
        return root

    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root

# Function to print tree in preorder traversal
def preorder(root):
    if not root:
        return
    print(root.val, end=" ")
    preorder(root.left)
    preorder(root.right)

# Create tree:
#        4
#      /   \
#     2     7
#    / \   / \
#   1   3 6   9

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print("Original Tree (Preorder):")
preorder(root)

invertTree(root)

print("\nInverted Tree (Preorder):")
preorder(root)

#Inverted tree:
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1