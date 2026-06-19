def subsets(arr):
    result = []

    def backtrack(path, start): #Subsets The Power Set
        result.append(list(path))

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)

    return result


# Example
arr = [1, 2, 3]

print(subsets(arr))