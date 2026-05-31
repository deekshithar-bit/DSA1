from collections import deque  #Sliding Window Maximum

def maxSlidingWindow(arr, k):
    res = []
    q = deque()

    i = j = 0
    while j < len(arr):
        while q and arr[j] > q[-1]:
            q.pop()

        q.append(arr[j])

        if j >= k - 1:
            res.append(q[0])

            if arr[i] == q[0]:
                q.popleft()

            i += 1

        j += 1

    return res
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(maxSlidingWindow(arr, k)) 