from Node import Node
import heapq

class Problem:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def solve(self):
        initial_node = Node(self.initial_state)
        frontier = []
        heapq.heappush(frontier, (self.misplacedHeuristic(initial_node.state), initial_node))
        explored = set()

        while frontier:
            _, current_node = heapq.heappop(frontier)

            if current_node.state == self.goal_state:
                return self.get_solution_path(current_node)

            explored.add(current_node)

            for successor in self.get_successors(current_node):
                if successor not in explored:
                    heapq.heappush(frontier, (successor.cost + self.misplacedHeuristic(successor.state), successor))

        return None

    def get_successors(self, node):
        successors = []
        zero_row, zero_col = self.get_zero_position(node.state)

        for action in self.get_valid_actions(zero_row, zero_col):
            new_state = self.generate_new_state(node.state, zero_row, zero_col, action)
            new_node = Node(new_state, node, action, node.cost + 1)
            successors.append(new_node)

        return successors

    def misplacedHeuristic(self, state):
        # Misplaced Tile Heuristic
        misplaced = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != self.goal_state[i][j]:
                    misplaced += 1
        return misplaced

    # def manhattanHeuristic(self, state):
    #     # Manhattan Distance Heuristic
    #     total_distance = 0
    #     for i in range(3):
    #         for j in range(3):
    #             value = state[i][j]
    #             if value != 0:
    #                 goal_row, goal_col = (value - 1) // 3, (value - 1) % 3
    #                 total_distance += abs(i - goal_row) + abs(j - goal_col)
    #     return total_distance


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
