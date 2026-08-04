from typing import List #All Paths from Source to Target

def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    target = len(graph) - 1
    res = []
    path = []

    def dfs(node):
        path.append(node)

        if node == target:
            res.append(path.copy())
        else:
            for nei in graph[node]:
                dfs(nei)

        path.pop()

    dfs(0)
    return res


# Example input
graph = [[1, 2], [3], [3], []]

# Output
print(allPathsSourceTarget(graph))