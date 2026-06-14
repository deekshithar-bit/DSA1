import heapq #Heap 

def findKthLargest(nums, k): #Kth Largest Element in an Array
    pq = []
    for num in nums:
        heapq.heappush(pq, num)
        if len(pq) > k:
            heapq.heappop(pq)
    return pq[0]

nums = [3, 2, 1, 5, 6, 4]
k = 2

print(findKthLargest(nums, k))