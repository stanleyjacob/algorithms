# binary tree node

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)
        if left_depth > right_depth:
            return left_depth
        return right_depth
