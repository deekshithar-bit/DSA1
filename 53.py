def peakIndexInMountainArray(arr): #Finding Peak in a Mountain Array
    l, r = 0, len(arr) - 1

    while l < r:
        m = l + (r - l) // 2

        if arr[m + 1] > arr[m]:
            l = m + 1
        else:
            r = m

    return r


# Example usage
arr = [1, 3, 5, 7, 6, 4, 2]

peak_index = peakIndexInMountainArray(arr)

print("Peak Index:", peak_index)
print("Peak Element:", arr[peak_index])