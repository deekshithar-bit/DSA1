T = int(input()) #Dutch National Flag algorithm

for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))

    low = 0
    mid = 0
    high = n - 1

    while mid <= high:
        if A[mid] == 0:
            A[low], A[mid] = A[mid], A[low]
            low += 1
            mid += 1

        elif A[mid] == 1:
            mid += 1

        elif A[mid] == 2:
            A[mid], A[high] = A[high], A[mid]
            high -= 1

    print(*A)