from functools import lru_cache 
from typing import List

def canPartition(arr: List[int]) -> bool: #Partition Equal Subset Sum
    total = sum(arr)
    if total % 2 != 0:
        return False

    target = total // 2
    n = len(arr)

    @lru_cache(None)
    def dfs(rem, start):
        if rem == 0:
            return True
        if rem < 0:
            return False

        for i in range(start, n):
            if dfs(rem - arr[i], i + 1):
                return True
        return False

    return dfs(target, 0)


# Example usage
arr = [1, 5, 11, 5]
print(canPartition(arr))