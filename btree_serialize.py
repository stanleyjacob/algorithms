# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        ret_str = []
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            curr_elem = q.get()
            if curr_elem is None:
                ret_str.append("null")
            else:
                ret_str.append(str(curr_elem.val))
                q.put(curr_elem.left)
                q.put(curr_elem.right)
        return ",".join(ret_str)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        list_nodes = data.split(",")
        ret_node = None
        if len(list_nodes) == 0:
            return ret_node
        ret_node = TreeNode(list_nodes[0])
        q = queue.Queue()
        q.put((ret_node, 0))
        while not q.empty():
            curr_node, i = q.get()
            if curr_node == "null":
                continue
            child_left_index = 2 * i + 1
            child_right_index = 2 * i + 2
            if child_left_index >= len(list_nodes):
                continue
            left = TreeNode(list_nodes[child_left_index])
            curr_node.left = left
            q.put((left, child_left_index))
            
            if child_right_index >= len(list_nodes):
                continue
            right = TreeNode(list_nodes[child_right_index])
            curr_node.right = right
            q.put((right, child_right_index))
        
        return ret_node
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(None)
str_curr = codec.serialize(None)
# codec.deserialize(codec.serialize(root))
