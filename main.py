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
    choice = input("Enter your choice of algorithm: 1, 2, or 3 \n")

    return toReturn, choice

def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")
    response = input("Type 1 to use a default puzzle, or 2 to enter your own puzzle. \n")
    initial_state, choice = beginningInput(response)
    if choice == '1': 
        problem = UniformCostSearch(initial_state)
        solution, costPerNodePath, hn = problem.solveUCS()
        pass
    elif choice == '2':
        problem = AMisplacedTile(initial_state)
        solution, costPerNodePath, hn = problem.solveAmissingTile()
    else:
        problem = AEuclideanDist(initial_state)
        solution, costPerNodePath, hn = problem.solveAEuclideanDist()
    

    # Display the solution
    if solution:
        print("Solution found:")
        for i in range(len(solution)):
            print("g(n):", costPerNodePath[i], "\th(n):", hn[i])
            node = solution[i]
            for j in range(3):
                print(node[j])
            print()
        print("GOAL!!!\n")
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()

# SOLUTIONS: 
# 1. [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
# 2. [[1, 2, 3], [6, 8, 0], [7, 5, 4]]
# 3. [[0, 1, 3], [4, 2, 5], [7, 8, 6]]  
# 4. [[1, 2, 3], [4, 5, 6], [7, 8, 0]] Trivial
# 5. [[1, 2, 3], [4, 5, 6], [7, 0, 8]] Very Easy
# 6. [[1, 2, 0], [4, 5, 3], [7, 8, 6]] Easy
# 7. [[0, 1, 2], [4, 5, 3], [7, 8, 6]] Doable
# 8. [[8, 7, 1], [6, 0, 2], [5, 4, 3]] Oh Boy - takes to long 10,000 iterations and can't find a solution

# CANNOT WORK:
# [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
# [[1, 2, 3], [4, 5, 6], [8, 7, 0]]

# NOTES
# goal g(n) > start g(n)
# g(n) = length of the tree from root to where solution is found
# h(n) = heuristic 