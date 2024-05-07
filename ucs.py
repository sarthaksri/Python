import queue as Q                   #UCS

def ucs(graph, start, end):
  queue = Q.PriorityQueue()
  queue.put((0, [start]))

  while not queue.empty():
    node = queue.get()
    current = node[1][len(node[1]) - 1]
    print("Current node: ", current)
    if end in node[1]:
      print("Path Found: " + str(node[1]), "Cost: ", str(node[0]))
      break

    cost = node[0]
    for neighbor in graph[current]:
      temp = node[1][:]

      temp.append(neighbor)
      print("temp node: ", temp)
      queue.put((cost + graph[current][neighbor], temp))



  graph = {'S' : {'A': 1, 'B': 5, 'C': 15}, 'A': {'S': 1, 'G': 10}, 'B': {'S': 5, 'G': 5}, 'C': {'S': 15, 'G': 5}, 'G': {'A': 10, 'B': 5, 'C': 5}}
  ucs(graph, 'S', 'G')
