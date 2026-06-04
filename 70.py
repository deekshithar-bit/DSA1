from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):  #Level Order Traversal Queue BFS
    if not root:
        return []

    q = deque([root])
    ans = []

    while q:
        levelArr = []
        levelSize = len(q)

        for _ in range(levelSize):
            curr = q.popleft()

            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

            levelArr.append(curr.val)

        ans.append(levelArr)

    return ans

# Create the tree:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(levelOrder(root))