import random

# Define the new goal state
goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

# Heuristic function: number of misplaced tiles
def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

# Actions: Up, Down, Left, Right
def actions(state):
    i, j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    possible_actions = []
    if i > 0: possible_actions.append((-1, 0))  # Up
    if i < 2: possible_actions.append((1, 0))   # Down
    if j > 0: possible_actions.append((0, -1))  # Left
    if j < 2: possible_actions.append((0, 1))   # Right
    return possible_actions

# Apply action to the state
def apply_action(state, action):
    new_state = [row[:] for row in state]
    i, j = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    di, dj = action
    new_i, new_j = i + di, j + dj
    new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
    return new_state

# Hill climb search
def hill_climb_search(initial_state):
    current_state = initial_state
    current_cost = misplaced_tiles(current_state)
    # best_state = current_state
    # best_cost = current_cost
    path = [initial_state]
    
    while True:
        neighbors = [(apply_action(current_state, action), action) for action in actions(current_state)]
        neighbor_states = [state for state, _ in neighbors]
        neighbor_costs = [misplaced_tiles(state) for state in neighbor_states]
        
        min_neighbor_cost = min(neighbor_costs)
        
        if min_neighbor_cost >= current_cost:
            return path
        
        best_neighbor_idx = neighbor_costs.index(min_neighbor_cost)
        best_neighbor_state, best_neighbor_action = neighbors[best_neighbor_idx]

        
        current_state = best_neighbor_state
        current_cost = min_neighbor_cost
        path.append(current_state)

# Test
initial_state = [[2, 0, 3],
                 [1, 8, 4],
                 [7, 6, 5]]

path = hill_climb_search(initial_state)


if path:
    print("Path to goal state:")
    for idx, state in enumerate(path):
        print("Step", idx + 1)
        for row in state:
            print(row)
        print()
else:
    print("Goal state not found.")
