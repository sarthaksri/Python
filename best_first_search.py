from queue import PriorityQueue

goal_state = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

def misplaced_tiles(state):
  count = 0
  for i in range(3):
    for j in range(3):
      if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
        count += 1
  return count

def actions(state):
  i, j = next((i,j) for i in range(3) for j in range(3) if state[i][j] == 0)
  possible_actions = []
  if i > 0 : possible_actions.append((-1, 0)) # up
  if i < 2 : possible_actions.append((1, 0)) # down
  if j > 0 : possible_actions.append((0, -1)) # left
  if j < 2 : possible_actions.append((0, 1)) # right
  return possible_actions

def apply_action(state, action):
  new_state = [row[:] for row in state]
  i, j = next((i,j) for i in range(3) for j in range(3) if state[i][j] == 0)
  di, dj = action
  new_i, new_j = i + di, j + dj
  new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
  return new_state
                                                                                   

def best_first_search(initial_state):
  frontier = PriorityQueue()
  frontier.put((misplaced_tiles(initial_state), initial_state))
  explored = set()
  parent = {}
  parent[tuple(map(tuple, initial_state))] = None

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
      if tuple(map(tuple, new_state)) not in explored:
        frontier.put((misplaced_tiles(new_state), new_state))
        parent[tuple(map(tuple, new_state))] = current_state

  return None



initial_state = [[2, 0, 3],
                 [1, 8, 4],
                 [7, 6, 5]]

path = best_first_search(initial_state)

if path:
  print("Path to goal state:")
  for idx, state in enumerate(path):
    print("Step", idx + 1)
    for row in state:
      print(row)
    print()
else:
  print("Goal not found.")