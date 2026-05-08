def dailyTemperatures(arr): #Daily Temperatures 
    n = len(arr)
    ans = [0] * n
    stack = []

    stack.append(n - 1)

    for i in range(n - 2, -1, -1):
        while stack:
            top = stack[-1]

            if arr[i] >= arr[top]:
                stack.pop()
            else:
                ans[i] = top - i
                break

        stack.append(i)

    return ans


# Example input
arr = [73, 74, 75, 71, 69, 72, 76, 73]

# Output
print(dailyTemperatures(arr))