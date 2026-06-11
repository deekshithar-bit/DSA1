class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val): #insert into a Binary Search tree 
    if not root:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Create BST
root = None

# Insert values
values = [4, 2, 7, 1, 3, 6, 9]
for v in values:
    root = insertIntoBST(root, v)

# Print BST in sorted order
print("Inorder Traversal:")
inorder(root) 
#structure of BST : 
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9