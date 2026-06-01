# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: #Preorder Transversal of Binary Tree
    def preorderTraversal(self, root):
        ans = []

        def traversal(curr):
            if not curr:
                return
            ans.append(curr.val)      # Root
            traversal(curr.left)      # Left
            traversal(curr.right)     # Right

        traversal(root)
        return ans

# Example tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
print(sol.preorderTraversal(root))