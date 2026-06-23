def combinationSum(arr, target): #Combination Sum
    result = []

    def backtrack(remainingSum, path, start):
        if remainingSum == 0:
            result.append(list(path))
            return

        if remainingSum < 0:
            return

        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(remainingSum - arr[i], path, i)  # i allows reuse of same number
            path.pop()

    backtrack(target, [], 0)
    return result


# Example
arr = [2, 3, 6, 7]
target = 7

print(combinationSum(arr, target))