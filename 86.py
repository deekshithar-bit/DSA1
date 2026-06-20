def backtrack(n, k, start, path, result): # combinations
    if len(path) == k:
        result.append(path[:])
        return

    for i in range(start, n + 1):
        path.append(i)
        backtrack(n, k, i + 1, path, result)
        path.pop()


def combine(n, k):
    result = []
    backtrack(n, k, 1, [], result)
    return result


# Example
print(combine(4, 2))