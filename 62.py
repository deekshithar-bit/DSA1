def trap(arr): #Trapping Rain Water
    n = len(arr)

    # Left max array
    maxL = [0] * n
    maxL[0] = arr[0]

    for i in range(1, n):
        maxL[i] = max(maxL[i - 1], arr[i])

    # Right max array
    maxR = [0] * n
    maxR[n - 1] = arr[n - 1]

    for i in range(n - 2, -1, -1):
        maxR[i] = max(arr[i], maxR[i + 1])

    # Calculate trapped water
    ans = 0

    for i in range(n):
        waterTrapped = min(maxL[i], maxR[i]) - arr[i]
        ans += max(waterTrapped, 0)

    return ans


# Example input
arr = [3, 0, 2, 0, 4]

# Function call
result = trap(arr)

# Output
print("Water trapped =", result)