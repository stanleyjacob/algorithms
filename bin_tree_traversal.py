# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        list_return = []
        q = queue.Queue()   # contains value and level
        q.put((root, 0))
        
        while not q.empty():
            
            curr_node, curr_level = q.get()
            
            if curr_node is not None:
                
                if len(list_return) == curr_level:
                    list_return.append([])
                list_return[curr_level].append(curr_node.val)
            
                index = curr_level + 1
                q.put((curr_node.left, index))
                q.put((curr_node.right, index))
                
        return list_return
