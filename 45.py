from collections import deque

def orangesRotting(grid):
    m = len(grid)
    n = len(grid[0])

    queue = deque()

    # Add all rotten oranges to queue
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                queue.append((i, j, 0))

    maxMinutes = 0

    # BFS traversal
    while queue:
        x, y, level = queue.popleft()

        if x > 0 and grid[x - 1][y] == 1:
            grid[x - 1][y] = 2
            queue.append((x - 1, y, level + 1))

        if x < m - 1 and grid[x + 1][y] == 1:
            grid[x + 1][y] = 2
            queue.append((x + 1, y, level + 1))

        if y < n - 1 and grid[x][y + 1] == 1:
            grid[x][y + 1] = 2
            queue.append((x, y + 1, level + 1))

        if y > 0 and grid[x][y - 1] == 1:
            grid[x][y - 1] = 2
            queue.append((x, y - 1, level + 1))

        maxMinutes = max(maxMinutes, level)

    # Check for any fresh orange left
    for row in grid:
        if 1 in row:
            return -1

    return maxMinutes


# Example input
grid = [
    [2,1,1],
    [1,1,0],
    [0,1,1]
]

# Function call
result = orangesRotting(grid)

# Output
print("Minutes needed:", result)