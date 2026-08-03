class Node: #Depth First Search (DFS)
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def cloneGraph(root: 'Node') -> 'Node':
    if not root:
        return None

    stack = [root]
    visited = {}             # original_node -> cloned_node

    cloneRoot = Node(root.val)
    visited[root] = cloneRoot

    while stack:
        curr = stack.pop()   # LIFO: iterative DFS
        cloneCurr = visited[curr]

        for n in curr.neighbors:
            if n not in visited:
                visited[n] = Node(n.val)
                stack.append(n)
            cloneCurr.neighbors.append(visited[n])

    return cloneRoot


# ---------------- Test ----------------

# Create a graph:
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

# Clone the graph
clone = cloneGraph(node1)

# Print the cloned graph using DFS
visited = set()

def printGraph(node):
    stack = [node]
    while stack:
        curr = stack.pop()
        if curr in visited:
            continue
        visited.add(curr)
        print(f"Node {curr.val} -> {[n.val for n in curr.neighbors]}")
        for neighbor in curr.neighbors:
            stack.append(neighbor)

print("Cloned Graph:")
printGraph(clone)