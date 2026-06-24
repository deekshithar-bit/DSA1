def combinationSum3(k, n): #Combination Sum III
    result = []
    def backtrack(remainingSum, path, start):
        if len(path) == k:
            if remainingSum == 0:
                result.append(path[:]) 
            return
        for i in range(start, 10):
            path.append(i)
            backtrack(remainingSum - i, path, i+1)
            path.pop()
    backtrack(n, [], 1)
    return result

# Example usage
print(combinationSum3(3, 7)) 