def nextGreaterElement(nums1, arr):
    ngeMap = {}
    stack = []
    n = len(arr)
    
    stack.append(arr[n - 1])
    ngeMap[arr[n - 1]] = -1

    for i in range(n - 2, -1, -1):
        top = stack[-1]
        if arr[i] < top:
            ngeMap[arr[i]] = top
        else:
            while stack:
                if stack[-1] < arr[i]:
                    stack.pop()
                else:
                    ngeMap[arr[i]] = stack[-1]
                    break
            if not stack:
                ngeMap[arr[i]] = -1
        stack.append(arr[i])

    ans = []
    for i in range(len(nums1)):
        ans.append(ngeMap[nums1[i]])
    
    return ans


# Example input
nums1 = [4, 1, 2]
arr = [1, 3, 4, 2]

# Function call
output = nextGreaterElement(nums1, arr)
print(output)

    