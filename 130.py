from collections import defaultdict, deque #Reconstruct Itinerary
from typing import List

def findItinerary(tickets: List[List[str]]) -> List[str]:
    graph = defaultdict(list)

    # Build graph
    for frm, to in tickets:
        graph[frm].append(to)

    # Sort destinations and convert to deque
    for k in graph:
        graph[k].sort()
        graph[k] = deque(graph[k])

    path = []

    def dfs(curr: str):
        dest = graph.get(curr, deque())
        while dest:
            nxt = dest.popleft()
            dfs(nxt)
        path.append(curr)

    dfs("JFK")
    return path[::-1]


# Example Input
tickets = [
    ["MUC", "LHR"],
    ["JFK", "MUC"],
    ["SFO", "SJC"],
    ["LHR", "SFO"]
]

# Output
print(findItinerary(tickets))