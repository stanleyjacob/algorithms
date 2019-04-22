
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        bfs_queue = [self]
        while len(bfs_queue) > 0:
          curr_elem = bfs_queue.pop(0)
          array.append(curr_elem.name)
          for child in curr_elem.children:
            bfs_queue.append(child)

        return array
