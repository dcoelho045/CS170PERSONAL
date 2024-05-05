from Node import Node
import heapq

class UniformCostSearch:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # uses a priority queue for forntier to explore nodes till a goal state is found
    def solveUCS(self):
        initial_node = Node(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (0, initial_node))
        explored = set()

        while frontier:
            _, current = heapq.heappop(frontier)
            if current.state == self.goal_state:
                path, costPerNodePath, hn = self.solPath(current)
                return  path, costPerNodePath, hn

            explored.add(current)

            for successor in self.childNode(current):
                if successor not in explored:
                    heapq.heappush(frontier, (successor.cost, successor))

            if current.cost > 50:
                break

        return None, None, None

    # produces child nodes by cheking where zero is, then chekcing where it can move, and then creating the chidlren nodes
    def childNode(self, node):
        successors = []
        row, column = self.zeroPos(node.state)

        for action in self.zeroAct(row, column):
            newState = self.nweNode(node.state, row, column, action)
            newNode = Node(newState, node, action, node.cost + 1)
            successors.append(newNode)

        return successors

    # finds the row and column index of the blank tile (0) in a given state and returns them
    def zeroPos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # determines which ways teh zero can move
    def zeroAct(self, row, colum):
        actions = []
        if row > 0:
            actions.append('u')
        if row < 2:
            actions.append('down')
        if colum < 2:
            actions.append('r')
        if colum > 0:
            actions.append('left')
        return actions

    # generates a new state refering to where the zero can move from the actiona array
    def nweNode(self, state, row, column, action):
        node = [row.copy() for row in state]
        if action == 'u':
            node[row][column] = node[row - 1][column]
            node[row - 1][column] = 0
        elif action == 'left':
            node[row][column] = node[row][column - 1]
            node[row][column - 1] = 0
        elif action == 'down':
            node[row][column] = node[row + 1][column]
            node[row + 1][column] = 0
        elif action == 'r':
            node[row][column] = node[row][column + 1]
            node[row][column + 1] = 0
        return node

    # returns the solution path from the initial state to a given node by following the parents to the root as well as cost - hn is always zero for ucs
    def solPath(self, node):
        path = []
        costPerNodePath = []
        hn = []
        current = node
        while current:
            path.append(current.state)
            costPerNodePath.append(current.cost)
            hn.append(0)
            current = current.parent
        return path[::-1], costPerNodePath[::-1], hn