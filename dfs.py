
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array, explore_set = set()):
        explore_set.add(self)
        array.append(self.name)

        for child in self.children:
            if child not in explore_set:
                child.depthFirstSearch(array, explore_set)

        return array
        
    def depthFirstSearch2(self, array, explore_set = set()):
        explored_set = set()
        dfs_stack = []
        dfs_stack.append(self)

        while len(dfs_stack) != 0:
          curr_node = dfs_stack.pop()
          explored_set.add(curr_node)
          for child in curr_node.children:
              if child not in explored_set:
                  dfs_stack.append(child)
          array.append(curr_node.name)

        return array
