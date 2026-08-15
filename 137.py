class Solution: #Articulation Points 
    def articulationPoints(self, V, adj):
        disc = [-1] * V
        low = [-1] * V
        parent = [-1] * V
        is_ap = [False] * V

        time = 0

        def dfs(u):
            nonlocal time

            disc[u] = low[u] = time
            time += 1

            children = 0

            for v in adj[u]:

                if v == parent[u]:
                    continue

                if disc[v] == -1:
                    parent[v] = u
                    children += 1

                    dfs(v)

                    low[u] = min(low[u], low[v])

                    if parent[u] == -1 and children > 1:
                        is_ap[u] = True

                    if parent[u] != -1 and low[v] >= disc[u]:
                        is_ap[u] = True

                else:
                    low[u] = min(low[u], disc[v])

        for u in range(V):
            if disc[u] == -1:
                dfs(u)

        ans = []

        for i in range(V):
            if is_ap[i]:
                ans.append(i)

        return ans if ans else [-1]


V = 4

adj = [
    [1],
    [0, 2],
    [1, 3],
    [2]
]

obj = Solution()
print(obj.articulationPoints(V, adj))