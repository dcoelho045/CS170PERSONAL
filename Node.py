class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    # defines the equality comparison between two Node instances
    def __eq__(self, other):
        return self.state == other.state
    
    # defines the less than comparison between two Node instances. Used for ordering objects
    def __lt__(self, other):
        return self.cost < other.cost

    # defines how the object is hashed, which is used for membership testing in sets and dictionaries
    # necessary when you want to use instances of the Node class as keys in a dictionary 
    def __hash__(self):
        return hash(str(self.state))

    # returns the path from the current node to the root node (node) in the search tree
    # traverses the parent links starting from the current node (self) and appends the actions taken at each step to the path list. 
    # Finally, reverses the path list to get the correct order of actions from the root to the current node.
    def get_solution_path(self, node):
        path = []
        current_node = node
        while current_node.parent:
            path.append(current_node.action)
            current_node = current_node.parent
        return path[::-1]
