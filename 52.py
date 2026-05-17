def searchRange(arr, target): #Find First & Last Position in Sorted Array
    ans = [-1, -1]

    # Find first occurrence
    l, r = 0, len(arr) - 1

    while l < r:
        m = l + (r - l) // 2

        if arr[m] < target:
            l = m + 1
        else:
            r = m

    if len(arr) > 0 and arr[l] == target:
        ans[0] = l

    # Find last occurrence
    l, r = 0, len(arr) - 1

    while l < r:
        m = l + (r - l + 1) // 2

        if arr[m] > target:
            r = m - 1
        else:
            l = m

    if len(arr) > 0 and arr[l] == target:
        ans[1] = l

    return ans


# Example usage
arr = [5, 7, 7, 8, 8, 10]
target = 8

print(searchRange(arr, target))