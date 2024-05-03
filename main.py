from AMisplacedTile import AMisplacedTile
from UniformCostSearch import UniformCostSearch
from AEuclideanDist import AEuclideanDist

def beginningInput(response):
    toReturn = []
    if (response == '2'):
        input1 = [int(x) for x in input("Enter the first row: ").split()]
        input2 = [int(x) for x in input("Enter the second row: ").split()]
        input3 = [int(x) for x in input("Enter the third row: ").split()]
        intial_state2 = [input1, input2, input3]
        toReturn = intial_state2
    else:
        inital_state1 = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
        toReturn = inital_state1
    
    print("1. Uniform Cost Search")
    print("2. A* with the Misplaced Tile heuristic")
    print("3. A* with the Euclidean distance heuristic")
    choice = input("Enter your choice of algorithm: 1 , 2, or 3 \n")

    return toReturn, choice

def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")
    response = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n")
    initial_state, choice = beginningInput(response)
    if choice == '1': 
        problem = UniformCostSearch(initial_state)
        solution = problem.solveUCS()
        pass
    elif choice == '2':
        problem = AMisplacedTile(initial_state)
        solution = problem.solveAmissingTile()
    else:
        problem = AEuclideanDist(initial_state)
        solution = problem.solveAEuclideanDist()
    

    # Display the solution
    if solution:
        print("Solution found:")
        for state in solution:
            for i in range(3):
                print(state[i])
            print()
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

# solutions: 
# [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
# [[1, 2, 3], [6, 8, 0], [7, 5, 4]]
# [[0, 1, 3], [4, 2, 5], [7, 8, 6]]
# 871602543

# cannot work:
# [[2, 8, 1], [0, 4, 3], [7, 6, 5]]

# print the heuristic cost and the cost from the goal state
# h(n) for Uniform Cost Search = 0
# uniform cost search
    # g(n) = to the length of the tree where the solution is found
    # goal g(n) > start g(n)

# Euclidean
# heuristic 