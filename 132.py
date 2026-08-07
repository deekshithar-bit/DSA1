def topological_sort_dfs(n, graph): #Topological Sort DFS
    visited = [False] * n
    ans = []

    def dfs(curr):
        visited[curr] = True
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                dfs(neighbor)
        ans.append(curr)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return ans[::-1]


# Number of vertices
n = 6

# Adjacency list
adj = [
    [],        # 0
    [],        # 1
    [3],       # 2 -> 3
    [1],       # 3 -> 1
    [0, 1],    # 4 -> 0, 1
    [0, 2]     # 5 -> 0, 2
]

# Perform topological sort
result = topological_sort_dfs(n, adj)

# Print the result
print("Topological Order:", result)