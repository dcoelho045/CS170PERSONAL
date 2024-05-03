class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __eq__(self, other):
        return self.state == other.state
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __hash__(self):
        return hash(str(self.state))

def get_solution_path(self, node):
    path = []
    current_node = node
    while current_node.parent:
        path.append(current_node.action)
        current_node = current_node.parent
    return path[::-1]
