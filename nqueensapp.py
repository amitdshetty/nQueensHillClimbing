import sys
import hillclimbingvariants

def main():
    # Default condition of 4 queens is no input is given
    noofQueensOnBoard = int(input('Enter the number of Queens to be placed on the board\n') or '4')
    # User cannot enter a number less than 2 or a number which is not a multiple of 2 for user validation
    if noofQueensOnBoard <= 2 or noofQueensOnBoard % 2 != 0 :
        print('Invalid Input. Please enter a value greater than and a multiple of 2')
        sys.exit(1)
    # User input for choice of algorithm
    print('Enter the choice of the algorithm to solve {}-queens problem'.format(noofQueensOnBoard))
    choiceOfAlgorithm = int(input('1. Steepest Hill Climb Algorithm\n2. Steepest Hill Climb Using Sideways Move Algorithm\n3. Random Restart Hill Climbing Algorithm\n4. Random Restart Hill Climbing Algorithm using sideways motion\n') or '1')
    print('Enter number of times for the local search technique to be applied on the problem')
    # No input by the user triggers a default case which inputs 300 as the number of iterations
    choiceOfTries = int(input('1.300\n2.400\n3.500\n4.600\n5.700\n6.800\n7.900\n8.1000\n') or '1')
    if choiceOfTries == 1:
        numOfIteration = 300
    elif choiceOfTries == 2:
        numOfIteration = 400
    elif choiceOfTries == 3:
        numOfIteration = 500
    elif choiceOfTries == 4:
        numOfIteration = 600
    elif choiceOfTries == 5:
        numOfIteration = 700
    elif choiceOfTries == 6:
        numOfIteration = 800
    elif choiceOfTries == 7:
        numOfIteration = 900
    elif choiceOfTries == 8:
        numOfIteration = 1000
    else :
        print('Invalid Choice for number of tries. Please try again')
        sys.exit(1)
    if choiceOfAlgorithm == 1:
        hillclimbingvariants.useSteepHillClimbingApproach(numOfIteration,noofQueensOnBoard)
    elif choiceOfAlgorithm == 2:
        hillclimbingvariants.useSteepHillClimbingApporachWithSidewaysMove(numOfIteration,noofQueensOnBoard)
    elif choiceOfAlgorithm == 3:
        hillclimbingvariants.useRandomRestartHillClimbingApporach(numOfIteration,noofQueensOnBoard)
    elif choiceOfAlgorithm == 4:
        hillclimbingvariants.useRandomRestartHillClimbingApporachWithSidewaysMove(numOfIteration,noofQueensOnBoard)
    else :
        print('Invalid Entry for Algorithm Choice. Try again')
        sys.exit(1)


if __name__ == '__main__':
    main()