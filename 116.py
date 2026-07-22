def maxSubArray(arr): #Maximum Subarray Kadane’s Algorithm
    curr_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, len(arr)):
        curr_sum = max(curr_sum + arr[i], arr[i])
        max_sum = max(max_sum, curr_sum)

    return max_sum

# Example input
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Function call
result = maxSubArray(arr)

# Print the output
print("Maximum Subarray Sum:", result)