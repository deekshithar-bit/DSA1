def insert(arr, x): #Insert Interval
    """
    arr: list of [start, end], sorted and non-overlapping
    x: [start, end]
    returns: new list of intervals after inserting x
    """
    n = len(arr)
    ans = []
    i = 0

    # Add intervals before the new interval
    while i < n and arr[i][1] < x[0]:
        ans.append(arr[i])
        i += 1

    # Merge overlapping intervals
    while i < n and arr[i][0] <= x[1]:
        x[0] = min(x[0], arr[i][0])
        x[1] = max(x[1], arr[i][1])
        i += 1

    ans.append(x)

    # Add remaining intervals
    while i < n:
        ans.append(arr[i])
        i += 1

    return ans


# Example 1
arr = [[1, 3], [6, 9]]
x = [2, 5]

result = insert(arr, x)
print(result)