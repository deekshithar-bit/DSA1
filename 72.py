class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum): #Path Sum
    if not root:
        return False

    ans = [False]

    def traverse(curr, currSum):
        newSum = currSum + curr.val

        if not curr.left and not curr.right:
            if newSum == targetSum:
                ans[0] = True

        if curr.left:
            traverse(curr.left, newSum)

        if curr.right:
            traverse(curr.right, newSum)

    traverse(root, 0)
    return ans[0]


# Constructing the tree:
#         5
#        / \
#       4   8
#      /   / \
#     11  13  4
#    /  \
#   7    2

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

print(hasPathSum(root, 22))