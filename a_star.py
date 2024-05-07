from queue import PriorityQueue

# Define the goal state
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

# A* algorithm
def a_star(initial_state):
    frontier = PriorityQueue()
    frontier.put((misplaced_tiles(initial_state), initial_state))
    explored = set()
    parent = {}
    g = {}
    g[tuple(map(tuple, initial_state))] = 0

    while not frontier.empty():
        _, current_state = frontier.get()

        if current_state == goal_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(tuple(map(tuple, current_state)))
            return path[::-1]

        explored.add(tuple(map(tuple, current_state)))

        for action in actions(current_state):
            new_state = apply_action(current_state, action)
            new_cost = g[tuple(map(tuple, current_state))] + 1
            if tuple(map(tuple, new_state)) not in explored or new_cost < g.get(tuple(map(tuple, new_state)), float('inf')):
                g[tuple(map(tuple, new_state))] = new_cost
                frontier.put((new_cost + misplaced_tiles(new_state), new_state))
                parent[tuple(map(tuple, new_state))] = current_state

    return None

# Test
initial_state = [[2, 0, 3],
                 [1, 8, 4],
                 [7, 6, 5]]


path = a_star(initial_state)

if path:
    print("Path to goal state:")
    for idx, state in enumerate(path):
        print("Step", idx + 1)
        for row in state:
            print(row)
        print()
else:
    print("Goal state not found.")
