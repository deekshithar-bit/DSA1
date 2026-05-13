def search(arr, target): # Search in Rotated Sorted Array
    l, r = 0, len(arr) - 1

    while l <= r:
        m = l + (r - l) // 2

        if arr[m] == target:
            return m

        # Left half is sorted
        if arr[l] <= arr[m]:
            if target >= arr[l] and target < arr[m]:
                r = m - 1
            else:
                l = m + 1

        # Right half is sorted
        else:
            if target > arr[m] and target <= arr[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


# Example usage
arr = [4, 5, 6, 7, 0, 1, 2]
target = 2

result = search(arr, target)

print("Index of target:", result) 