from Node import Node
import heapq

class AEuclideanDist:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # uses a priority queue for forntier to explore nodes with low f(n) = cost + h(n) till a goal state is found
    def solveAEuclideanDist(self):
        initial_node = Node(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (self.euclideanHeuristic(initial_node.state), initial_node))
        explored = set()

        while frontier:
            _, current = heapq.heappop(frontier)

            if current.state == self.goal_state:
                path, costPerNodePath, hn = self.solPath(current)
                return path, costPerNodePath, hn

            explored.add(current)

            for successor in self.childNode(current):
                if successor not in explored:
                    heapq.heappush(frontier, (successor.cost + self.euclideanHeuristic(successor.state), successor))
            
            if current.cost > 50:
                break

        return None, None, None

    # produces child nodes by cheking where zero is, then chekcing where it can move, and then creating the chidlren nodes
    def childNode(self, node):
        successors = []
        row, column = self.zeroPos(node.state)

        for action in self.zeroAct(row, column):
            newState = self.newNode(node.state, row, column, action)
            newNode = Node(newState, node, action, node.cost + 1)
            successors.append(newNode)

        return successors
    
    # calculates the euclidean heuritic for a given state
    def euclideanHeuristic(self, state):
        distance = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    row, column = (value - 1) // 3, (value - 1) % 3
                    distance += ((i - row) ** 2 + (j - column) ** 2) ** 0.5
        return distance

    
    # finds the row and column index of the blank tile (0) in a given state and returns them
    def zeroPos(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    # determines the valid actions (up, down, left, right) that can be applied to the blank tile based on its current position
    def zeroAct(self, row, column):
        actions = []
        if row > 0:
            actions.append('u')
        if column > 0:
            actions.append('l')
        if column < 2:
            actions.append('r')
        if row < 2:
            actions.append('d')
        return actions

    # generates a new state by applying an action to the blank tile in the current state
    def newNode(self, state, row, column, action):
        node = [row.copy() for row in state]
        if action == 'u':
            node[row][column] = node[row - 1][column]
            node[row - 1][column] = 0
        elif action == 'd':
            node[row][column] = node[row + 1][column]
            node[row + 1][column] = 0
        elif action == 'l':
            node[row][column] = node[row][column - 1]
            node[row][column - 1] = 0
        elif action == 'r':
            node[row][column] = node[row][column + 1]
            node[row][column + 1] = 0
        return node

    # returns the solution path from the initial state to a given node by following the parents to the root as well as cost and hn
    def solPath(self, node):
        path = []
        costPerNodePath = []
        hn = []
        current = node
        while current:
            path.append(current.state)
            costPerNodePath.append(current.cost)
            hn.append(self.euclideanHeuristic(current.state))
            current = current.parent
        return path[::-1], costPerNodePath[::-1], hn[::-1]
