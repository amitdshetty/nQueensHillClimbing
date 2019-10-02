import random

# Steepest ascent with and without sideways
def steepest_ascent(board_wrapper, allow_sideways=False, max_sideways=100):
    node = board_wrapper.start_state
    node_cost = board_wrapper.cost_function(node)
    path = []
    sideways_moves = 0
    while True:
        path.append(node)
        best_move = get_next_best_move(node, board_wrapper)
        best_move_cost = board_wrapper.cost_function(best_move)
        if best_move_cost > node_cost:
            break
        elif best_move_cost == node_cost:
            if not allow_sideways or sideways_moves == max_sideways:
                break
            else:
                sideways_moves += 1
        else:
            sideways_moves = 0
        node = best_move
        node_cost = best_move_cost
    return {'is_final_state': 1 if board_wrapper.is_goal(node) else 0, 'solution': path , 'problem': board_wrapper}

# Random restart using steepest ascent with and without sideways
def random_restart(random_board, noofQueensOnBoard, allow_sideways):
    num_restarts = 100
    path = []
    for _ in range(num_restarts):
        result = steepest_ascent(random_board(noofQueensOnBoard), allow_sideways)
        path += result['solution']
        if result['is_final_state'] == 1:
            break
    result['solution'] = path
    return result

# Calculate the cost of getting the nest best move based on the queen attack heuristic
def get_next_best_move(node, problem):
    best_moves = node.get_children()
    moves_cost = [problem.cost_function(child) for child in best_moves]
    min_cost = min(moves_cost)
    best_move = random.choice([move for move_index, move in enumerate(best_moves) if moves_cost[move_index] == min_cost])
    return best_move