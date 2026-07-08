def eraseOverlapIntervals(arr): #Non Overlapping Intervals
    if not arr:
        return 0

    arr.sort(key=lambda x: x[1])
    removeCount = 0
    k = float('-inf')

    for start, end in arr:
        if start < k:
            removeCount += 1
        else:
            k = end

    return removeCount


# Example input
arr = [[1, 2], [2, 3], [3, 4], [1, 3]]

# Output
print(eraseOverlapIntervals(arr))