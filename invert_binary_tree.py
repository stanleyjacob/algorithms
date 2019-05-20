
def invertBinaryTree(tree):
    if tree is None:
        return
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
