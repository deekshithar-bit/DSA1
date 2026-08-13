def findBridges(V, edges): #Tarjan’s DFS algorithm
    graph = [[] for _ in range(V)]

    # Build adjacency list
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    disc = [-1] * V
    low = [-1] * V
    time = 0
    bridges = []

    def dfs(u, parent):
        nonlocal time

        disc[u] = low[u] = time
        time += 1

        for v in graph[u]:

            # Ignore the edge back to parent
            if v == parent:
                continue

            # If v is not visited, it is a DFS tree edge
            if disc[v] == -1:
                dfs(v, u)

                # Update low value of u
                low[u] = min(low[u], low[v])

                # Bridge condition
                if low[v] > disc[u]:
                    bridges.append([u, v])

            else:
                # Back edge
                low[u] = min(low[u], disc[v])

    # Graph is connected, so starting from 0 is enough.
    # This loop also makes the code work for disconnected graphs.
    for u in range(V):
        if disc[u] == -1:
            dfs(u, -1)

    return bridges 

V = 5
edges = [
    [0, 1],
    [1, 2],
    [2, 0],
    [1, 3],
    [3, 4]
]

print(findBridges(V, edges))    