from collections import defaultdict #Detect Cycle in Undirected Connected Graph

def hasCycle(edges):
    graph = defaultdict(list)

    # Build the adjacency list
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    visited = set()

    def dfs(curr, parent):
        visited.add(curr)

        for neighbor in graph[curr]:
            if neighbor not in visited:
                if dfs(neighbor, curr):
                    return True
            elif neighbor != parent:
                return True

        return False

    # Check every connected component
    for node in graph:
        if node not in visited:
            if dfs(node, -1):
                return True

    return False


print(hasCycle([[0,1],[1,2],[2,0]]))               # True
print(hasCycle([[0,1],[1,2],[2,3]]))               # False
print(hasCycle([[0,1],[1,2],[2,3],[3,4],[1,4]]))   # True