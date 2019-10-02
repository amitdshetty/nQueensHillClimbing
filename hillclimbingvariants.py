import hillclimbingalgos
import boardwrapper

# Steepest Ascent without sideway move method
def useSteepHillClimbingApproach(choiceOfIteration,noofQueensOnBoard):
    total = 0
    fail_steps = 0
    solution_path = []
    generated_boards = []
    for _ in range(choiceOfIteration):
        final_state = hillclimbingalgos.steepest_ascent(boardwrapper.BoardWrapper(noofQueensOnBoard))
        total += final_state['is_final_state']
        fail_steps += len(final_state['solution'])
        if final_state['is_final_state']:
            if (final_state['problem'] not in generated_boards) and (len(generated_boards) < 4):
                generated_boards.append(final_state['problem'])
                solution_path.append(final_state['solution'])
    printFinalResult('Steepest Ascent Hill Climbing', solution_path, choiceOfIteration, total)

# Steepest Ascent with Sideway move up to 100 moves
def useSteepHillClimbingApporachWithSidewaysMove(choiceOfIteration,noofQueensOnBoard):
    total = 0
    fail_steps = 0
    solution_path = []
    generated_boards = []
    for _ in range(choiceOfIteration):
        final_state = hillclimbingalgos.steepest_ascent(boardwrapper.BoardWrapper(noofQueensOnBoard), allow_sideways=True)
        total += final_state['is_final_state']
        fail_steps += len(final_state['solution'])
        if final_state['is_final_state']:
            if (final_state['problem'] not in generated_boards) and (len(generated_boards) < 4):
                generated_boards.append(final_state['problem'])
                solution_path.append(final_state['solution'])
    printFinalResult('Steepest Ascent Hill Climbing with Sideway Move', solution_path, choiceOfIteration, total)

# Steepest Ascent with Random Restart (no sideway movement)
def useRandomRestartHillClimbingApporach(choiceOfIteration,noofQueensOnBoard):
    total = 0
    fail_steps = 0
    solution_path = []
    generated_boards = []
    for _ in range(choiceOfIteration):
        final_state = hillclimbingalgos.random_restart(boardwrapper.BoardWrapper(noofQueensOnBoard).__class__, noofQueensOnBoard, allow_sideways=False)
        total += final_state['is_final_state']
        fail_steps += len(final_state['solution'])
        if final_state['is_final_state']:
            if (final_state['problem'] not in generated_boards) and (len(generated_boards) < 4):
                generated_boards.append(final_state['problem'])
                solution_path.append(final_state['solution'])
    printFinalResult('Steepest Ascent with Random Restart Hill Climbing', solution_path, choiceOfIteration, total)

# Steepest Ascent with Random Restart (no sideway movement)
def useRandomRestartHillClimbingApporachWithSidewaysMove(choiceOfIteration,noofQueensOnBoard):
    total = 0
    fail_steps = 0
    solution_path = []
    generated_boards = []
    for _ in range(choiceOfIteration):
        final_state = hillclimbingalgos.random_restart(boardwrapper.BoardWrapper(noofQueensOnBoard).__class__, noofQueensOnBoard, allow_sideways=True)
        total += final_state['is_final_state']
        fail_steps += len(final_state['solution'])
        if final_state['is_final_state']:
            if (final_state['problem'] not in generated_boards) and (len(generated_boards) < 4):
                generated_boards.append(final_state['problem'])
                solution_path.append(final_state['solution'])
    printFinalResult('Steepest Ascent with Random Restart Hill Climbing with Sideways Move', solution_path, choiceOfIteration, total)

def printFinalResult(localSearchAlgoUsed, sample_sequences, choiceOfTries, total):
    print('{} Results :\nSuccess Count : {}\nFailure : {}'.format(localSearchAlgoUsed, total, choiceOfTries - total))
    for i, currentState in enumerate(sample_sequences):
        print('Random Initial Configuration #{}.'.format(i + 1))
        print('Initial State :\n{}'.format(currentState[0]))
        print('Final State :\n{}'.format(currentState[-1]))