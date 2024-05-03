from Node import Node
import heapq

class UniformCostSearch:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def solveUCS(self):
        initial_node = Node(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (0, initial_node))
        explored = set()

        while frontier:
            _, current_node = heapq.heappop(frontier)
            print("current_node cost: ", current_node.cost)
            if current_node.state == self.goal_state:
                return self.get_solution_path(current_node) 

            explored.add(current_node)

            for successor in self.get_successors(current_node):
                if successor not in explored:
                    heapq.heappush(frontier, (successor.cost, successor))

        return None

    def get_successors(self, node):
        successors = []
        zero_row, zero_col = self.get_zero_position(node.state)

        for action in self.get_valid_actions(zero_row, zero_col):
            new_state = self.generate_new_state(node.state, zero_row, zero_col, action)
            new_node = Node(new_state, node, action, node.cost + 1)
            successors.append(new_node)

        return successors

    def get_zero_position(self, state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def get_valid_actions(self, zero_row, zero_col):
        actions = []
        if zero_row > 0:
            actions.append('up')
        if zero_row < 2:
            actions.append('down')
        if zero_col > 0:
            actions.append('left')
        if zero_col < 2:
            actions.append('right')
        return actions

    def generate_new_state(self, state, zero_row, zero_col, action):
        new_state = [row.copy() for row in state]
        if action == 'up':
            new_state[zero_row][zero_col] = new_state[zero_row - 1][zero_col]
            new_state[zero_row - 1][zero_col] = 0
        elif action == 'down':
            new_state[zero_row][zero_col] = new_state[zero_row + 1][zero_col]
            new_state[zero_row + 1][zero_col] = 0
        elif action == 'left':
            new_state[zero_row][zero_col] = new_state[zero_row][zero_col - 1]
            new_state[zero_row][zero_col - 1] = 0
        elif action == 'right':
            new_state[zero_row][zero_col] = new_state[zero_row][zero_col + 1]
            new_state[zero_row][zero_col + 1] = 0
        return new_state

    def get_solution_path(self, node):
        path = []
        current_node = node
        while current_node:
            path.append(current_node.state)
            current_node = current_node.parent
        return path[::-1]