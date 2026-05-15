def findPeakElement(arr): #Finding peak element
    l, r = 0, len(arr) - 1

    while l < r:
        m = l + (r - l) // 2

        if arr[m] < arr[m + 1]:
            l = m + 1
        else:
            r = m

    return l


# Example array
arr = [1, 3, 20, 4, 1, 0]

# Find peak index
peak_index = findPeakElement(arr)

# Print result
print("Peak element index:", peak_index)
print("Peak element value:", arr[peak_index]) 