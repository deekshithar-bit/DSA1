class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root): #Maximum Depth of Binary Tree
    if not root:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1

# Create a binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Maximum Depth:", maxDepth(root))