
# O(d) space, O(n) time
def invertBinaryTree(tree):
    if tree is None:
        return
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

# O(n) space, O(n) time
# Common bug: referring to tree in while loop
#             rather than curr_elem
def invertBinaryTree(tree):
	curr_queue = [tree]
	while len(curr_queue):
		curr_elem = curr_queue.pop(0)
		if curr_elem is None:
			continue
		else:
			curr_elem.left, curr_elem.right = \
				curr_elem.right, curr_elem.left
			curr_queue.append(curr_elem.left)
			curr_queue.append(curr_elem.right)
