def findCheapestPrice(n, flights, src, dst, k): # Cheapest flight within K stops
    # dist[i] = cheapest price to reach city i
    dist = [float('inf')] * n
    dist[src] = 0

    # At most k stops means at most k + 1 flights
    for _ in range(k + 1):
        # Copy so we only use routes from the previous iteration.
        # This prevents using more than one additional flight per round.
        temp = dist[:]

        for from_city, to_city, price in flights:
            if dist[from_city] != float('inf'):
                temp[to_city] = min(
                    temp[to_city],
                    dist[from_city] + price
                )

        dist = temp

    return -1 if dist[dst] == float('inf') else dist[dst] 

n = 4
flights = [
    [0, 1, 100],
    [1, 2, 100],
    [0, 2, 500],
    [2, 3, 100]
]

src = 0
dst = 2
k = 1

print(findCheapestPrice(n, flights, src, dst, k))