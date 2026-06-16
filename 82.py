import heapq

def lastStoneWeight(stones): #Last Stone Weight
    stones = [-s for s in stones]  # max heap by negating
    heapq.heapify(stones)

    while len(stones) > 1:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)

        if y - x > 0:
            heapq.heappush(stones, -(y - x))

    return -stones[0] if stones else 0

print(lastStoneWeight([2, 7, 4, 1, 8, 1]))