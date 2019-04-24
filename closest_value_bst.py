
def findClosestValueInBstHelper(tree, target, closest):
	if tree is None:
		return closest
	
	if tree.value == target:
		return target
	
	if abs(target - tree.value) < abs(target - closest):
		closest = tree.value
	
	if target < tree.value:
		return findClosestValueInBstHelper(tree.left, target, closest)
	
	if target > tree.value:
		return findClosestValueInBstHelper(tree.right, target, closest)
	
def findClosestValueInBst(tree, target):
	return findClosestValueInBstHelper(tree, target, float('inf'))

def findClosestValueInBst2(tree, target):
    closest_value = float('inf')
	curr_node = tree
	
	while curr_node is not None:
		
		if target == curr_node.value:
			return target
		
		diff = abs(target - curr_node.value)
		if diff < abs(target - closest_value):
			closest_value = curr_node.value
		
		if target > curr_node.value:
			curr_node = curr_node.right
			
		elif target < curr_node.value:
			curr_node = curr_node.left
	
	return closest_value
