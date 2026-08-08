from collections import deque #Number of Operations to Make Network Connected

def makeConnected(n, connections):
    if len(connections) < n - 1:
        return -1

    graph = [[] for _ in range(n)]

    for u, v in connections:
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * n
    components = 0

    def bfs(src):
        q = deque([src])
        visited[src] = True

        while q:
            curr = q.popleft()

            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    q.append(neighbor)

    for i in range(n):
        if not visited[i]:
            components += 1
            bfs(i)

    return components - 1


# Example input
n = 4
connections = [[0, 1], [0, 2], [1, 2]]

# Function call
result = makeConnected(n, connections)

print("Minimum operations required:", result)