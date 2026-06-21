def permute(arr):
    result = []
    n = len(arr)
    
    def backtrack(path): #permutation 
        if len(path) == n:
            result.append(path[:])
            return
        
        for i in range(n):
            if arr[i] not in path:
                path.append(arr[i])
                backtrack(path)
                path.pop()
    
    backtrack([])
    return result


# Example
arr = [1, 2, 3]

res = permute(arr)

for r in res:
    print(r)