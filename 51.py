def findMin(a): #Find Minimum in Rotated Sorted Array
    l, r = 0, len(a) - 1

    while l <= r:

        # If the subarray is already sorted
        if a[l] <= a[r]:
            return a[l]

        m = l + (r - l) // 2

        # Check if middle element is minimum
        if m > 0 and a[m] < a[m - 1]:
            return a[m]

        # Decide which half to search
        if a[l] > a[m]:
            r = m - 1
        else:
            l = m + 1

    return -1


# Driver code
arr = [5, 6, 7, 1, 2, 3, 4]

print("Minimum element is:", findMin(arr))