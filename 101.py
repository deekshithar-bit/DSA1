from typing import List #Merge Intervals

def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    ans = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], intervals[i][1])
        else:
            ans.append(intervals[i])

    return ans

# Example input
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Function call
result = merge(intervals)

# Output
print(result)