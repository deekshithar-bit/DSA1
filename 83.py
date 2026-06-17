import heapq
from collections import Counter
 
def topKFrequent(arr, k): #Top K Frequent Elements
    # Count frequencies
    freq_map = Counter(arr)

    # Min heap
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]


# Example usage
arr = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(arr, k))