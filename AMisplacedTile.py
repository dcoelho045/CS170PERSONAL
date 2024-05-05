from Node import Node
import heapq

class AMisplacedTile:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # uses a priority queue for forntier to explore nodes with low f(n) = cost + h(n) till a goal state is found
    def solveAmissingTile(self):
        initial_node = Node(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (self.misplacedHeuristic(initial_node.state), initial_node))
        explored = set()

        while frontier:
            _, current = heapq.heappop(frontier)

            if current.state == self.goal_state:
                path, costPerNodePath, hn = self.solPath(current)
                return path, costPerNodePath, hn

            explored.add(current)

            for successor in self.childNode(current):
                if successor not in explored:
                    heapq.heappush(frontier, (successor.cost + self.misplacedHeuristic(successor.state), successor)) 

            if current.cost > 50:
                break

        return None, None, None

    # produces child nodes by cheking where zero is, then chekcing where it can move, and then creating the chidlren nodes
    def childNode(self, node):
        successors = []
        row, colum = self.zeroPos(node.state)

        for action in self.zeroAct(row, colum):
            newState = self.newNode(node.state, row, colum, action)
            newNode = Node(newState, node, action, node.cost + 1)
            successors.append(newNode)

        return successors

    # calculates the misplaced tile heuristic for a given state
    # counts the number of tiles that are not in their goal position and returns this count as the heuristic value
    def misplacedHeuristic(self, state):
        # Misplaced Tile Heuristic
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j] and state[i][j] != 0:
                    misplaced += 1
        return misplaced
    
    # finds the row and column of the zero
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
            actions.append('d')
        if colum > 0:
            actions.append('l')
        if colum < 2:
            actions.append('r')
        return actions

    # generates a new state refering to where the zero can move from the actiona array
    def newNode(self, state, row, colum, action):
        node = [row.copy() for row in state]
        if action == 'u':
            node[row][colum] = node[row - 1][colum]
            node[row - 1][colum] = 0
        elif action == 'd':
            node[row][colum] = node[row + 1][colum]
            node[row + 1][colum] = 0
        elif action == 'l':
            node[row][colum] = node[row][colum - 1]
            node[row][colum - 1] = 0
        elif action == 'r':
            node[row][colum] = node[row][colum + 1]
            node[row][colum + 1] = 0
        return node

    # returns the solution path from the initial state to a given node by following the parents to the root as well as cost and hn
    def solPath(self, node):
        path = []
        current = node
        costPerNodePath = []
        hn = []
        while current:
            path.append(current.state)
            costPerNodePath.append(current.cost)
            hn.append(self.misplacedHeuristic(current.state))
            current = current.parent
        return path[::-1], costPerNodePath[::-1], hn[::-1]
