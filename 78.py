class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root, k): #kth Smallest Element in a BST
        self.k = k
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)

            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            inorder(node.right)

        inorder(root)
        return self.result


# Construct BST:
#       5
#      / \
#     3   6
#    / \
#   2   4
#  /
# 1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

k = 3

sol = Solution()
print(sol.kthSmallest(root, k))