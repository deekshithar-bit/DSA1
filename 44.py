def nextGreaterElements(arr): #Next Greater Elements II
    n = len(arr)
    stack = []
    ans = [-1] * n

    stack.append(arr[n - 1])

    for i in range(2 * n - 2, -1, -1):
        while stack:
            top = stack[-1]

            if arr[i % n] < top:
                ans[i % n] = top
                break
            else:
                stack.pop()

        stack.append(arr[i % n])

    return ans


# Example input
arr = [1, 2, 1]

# Function call
result = nextGreaterElements(arr)

# Output
print(result)