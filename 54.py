def singleNonDuplicate(arr): #Single Element in a Sorted Array
    l, r = 0, len(arr) - 1

    while l < r:
        m = l + (r - l) // 2

        # Make sure m is not at boundaries
        if m > 0 and arr[m] == arr[m - 1]:
            leftCount = m - l

            if leftCount % 2 == 1:
                r = m - 2
            else:
                l = m + 1

        elif m < len(arr) - 1 and arr[m] == arr[m + 1]:
            leftCount = m - l

            if leftCount % 2 == 1:
                r = m - 1
            else:
                l = m + 2

        else:
            return arr[m]

    return arr[l]


# Example input
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]

# Function call
print("Single non-duplicate element is:", singleNonDuplicate(arr))