from collections import deque         #blocksWorldDFS

# Define the initial state
initial_state = [
    ['A'],
    ['B','C'],
    []
]

# Define the goal state
goal_state = [
    ['A','B','C'],
    [],[]
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

# Define the DFS algorithm
def dfs(initial_state, goal_state):
    frontier = deque([(initial_state, [initial_state])])
    visited = set()

    while frontier:
        state, path = frontier.pop()
        if state == goal_state:
            return path
        if tuple(map(tuple, state)) in visited:
            continue
        visited.add(tuple(map(tuple, state)))

        for action in actions(state):
            new_state = transition(state, action)
            frontier.append((new_state, path + [new_state]))

    return None

# Find the solution
solution = dfs(initial_state, goal_state)

if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")