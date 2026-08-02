from collections import deque #Breadth First Search (BFS)

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if not node:
        return None

    visited = {}
    q = deque([node])

    cloneRoot = Node(node.val)
    visited[node] = cloneRoot

    while q:
        curr = q.popleft()
        cloneCurr = visited[curr]

        for n in curr.neighbors:
            if n not in visited:
                visited[n] = Node(n.val)
                q.append(n)
            cloneCurr.neighbors.append(visited[n])

    return cloneRoot

# -------- Create a sample graph --------
# Graph:
# 1 -- 2
# |    |
# 4 -- 3

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

# -------- Clone the graph --------
cloned = cloneGraph(node1)

# -------- Print the cloned graph using BFS --------
def printGraph(node):
    visited = set()
    q = deque([node])

    while q:
        curr = q.popleft()
        if curr in visited:
            continue

        visited.add(curr)
        print(f"Node {curr.val}: {[n.val for n in curr.neighbors]}")

        for n in curr.neighbors:
            if n not in visited:
                q.append(n)

print("Original Graph:")
printGraph(node1)

print("\nCloned Graph:")
printGraph(cloned)