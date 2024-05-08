from collections import deque         #blocksWorldDLSD1

# Define the initial state
initial_state = [
    ['A'],
    ['B','C'],
    []
]

# Define the goal state
goal_state = [
    ['A','B','C'],
    [],
    []
]

# Define the possible actions
def actions(state):
    actions = []
    for i in range(len(state)):
        for j in range(len(state)):
            if i != j and state[i]:
                actions.append((i, j))
    return actions

# Define the transition function
def transition(state, action):
    new_state = [s[:] for s in state]
    i, j = action
    new_state[j].append(new_state[i].pop())
    return new_state

# Define the Depth-Limited Search algorithm with D = 1
def dls(initial_state, goal_state, depth_limit):
    frontier = deque([(initial_state, [initial_state], 0)])  # Include depth in the frontier tuple
    visited = set()

    while frontier:
        state, path, depth = frontier.popleft()
        if state == goal_state:
            return path
        if depth >= depth_limit:  # Check if depth limit is reached
            break
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))

        for action in actions(state):
            new_state = transition(state, action)
            frontier.append((new_state, path + [new_state], depth + 1))  # Increase depth by 1

    return None

# Find the solution using Depth-Limited Search with D = 1
solution = dls(initial_state, goal_state, depth_limit=1)

if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
