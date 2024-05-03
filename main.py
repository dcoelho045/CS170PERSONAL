from Problem import Problem

def beginningInput(response):
    if (response == '2'):
        input1 = [int(x) for x in input("Enter the first row: ").split()]
        input2 = [int(x) for x in input("Enter the second row: ").split()]
        input3 = [int(x) for x in input("Enter the third row: ").split()]
        intial_state2 = [input1, input2, input3]
        return intial_state2
    else:
        inital_state1 = [[1, 2, 3], [4, 8, 0], [7, 6, 5]]
        return inital_state1

def main():
    print("Welcome to dcoel003, abrem005, jgonz671, 8 puzzle solver.")
    response = input("Type “1” to use a default puzzle, or “2” to enter your own puzzle. \n")
    beginningInputResponse = beginningInput(response)
        
    problem = Problem(beginningInputResponse)

    
    solution = problem.solve()

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

# cannot work:
# [[2, 8, 1], [0, 4, 3], [7, 6, 5]]