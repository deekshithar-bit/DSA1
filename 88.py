def subsetsWithDup(arr):
    arr.sort()
    result = []

    def backtrack(path, start): #Subset II
        result.append(path[:])

        for i in range(start, len(arr)):
            # Skip duplicates at the same recursion level
            if i > start and arr[i] == arr[i - 1]:
                continue

            path.append(arr[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)
    return result


# Example usage
arr = [1, 2, 2]

subsets = subsetsWithDup(arr)

print(subsets)