def findClosestElements(arr, k, x): #Finding k Closest Elements
    l, r = 0, len(arr) - k

    while l < r:
        m = l + (r - l) // 2

        if x - arr[m] > arr[m + k] - x:
            l = m + 1
        else:
            r = m

    return arr[l:l + k]


# Example
arr = [1, 2, 3, 4, 5]
k = 4
x = 3

result = findClosestElements(arr, k, x)
print(result)