class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val): #Search in a Binary Search Tree
    if not root or root.val == val:
        return root
    return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)

# Create BST
#        4
#      /   \
#     2     7
#    / \
#   1   3

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

# Search for value 2
result = searchBST(root, 2)

if result:
    print("Found node:", result.val)
else:
    print("Value not found")
