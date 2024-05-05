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