import heapq

def kthSmallest(matrix, k): #Kth Smallest Element in a Sorted Matrix
    n = len(matrix)
    heap = []

    # Push the first element of each row
    for i in range(min(n, k)):
        heapq.heappush(heap, (matrix[i][0], i, 0))

    # Extract the smallest k-1 times
    for _ in range(k - 1):
        val, row, col = heapq.heappop(heap)

        if col + 1 < len(matrix[0]):
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))

    return heapq.heappop(heap)[0]


# Example usage
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]

k = 8

result = kthSmallest(matrix, k)
print(result)