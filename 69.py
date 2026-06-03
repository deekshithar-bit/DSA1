class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root): #Postorder Transversal of Binary Tree
    if not root:
        return []

    s1 = [root]
    s2 = []

    while s1:
        curr = s1.pop()
        s2.append(curr)

        if curr.left:
            s1.append(curr.left)
        if curr.right:
            s1.append(curr.right)

    ans = []
    while s2:
        ans.append(s2.pop().val)

    return ans

# Example tree:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(postorderTraversal(root))