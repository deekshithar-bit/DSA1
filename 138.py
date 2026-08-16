def kosaraju(V, Adj): #Kosaraju's Algorithm
    # Step 1: DFS and store vertices by finishing time
    visited = [False] * V
    finish_order = []

    def dfs1(node):
        visited[node] = True

        for neighbor in Adj[node]:
            if not visited[neighbor]:
                dfs1(neighbor)

        finish_order.append(node)

    for i in range(V):
        if not visited[i]:
            dfs1(i)

    # Step 2: Create the transpose graph
    transpose = [[] for _ in range(V)]

    for u in range(V):
        for v in Adj[u]:
            transpose[v].append(u)

    # Step 3: DFS on transpose graph in reverse finish order
    visited = [False] * V
    scc_count = 0

    def dfs2(node):
        visited[node] = True

        for neighbor in transpose[node]:
            if not visited[neighbor]:
                dfs2(neighbor)

    for node in reversed(finish_order):
        if not visited[node]:
            dfs2(node)
            scc_count += 1

    return scc_count 
V = 5

Adj = [
    [2, 3],  # 0 -> 2, 3
    [0],     # 1 -> 0
    [1],     # 2 -> 1
    [4],     # 3 -> 4
    []       # 4
]

print(kosaraju(V, Adj))